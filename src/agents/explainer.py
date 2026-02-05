"""Explainer agent."""
from src.agents.base import BaseAgent
from src.utils.logger import get_logger

logger = get_logger()

EXPLAINER_PROMPT = """You are a patient math tutor explaining solutions to JEE students.

Given a solution, explain it clearly with:
1. Key concepts involved
2. Step-by-step breakdown (why each step)
3. Common mistakes to avoid
4. Related concepts to explore

Be encouraging and pedagogical. Use analogies when helpful."""

class ExplainerAgent(BaseAgent):
    def __init__(self):
        super().__init__(EXPLAINER_PROMPT, temperature=0.7)
    
    def explain(self, problem: str, solution: str) -> str:
        """Generate student-friendly explanation."""
        logger.info("Generating explanation...")
        
        prompt = f"""Problem: {problem}

Solution:
{solution}

Explain this clearly for a student:"""
        
        explanation = self.invoke(prompt)
        return explanation
