"""Episodic memory for past solutions."""
from datetime import datetime
from pathlib import Path
import json
from src.rag.vector_store import VectorStore
from src.utils.logger import get_logger
from src.utils.config import config

logger = get_logger()

class EpisodicMemory:
    def __init__(self):
        self.vs = VectorStore()
        # Use separate collection for memory
        from chromadb.config import Settings
        import chromadb
        
        client = chromadb.PersistentClient(
            path=config.VECTOR_STORE_PATH,
            settings=Settings(anonymized_telemetry=False)
        )
        
        self.collection = client.get_or_create_collection(
            name=config.MEMORY_COLLECTION,
            metadata={"hnsw:space": "cosine"}
        )
    
    def store_solution(self, problem: str, solution: str, feedback: dict = None):
        """Store solved problem in memory."""
        doc_id = f"memory_{datetime.now().timestamp()}"
        
        memory_text = f"Problem: {problem}\nSolution: {solution}"
        
        metadata = {
            'timestamp': datetime.now().isoformat(),
            'problem': problem,
            'has_feedback': feedback is not None
        }
        
        if feedback:
            metadata['user_rating'] = feedback.get('rating', 0)
            metadata['was_correct'] = feedback.get('correct', True)
        
        # Embed and store
        from sentence_transformers import SentenceTransformer
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        embedding = embedder.encode(memory_text).tolist()
        
        self.collection.add(
            documents=[memory_text],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[doc_id]
        )
        
        logger.info(f"Stored solution in memory: {doc_id}")
    
    def retrieve_similar(self, problem: str, top_k: int = 3) -> list:
        """Retrieve similar past solutions."""
        from sentence_transformers import SentenceTransformer
        embedder = SentenceTransformer('all-MiniLM-L6-v2')
        
        query_embedding = embedder.encode(problem).tolist()
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        if not results['documents'] or not results['documents'][0]:
            return []
        
        similar = []
        for i in range(len(results['documents'][0])):
            similar.append({
                'text': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'similarity': 1 - results['distances'][0][i]
            })
        
        return similar
