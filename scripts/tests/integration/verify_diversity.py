
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.rag.vector_store import VectorStore
from src.utils.logger import get_logger

logger = get_logger()

def test_diversity():
    vs = VectorStore()
    
    # Use a broad topic that should have formulas, templates, and examples
    query = "trigonometry identities and solving equations"
    logger.info(f"Testing diversity for query: {query}")
    
    results = vs.search_diverse(query, top_k=6)
    
    types = [d['metadata'].get('type') for d in results]
    logger.info(f"Retrieved types: {types}")
    
    has_formula = any('formula' in t for t in types)
    has_template = any('template' in t for t in types if t)
    has_example = any('example' in t for t in types if t)
    
    print("\nRETRIEVAL DIVERSITY REPORT")
    print("-" * 30)
    print(f"Total Results: {len(results)}")
    print(f"Has Formula:   {'✅' if has_formula else '❌'}")
    print(f"Has Template:  {'✅' if has_template else '❌'}")
    print(f"Has Example:   {'✅' if has_example else '❌'}")
    print("-" * 30)
    
    for i, doc in enumerate(results, 1):
        print(f"{i}. [{doc['metadata'].get('type')}] {doc['text'][:80]}... (Score: {doc.get('hybrid_score', 0):.3f})")

if __name__ == "__main__":
    test_diversity()
