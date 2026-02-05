"""Solver agent with RAG and tools."""
from src.agents.base import BaseAgent
from src.rag.vector_store import VectorStore
from src.tools.sympy_solver import SymPySolver
from src.utils.logger import get_logger

logger = get_logger()

SOLVER_PROMPT = """You are an expert math tutor solving JEE-level problems.

Use the provided context from knowledge base and tool results.
Solve step-by-step:
1. State what is given and what to find
2. Identify relevant concepts/formulas
3. Apply formulas with clear steps
4. Show all calculations
5. Provide final answer

Be clear, accurate, and pedagogical."""

class SolverAgent(BaseAgent):
    def __init__(self, vector_store: VectorStore):
        super().__init__(SOLVER_PROMPT, temperature=0.2)
        self.vs = vector_store
        self.sympy = SymPySolver()
    
    def solve(self, problem: str, topic: str) -> dict:
        """Solve problem using RAG and tools."""
        logger.info(f"Solving {topic} problem...")
        
        # Retrieve relevant knowledge using HYBRID SEARCH (dense + BM25)
        docs = self.vs.hybrid_search(problem, top_k=3)
        context = "\n\n".join([
            f"[{d['metadata']['type']}] {d['text']} (score: {d.get('hybrid_score', 0):.3f})"
            for d in docs
        ])
        
        logger.info(f"Retrieved {len(docs)} documents via hybrid search")
        
        # Try using SymPy for certain topics
        tool_result = None
        if topic == "algebra":
            tool_result = self.sympy.solve_equation(problem)
        elif topic == "calculus":
            if "derivative" in problem.lower() or "differentiate" in problem.lower():
                # Extract expression (simplified for demo)
                tool_result = "Tool: Use differentiation rules from context"
        
        # Construct prompt
        prompt = f"""Problem: {problem}

Relevant Knowledge:
{context}

{f'Tool Result: {tool_result}' if tool_result else ''}

Provide step-by-step solution:"""
        
        solution = self.invoke(prompt)
        
        return {
            'solution': solution,
            'retrieved_context': [{'text': d['text'], 'score': d.get('hybrid_score', 0)} for d in docs],
            'tool_used': tool_result is not None
        }
