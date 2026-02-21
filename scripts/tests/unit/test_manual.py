"""Manual testing script."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agents.orchestrator import Orchestrator
from src.rag.knowledge_builder import build_knowledge_base
from src.utils.logger import get_logger

logger = get_logger()

def test_text_input():
    """Test with text input."""
    logger.info("\n" + "="*60)
    logger.info("TEST 1: Text Input - Quadratic Equation")
    logger.info("="*60)
    
    orch = Orchestrator()
    
    problem = "Solve the equation: x² - 5x + 6 = 0"
    result = orch.process(problem)
    
    print("\n📊 RESULT:")
    print(f"Status: {result['status']}")
    print(f"\nTopic: {result['parsed'].topic}")
    print(f"Difficulty: {result['parsed'].difficulty}")
    print(f"\nSolution:\n{result['solution']}")
    print(f"\nConfidence: {result['verification']['confidence']:.1%}")
    
    return result

def test_calculus():
    """Test calculus problem."""
    logger.info("\n" + "="*60)
    logger.info("TEST 2: Calculus - Differentiation")
    logger.info("="*60)
    
    orch = Orchestrator()
    
    problem = "Find the derivative of f(x) = x³ + 2x² - 5x + 1"
    result = orch.process(problem)
    
    print("\n📊 RESULT:")
    print(f"Status: {result['status']}")
    print(f"\nSolution:\n{result['solution']}")
    print(f"\nExplanation:\n{result['explanation'][:200]}...")
    
    return result

def test_memory():
    """Test memory retrieval."""
    logger.info("\n" + "="*60)
    logger.info("TEST 3: Memory System")
    logger.info("="*60)
    
    from src.memory.episodic import EpisodicMemory
    
    memory = EpisodicMemory()
    
    # Store a solution
    memory.store_solution(
        problem="x² - 4 = 0",
        solution="x = ±2",
        feedback={'correct': True, 'rating': 5}
    )
    
    # Retrieve similar
    similar = memory.retrieve_similar("x² - 9 = 0")
    
    print("\n📚 SIMILAR PROBLEMS:")
    for i, item in enumerate(similar, 1):
        print(f"\n{i}. Similarity: {item['similarity']:.2%}")
        print(f"   {item['text'][:100]}...")
    
    return similar

if __name__ == "__main__":
    print("\n🧮 AI MATH MENTOR - MANUAL TESTING\n")
    
    # Build KB first
    print("Building knowledge base...")
    build_knowledge_base()
    print("✅ Knowledge base ready\n")
    
    # Run tests
    test_text_input()
    input("\nPress Enter to continue to next test...")
    
    test_calculus()
    input("\nPress Enter to continue to next test...")
    
    test_memory()
    
    print("\n✅ All manual tests complete!")
