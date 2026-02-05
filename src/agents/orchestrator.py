"""Agent orchestrator."""
from src.agents.parser import ParserAgent
from src.agents.solver import SolverAgent
from src.agents.verifier import VerifierAgent
from src.agents.explainer import ExplainerAgent
from src.rag.vector_store import VectorStore
from src.utils.logger import get_logger
from src.utils.models import Solution

logger = get_logger()

class Orchestrator:
    def __init__(self):
        self.vs = VectorStore()
        self.parser = ParserAgent()
        self.solver = SolverAgent(self.vs)
        self.verifier = VerifierAgent()
        self.explainer = ExplainerAgent()
    
    def process(self, raw_input: str) -> dict:
        """Process problem through agent pipeline."""
        logger.info("=" * 60)
        logger.info("Starting agent orchestration")
        
        # Step 1: Parse
        parsed = self.parser.parse(raw_input)
        
        # Check if clarification needed
        if parsed.needs_clarification:
            return {
                'status': 'needs_clarification',
                'parsed': parsed,
                'message': f"Ambiguities found: {', '.join(parsed.ambiguities)}"
            }
        
        # Step 2: Solve
        solve_result = self.solver.solve(parsed.problem_text, parsed.topic)
        
        # Step 3: Verify
        verification = self.verifier.verify(parsed.problem_text, solve_result['solution'])
        
        # Check if HITL needed
        if verification['confidence'] < 0.6:
            return {
                'status': 'needs_review',
                'parsed': parsed,
                'solution': solve_result['solution'],
                'verification': verification,
                'message': f"Low confidence: {verification['confidence']}"
            }
        
        # Step 4: Explain
        explanation = self.explainer.explain(parsed.problem_text, solve_result['solution'])
        
        logger.info("Orchestration complete")
        logger.info("=" * 60)
        
        return {
            'status': 'success',
            'parsed': parsed,
            'solution': solve_result['solution'],
            'verification': verification,
            'explanation': explanation,
            'retrieved_context': solve_result['retrieved_context']
        }
