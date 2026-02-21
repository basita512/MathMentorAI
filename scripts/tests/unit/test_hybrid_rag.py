"""Quick test for hybrid RAG system."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.rag.vector_store import VectorStore
from src.rag.knowledge_builder import build_knowledge_base
from src.utils.logger import get_logger

logger = get_logger()

def test_hybrid_rag():
    """Test hybrid vs dense-only search."""
    
    print("\n" + "="*60)
    print("TESTING HYBRID RAG SYSTEM")
    print("="*60)
    
    # Build knowledge base first
    print("\n1. Building knowledge base...")
    build_knowledge_base()
    
    # Initialize vector store
    print("\n2. Initializing vector store...")
    vs = VectorStore()
    
    # Test query
    query = "How do I find the derivative of x squared?"
    
    print(f"\n3. Test Query: '{query}'")
    print("\n" + "-"*60)
    
    # Dense-only search
    print("\n📊 DENSE-ONLY VECTOR SEARCH:")
    dense_results = vs.search(query, top_k=3)
    for i, doc in enumerate(dense_results, 1):
        print(f"\n  [{i}] Score: {doc.get('score', 0):.4f}")
        print(f"      Type: {doc['metadata'].get('type', 'unknown')}")
        print(f"      Text: {doc['text'][:100]}...")
    
    print("\n" + "-"*60)
    
    # Hybrid search
    print("\n🚀 HYBRID SEARCH (Dense + BM25):")
    hybrid_results = vs.hybrid_search(query, top_k=3)
    for i, doc in enumerate(hybrid_results, 1):
        print(f"\n  [{i}] Hybrid Score: {doc.get('hybrid_score', 0):.4f}")
        print(f"      Dense: {doc.get('dense_score', 0):.4f} | Sparse: {doc.get('sparse_score', 0):.4f}")
        print(f"      Type: {doc['metadata'].get('type', 'unknown')}")
        print(f"      Text: {doc['text'][:100]}...")
    
    print("\n" + "="*60)
    print("✅ HYBRID RAG TEST COMPLETE")
    print("="*60)
    
    # Test with algebra query
    print("\n\n" + "="*60)
    print("TESTING WITH ALGEBRA QUERY")
    print("="*60)
    
    query2 = "quadratic equation formula"
    print(f"\nQuery: '{query2}'")
    
    print("\n🚀 HYBRID RESULTS:")
    results2 = vs.hybrid_search(query2, top_k=3)
    for i, doc in enumerate(results2, 1):
        print(f"\n  [{i}] Score: {doc.get('hybrid_score', 0):.4f}")
        print(f"      {doc['text'][:150]}...")
    
    print("\n✅ Tests passed! Hybrid RAG is working.")

if __name__ == "__main__":
    test_hybrid_rag()
