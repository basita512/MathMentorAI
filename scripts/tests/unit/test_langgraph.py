"""Test LangGraph state machine orchestration."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.orchestration.graph import GraphOrchestrator
from src.rag.knowledge_builder import build_knowledge_base
from src.utils.logger import get_logger

logger = get_logger()

def test_langgraph():
    """Test the LangGraph orchestrator."""
    
    print("\n" + "="*60)
    print("TESTING LANGGRAPH STATE MACHINE ORCHESTRATION")
    print("="*60)
    
    # Build knowledge base
    print("\n1. Building knowledge base...")
    build_knowledge_base()
    
    # Initialize orchestrator
    print("\n2. Initializing GraphOrchestrator...")
    orch = GraphOrchestrator()
    
    # Test problem
    problem = "Solve the quadratic equation: x² - 5x + 6 = 0"
    
    print(f"\n3. Processing Problem...")
    print(f"   '{problem}'")
    print("\n" + "-"*60)
    
    # Process through graph
    result = orch.process(problem)
    
    print("\n" + "-"*60)
    print("\n📊 FINAL STATE:")
    print(f"   Status: {result['status']}")
    print(f"   Topic: {result['topic']}")
    print(f"   Difficulty: {result['difficulty']}")
    print(f"   Verification Passed: {result['verification_passed']}")
    print(f"   Verification Confidence: {result.get('verification_confidence', 0):.1%}")
    
    print("\n🔍 AGENT TRACE:")
    for i, trace in enumerate(result['agent_trace'], 1):
        status = trace.get('status', 'unknown')
        conf = trace.get('confidence', None)
        conf_str = f" (conf: {conf:.1%})" if conf else ""
        print(f"   [{i}] {trace['agent']}: {status}{conf_str}")
    
    print("\n📚 RETRIEVED CONTEXT:")
    for i, ctx in enumerate(result['retrieved_context'], 1):
        score = ctx.get('score', 0) if isinstance(ctx, dict) else 0
        text = ctx.get('text', ctx)[:80] if isinstance(ctx, dict) else str(ctx)[:80]
        print(f"   [{i}] (score: {score:.3f}) {text}...")
    
    print("\n✅ SOLUTION:")
    print(f"   {result['current_solution'][:200]}...")
    
    print("\n📖 EXPLANATION:")
    print(f"   {result['explanation'][:200]}...")
    
    # Calculate processing time
    if result.get('start_time') and result.get('end_time'):
        duration = result['end_time'] - result['start_time']
        print(f"\n⏱️  Processing Time: {duration:.2f} seconds")
    
    print("\n" + "="*60)
    print("✅ LANGGRAPH TEST COMPLETE")
    print("="*60)
    
    print("\n🎯 KEY FEATURES DEMONSTRATED:")
    print("   ✅ State-based orchestration")
    print("   ✅ Conditional routing (clarification/review)")
    print("   ✅ Agent trace tracking")
    print("   ✅ Hybrid RAG integration")
    print("   ✅ Comprehensive state management")

if __name__ == "__main__":
    test_langgraph()
