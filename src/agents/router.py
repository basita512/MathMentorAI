"""Intent Router Agent - Routes problems to appropriate solving strategies."""
from src.agents.base import BaseAgent
from src.utils.logger import get_logger

logger = get_logger()

ROUTER_PROMPT = """You are an Intent Router for a math tutoring system.

Analyze the student's request and classify:

1. **Intent Type**:
   - solve_problem: Student wants a complete solution
   - explain_concept: Student wants to understand a concept/method
   - verify_answer: Student has an answer and wants verification
   - practice: Student wants similar practice problems

2. **Problem Topic** (choose one):
   - algebra: Complex numbers, quadratics, sequences, binomial, P&C
   - probability: Probability distributions, conditional probability
   - calculus: Limits, derivatives, optimization
   - linear_algebra: Matrices, vectors, determinants

3. **Complexity Level**:
   - basic: Straightforward application of formula
   - intermediate: Requires multiple steps or concept combinations
   - advanced: Non-standard approach or deep reasoning

4. **Required Tools** (list all that apply):
   - symbolic_solver: Needs algebraic manipulation (SymPy)
   - numerical_calculator: Needs numerical computation
   - graph_plotter: Needs visualization
   - wolfram: Complex symbolic math requiring external validation
   - none: Can solve with RAG knowledge only

Return ONLY a JSON object:
{
  "intent": "solve_problem",
  "topic": "calculus",
  "complexity": "intermediate",
  "tools": ["symbolic_solver"],
  "routing_explanation": "Brief explanation of routing decision"
}"""

class RouterAgent(BaseAgent):
    """Routes problems based on intent and topic classification."""
    
    def __init__(self):
        super().__init__(ROUTER_PROMPT, temperature=0.1)
    
    def route(self, problem_text: str) -> dict:
        """Classify intent and route the problem.
        
        Args:
            problem_text: The math problem to route
            
        Returns:
            dict with intent, topic, complexity, tools, and explanation
        """
        logger.info("Routing problem...")
        
        prompt = f"""Problem: {problem_text}

Analyze and route this problem."""
        
        response = self.invoke(prompt)
        
        # Parse JSON response
        try:
            import json
            # Extract JSON from response (handle markdown code blocks)
            if "```json" in response:
                json_str = response.split("```json")[1].split("```")[0].strip()
            elif "```" in response:
                json_str = response.split("```")[1].split("```")[0].strip()
            else:
                json_str = response.strip()
            
            routing_decision = json.loads(json_str)
            
            logger.info(f"Routed to: {routing_decision['intent']} | Topic: {routing_decision['topic']}")
            
            return routing_decision
            
        except Exception as e:
            logger.error(f"Failed to parse routing decision: {e}")
            logger.error(f"Raw response: {response}")
            
            # Fallback to default routing
            return {
                "intent": "solve_problem",
                "topic": "algebra",
                "complexity": "intermediate",
                "tools": ["none"],
                "routing_explanation": "Default routing due to parsing error"
            }
