"""Unit tests for RAG vector store."""
import pytest
from unittest.mock import Mock, patch

from src.rag.vector_store import VectorStore

class TestVectorStore:
    """Test hybrid RAG vector store."""
    
    @patch('src.rag.vector_store.chromadb.Client')
    def test_initialization(self, mock_client):
        """Test vector store initializes collections."""
        store = VectorStore()
        assert store.collection is not None
    
    @patch('src.rag.vector_store.chromadb.Client')
    def test_add_documents(self, mock_client):
        """Test adding documents to vector store."""
        store = VectorStore()
        
        docs = [
            {"content": "Test formula", "metadata": {"source": "test"}},
            {"content": "Another formula", "metadata": {"source": "test2"}}
        ]
        
        # Should not raise error
        try:
            store.add_documents(docs)
        except Exception as e:
            pytest.fail(f"add_documents raised {e}")
    
    @patch('src.rag.vector_store.chromadb.Client')
    def test_dense_search(self, mock_client):
        """Test dense vector search."""
        store = VectorStore()
        
        # Mock collection query
        mock_collection = Mock()
        mock_collection.query.return_value = {
            "documents": [["Test result"]],
            "metadatas": [[{"source": "test"}]],
            "distances": [[0.1]]
        }
        store.collection = mock_collection
        
        results = store.dense_search("test query", top_k=3)
        
        assert len(results) > 0
        assert "content" in results[0]
        assert "metadata" in results[0]
    
    @patch('src.rag.vector_store.chromadb.Client')
    def test_hybrid_search(self, mock_client):
        """Test hybrid (dense + sparse) search."""
        store = VectorStore()
        
        # Mock both dense and sparse returns
        mock_collection = Mock()
        mock_collection.query.return_value = {
            "documents": [["Dense result"]],
            "metadatas": [[{"source": "dense"}]],
            "distances": [[0.1]]
        }
        store.collection = mock_collection
        
        # Mock BM25
        store.bm25_index = Mock()
        store.bm25_corpus = [{"content": "Sparse result", "metadata": {"source": "sparse"}}]
        store.bm25_index.get_scores.return_value = [0.5]
        
        results = store.hybrid_search("test query", top_k=3)
        
        # Should combine results from both methods
        assert len(results) > 0

class TestRAGRetrieval:
    """Test RAG retrieval quality."""
    
    @patch('src.rag.vector_store.chromadb.Client')
    def test_retrieval_for_algebra(self, mock_client):
        """Test retrieving algebra formulas."""
        store = VectorStore()
        
        mock_collection = Mock()
        mock_collection.query.return_value = {
            "documents": [["Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a"]],
            "metadatas": [[{"source": "formulas/algebra.json", "topic": "algebra"}]],
            "distances": [[0.05]]
        }
        store.collection = mock_collection
        store.bm25_index = None  # Skip BM25 for this test
        
        results = store.hybrid_search("solve quadratic equation", top_k=3)
        
        assert len(results) > 0
        assert "quadratic" in results[0]["content"].lower()
    
    @patch('src.rag.vector_store.chromadb.Client')
    def test_retrieval_for_calculus(self, mock_client):
        """Test retrieving calculus formulas."""
        store = VectorStore()
        
        mock_collection = Mock()
        mock_collection.query.return_value = {
            "documents": [["Power rule: d/dx(x^n) = n·x^(n-1)"]],
            "metadatas": [[{"source": "formulas/calculus.json", "topic": "calculus"}]],
            "distances": [[0.08]]
        }
        store.collection = mock_collection
        store.bm25_index = None
        
        results = store.hybrid_search("find derivative power rule")
        
        assert len(results) > 0
        assert "derivative" in results[0]["content"].lower() or "power" in results[0]["content"].lower()
