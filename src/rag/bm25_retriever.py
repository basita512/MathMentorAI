"""BM25 sparse retrieval for keyword-based matching."""
from rank_bm25 import BM25Okapi
from typing import List, Dict, Tuple
import re
from src.utils.logger import get_logger

logger = get_logger()

class BM25Retriever:
    """Sparse retrieval using BM25 algorithm."""
    
    def __init__(self, documents: List[Dict[str, str]]):
        """
        Initialize BM25 retriever.
        
        Args:
            documents: List of dicts with 'text' and 'metadata' keys
        """
        logger.info(f"Initializing BM25 with {len(documents)} documents")
        
        self.documents = documents
        
        # Tokenize all documents
        self.tokenized_corpus = [
            self._tokenize(doc['text']) 
            for doc in documents
        ]
        
        # Create BM25 index
        self.bm25 = BM25Okapi(self.tokenized_corpus)
        
        logger.info("BM25 index created")
    
    def _tokenize(self, text: str) -> List[str]:
        """
        Tokenize text with math notation awareness.
        
        Args:
            text: Input text
            
        Returns:
            List of tokens
        """
        # Preserve math notation as single tokens
        # e.g., "x²", "∫", "∂", etc.
        
        # Lowercase
        text = text.lower()
        
        # Split on whitespace and punctuation, but preserve math symbols
        tokens = re.findall(r'[a-z0-9]+|[²³⁴⁵⁶⁷⁸⁹⁰]|[∫∂∇√±×÷≠≤≥∈∉⊂⊃∩∪]', text)
        
        return tokens
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[Dict, float]]:
        """
        Search for relevant documents using BM25.
        
        Args:
            query: Search query
            top_k: Number of results to return
            
        Returns:
            List of (document, score) tuples
        """
        logger.info(f"BM25 search: '{query[:50]}...'")
        
        # Tokenize query
        query_tokens = self._tokenize(query)
        
        # Get BM25 scores
        scores = self.bm25.get_scores(query_tokens)
        
        # Get top-k indices
        top_indices = scores.argsort()[-top_k:][::-1]
        
        # Return documents with scores
        results = [
            (self.documents[i], float(scores[i]))
            for i in top_indices
        ]
        
        logger.info(f"Found {len(results)} results")
        
        return results
