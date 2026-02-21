"""Solver agent with RAG and tools."""
from src.agents.base import BaseAgent
from src.rag.vector_store import VectorStore
from src.tools.sympy_solver import SymPySolver
from src.tools.web_search import WebSearchTool
from src.memory.episodic import EpisodicMemory
from src.utils.logger import get_logger
from src.utils.config import config

logger = get_logger()

SOLVER_PROMPT = """You are an expert math tutor solving JEE-level problems.

Use the provided context from knowledge base and tool results.

SOLUTION STRUCTURE (follow this exactly):

## Problem Analysis
- What is given
- What to find
- Domain/interval if specified
- Relevant concepts/formulas needed

## Step-by-Step Solution

**Step 1:** [Description]
[Work with LaTeX equations]

**Step 2:** [Description]  
[Work with LaTeX equations]

[Continue for all steps...]

**Final Step: List all solutions**
If an interval is specified (like $[0, 2\\pi]$), you MUST:
1. Substitute integer values of $k$ into general solution
2. Find ALL specific values in the interval
3. List them explicitly (e.g., $x = 0, \\frac{\\pi}{2}, \\pi, \\frac{3\\pi}{2}$)

## Final Answer
> **Solutions in [interval]:** [List ALL specific numerical/symbolic values]
>
> Example: $x = 0, \\frac{2\\pi}{3}, \\pi, \\frac{4\\pi}{3}$

## Verification (Optional)
Pick one solution and verify by substitution.

---

CRITICAL FORMATTING RULES:
- ALL math expressions MUST use LaTeX:
1. **Understand**: Restate the problem briefly
2. **Approach**: State which concepts/formulas you'll use
3. **Solution**: Show step-by-step work with clear reasoning
4. **Answer**: Final answer in a box or clear statement

CRITICAL RULES:
- For trigonometric equations in an interval like [0, 2π], you MUST list ALL specific numerical values (e.g., x = 0, π/4, π/2, 3π/4, π), NOT just general formulas with "n" or "k"
- Use LaTeX for math notation when helpful
- Explain each step clearly for a student learning
- If the solution comes from web search, mention "Based on searched references..."

Be clear, accurate, and pedagogical. ALWAYS complete the final step for interval problems!"""

class SolverAgent(BaseAgent):
    def __init__(self, vector_store: VectorStore):
        super().__init__(SOLVER_PROMPT, temperature=0.2)
        self.vs = vector_store
        self.sympy = SymPySolver()
        # Initialize episodic memory
        self.memory = EpisodicMemory()
        # Initialize web search
        self.web_search = WebSearchTool()
    
    def solve(self, problem: str, topic: str) -> dict:
        """Solve problem using RAG and tools."""
        logger.info(f"Solving {topic} problem...")
        
        # Step 1: Check episodic memory for similar past problems
        similar_problems = self.memory.retrieve_similar(problem, top_k=2)
        memory_context = ""
        
        if similar_problems:
            logger.info(f"Found {len(similar_problems)} similar problems in memory")
            memory_context = "\n\nSimilar problems solved before:\n"
            for i, sim in enumerate(similar_problems, 1):
                similarity_score = sim['similarity']
                if similarity_score > 0.7:  # Only use highly similar problems
                    memory_context += f"\n{i}. {sim['text']} (similarity: {similarity_score:.2f})\n"
        
        # Step 2: Retrieve relevant knowledge using DIVERSE HYBRID SEARCH
        # Ensures a mix of formulas, templates, and examples
        docs = self.vs.search_diverse(problem, top_k=6)
        
        # Calculate max relevance score
        max_score = max([d.get('hybrid_score', 0) for d in docs]) if docs else 0.0
        logger.info(f"Retrieved {len(docs)} documents via hybrid search (max score: {max_score:.3f})")
        
        # Step 3: Web search fallback if KB confidence is low
        web_search_used = False
        web_context = ""
        web_citations = []
        
        if config.WEB_SEARCH_ENABLED and (not docs or max_score < config.WEB_SEARCH_THRESHOLD):
            logger.warning(f"Low KB confidence ({max_score:.3f}). Triggering web search...")
            search_result = self.web_search.search(problem, max_results=3)
            
            if search_result['results']:
                web_search_used = True
                web_context = self.web_search.format_for_context(search_result)
                web_citations = self.web_search.extract_citations(search_result)
                logger.info(f"Web search returned {len(search_result['results'])} results")
        
        # Step 4: Format KB context
        context = "\n\n".join([
            f"[{d['metadata']['type']}] {d['text']} (score: {d.get('hybrid_score', 0):.3f})"
            for d in docs
        ])
        
        # Try using SymPy for certain topics
        tool_result = None
        if topic == "algebra":
            tool_result = self.sympy.solve_equation(problem)
        elif topic == "calculus":
            if "derivative" in problem.lower() or "differentiate" in problem.lower():
                # Extract expression (simplified for demo)
                tool_result = "Tool: Use differentiation rules from context"
        
        # Construct prompt with all available context
        prompt = f"""Problem: {problem}
{memory_context}

Relevant Knowledge:
{context}

{web_context}

{f'Tool Result: {tool_result}' if tool_result else ''}

Provide step-by-step solution following the structure above. 
CRITICAL: If the problem asks for solutions in an interval (like [0, 2π]), you MUST list ALL specific values, not just the general formula with k!
{f'Note: This solution uses web search results. Please cite sources appropriately.' if web_search_used else ''}"""
        
        # Invoke LLM
        solution = self.invoke(prompt)
        
        # Combine all citations (KB + Web)
        all_citations = [{'text': d['text'], 'score': d.get('hybrid_score', 0), 'source': 'knowledge_base'} for d in docs]
        all_citations.extend(web_citations)
        
        return {
            'solution': solution,
            'retrieved_context': [{'text': d['text'], 'score': d.get('hybrid_score', 0)} for d in docs],
            'similar_problems': similar_problems,
            'tool_used': tool_result is not None,
            'web_search_used': web_search_used,
            'citations': all_citations
        }
