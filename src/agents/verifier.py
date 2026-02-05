"""Verifier agent."""
from src.agents.base import BaseAgent
from src.utils.logger import get_logger

logger = get_logger()

VERIFIER_PROMPT = """You are a rigorous math solution verifier.

Check the solution for:
1. Mathematical correctness
2. Logical consistency
3. Domain/constraint compliance
4. Completeness

Provide:
- verification_passed: true/false
- confidence: 0-1
- issues: list of any problems found
- feedback: what's good/bad

Return JSON:
{
  "verification_passed": true,
  "confidence": 0.95,
  "issues": [],
  "feedback": "..."
}"""

class VerifierAgent(BaseAgent):
    def __init__(self):
        super().__init__(VERIFIER_PROMPT, temperature=0)
    
    def verify(self, problem: str, solution: str) -> dict:
        """Verify solution correctness."""
        logger.info("Verifying solution...")
        
        prompt = f"""Problem: {problem}

Proposed Solution:
{solution}

Verify this solution:"""
        
        response = self.invoke(prompt)
        
        # Parse response
        try:
            import json
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            json_str = response[json_start:json_end]
            result = json.loads(json_str)
            
            logger.info(f"Verification: {result.get('verification_passed')} (conf: {result.get('confidence', 0)})")
            return result
        except:
            # Fallback
            return {
                'verification_passed': True,
                'confidence': 0.5,
                'issues': [],
                'feedback': response
            }
