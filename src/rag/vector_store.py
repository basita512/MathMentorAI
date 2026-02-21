"""Vector store management."""
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from typing import List, Dict
from src.utils.logger import get_logger
from src.utils.config import config

logger = get_logger()

class VectorStore:
    def __init__(self):
        logger.info("Initializing ChromaDB...")
        
        self.client = chromadb.PersistentClient(
            path=config.VECTOR_STORE_PATH,
            settings=Settings(anonymized_telemetry=False)
        )
        
        self.collection = self.client.get_or_create_collection(
            name="math_knowledge",
            metadata={"hnsw:space": "cosine"}
        )
        
        logger.info("Loading embedding model...")
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Initialize BM25 retriever (lazy initialization)
        self.bm25_retriever = None
        
        logger.info("Vector store ready")
    
    def add_documents(self, texts: list, metadatas: list, ids: list):
        """Add documents to vector store."""
        embeddings = self.embedder.encode(texts).tolist()
        
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        logger.info(f"Added {len(texts)} documents")
        
        # Reset BM25 to force rebuild on next hybrid search
        self.bm25_retriever = None
    
    def search(self, query: str, top_k: int = None) -> list:
        """Search similar documents using dense vectors only."""
        if top_k is None:
            top_k = config.TOP_K
        
        query_embedding = self.embedder.encode(query).tolist()
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        documents = []
        if results['documents']:
            for i in range(len(results['documents'][0])):
                documents.append({
                    'text': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i],
                    'score': 1 - results['distances'][0][i]  # Convert distance to similarity
                })
        
        return documents

    def search_with_filter(self, query: str, filter_dict: dict, top_k: int = 3) -> list:
        """Search with metadata filtering."""
        query_embedding = self.embedder.encode(query).tolist()
        
        try:
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k,
                where=filter_dict
            )
        except Exception as e:
            logger.warning(f"Error in search_with_filter: {e}")
            return []
            
        documents = []
        if results['documents']:
            for i in range(len(results['documents'][0])):
                documents.append({
                    'text': results['documents'][0][i],
                    'metadata': results['metadatas'][0][i],
                    'distance': results['distances'][0][i],
                    'score': 1 - results['distances'][0][i]
                })
        
        return documents
    
    def hybrid_search(
        self, 
        query: str, 
        top_k: int = None,
        dense_weight: float = 0.7,
        sparse_weight: float = 0.3
    ) -> List[Dict]:
        """
        Hybrid search combining dense vectors and BM25 sparse retrieval.
        
        Uses reciprocal rank fusion to combine results.
        
        Args:
            query: Search query
            top_k: Number of results to return
            dense_weight: Weight for dense retrieval (0-1)
            sparse_weight: Weight for sparse retrieval (0-1)
            
        Returns:
            List of documents ranked by hybrid score
        """
        if top_k is None:
            top_k = config.TOP_K
        
        logger.info(f"Hybrid search: '{query[:50]}...'")
        
        # 1. Dense retrieval (vector search)
        dense_results = self.search(query, top_k=top_k * 2)  # Get more for fusion
        
        # 2. Sparse retrieval (BM25)
        if self.bm25_retriever is None:
            self._build_bm25_index()
        
        sparse_results = self.bm25_retriever.search(query, top_k=top_k * 2)
        
        # 3. Reciprocal Rank Fusion (RRF)
        # RRF score = sum(1 / (k + rank)) for each retrieval method
        # k = 60 is a common default
        k = 60
        
        # Calculate scores for dense results
        dense_scores = {}
        for rank, doc in enumerate(dense_results, 1):
            doc_text = doc['text']
            dense_scores[doc_text] = 1.0 / (k + rank)
        
        # Calculate scores for sparse results  
        sparse_scores = {}
        for rank, (doc, _) in enumerate(sparse_results, 1):
            doc_text = doc['text']
            sparse_scores[doc_text] = 1.0 / (k + rank)
        
        # Combine scores with weights
        combined_scores = {}
        all_docs = {}
        
        # Add dense results
        for doc in dense_results:
            text = doc['text']
            all_docs[text] = doc
            combined_scores[text] = dense_weight * dense_scores.get(text, 0)
        
        # Add sparse results
        for doc, _ in sparse_results:
            text = doc['text']
            if text not in all_docs:
                all_docs[text] = doc
            combined_scores[text] = combined_scores.get(text, 0) + sparse_weight * sparse_scores.get(text, 0)
        
        # Sort by combined score
        ranked_texts = sorted(
            combined_scores.keys(),
            key=lambda x: combined_scores[x],
            reverse=True
        )[:top_k]
        
        # Build final results
        results = []
        for text in ranked_texts:
            doc = all_docs[text].copy()
            doc['hybrid_score'] = combined_scores[text]
            doc['dense_score'] = dense_scores.get(text, 0)
            doc['sparse_score'] = sparse_scores.get(text, 0)
            results.append(doc)
        
        logger.info(f"Hybrid search returned {len(results)} results")
        
        return results

    def search_diverse(
        self, 
        query: str, 
        top_k: int = 5,
        dense_weight: float = 0.7,
        sparse_weight: float = 0.3
    ) -> List[Dict]:
        """
        Search for documents and ensure diversity across types (formula, template, example).
        
        Args:
            query: Search query
            top_k: Total number of results to return
            dense_weight: Weight for dense retrieval
            sparse_weight: Weight for sparse retrieval
            
        Returns:
            List of diverse documents
        """
        # 1. Fetch more results initially to insure we have candidates from all categories
        candidates = self.hybrid_search(
            query, 
            top_k=top_k * 3, 
            dense_weight=dense_weight, 
            sparse_weight=sparse_weight
        )
        
        if not candidates:
            return []
            
        # 2. Group by type
        # We look for: 'formula', 'template_method' (or template_*), 'example_solution'
        by_type = {
            'formula': [],
            'template': [],
            'example': [],
            'other': []
        }
        
        for doc in candidates:
            dtype = doc.get('metadata', {}).get('type', 'other')
            if dtype == 'formula':
                by_type['formula'].append(doc)
            elif 'template' in dtype:
                by_type['template'].append(doc)
            elif 'example' in dtype:
                by_type['example'].append(doc)
            else:
                by_type['other'].append(doc)
        
        # 3. Select at least one of each (if available)
        diverse_results = []
        seen_texts = set()
        
        # Priority 1: Top Formula
        if by_type['formula']:
            doc = by_type['formula'][0]
            diverse_results.append(doc)
            seen_texts.add(doc['text'])
            
        # Priority 2: Top Template
        if by_type['template']:
            doc = by_type['template'][0]
            diverse_results.append(doc)
            seen_texts.add(doc['text'])
            
        # Priority 3: Top Example
        if by_type['example']:
            doc = by_type['example'][0]
            diverse_results.append(doc)
            seen_texts.add(doc['text'])
            
        # 4. Fill remaining slots with the best remaining candidates regardless of type
        # Sort remaining candidates by their hybrid score
        remaining = [c for c in candidates if c['text'] not in seen_texts]
        
        # Already sorted by hybrid_score from hybrid_search call
        for doc in remaining:
            if len(diverse_results) >= top_k:
                break
            diverse_results.append(doc)
            
        logger.info(f"Diverse search returned {len(diverse_results)} results across {len(set(d['metadata'].get('type') for d in diverse_results))} categories")
        
        return diverse_results
    
    def _build_bm25_index(self):
        """Build BM25 index from all documents in collection."""
        logger.info("Building BM25 index...")
        
        # Get all documents from ChromaDB
        all_results = self.collection.get()
        
        documents = [
            {'text': doc, 'metadata': meta}
            for doc, meta in zip(all_results['documents'], all_results['metadatas'])
        ]
        
        # Import here to avoid circular dependency
        from src.rag.bm25_retriever import BM25Retriever
        self.bm25_retriever = BM25Retriever(documents)
        
        logger.info(f"BM25 index built with {len(documents)} documents")
