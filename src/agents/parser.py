"""Parser agent."""
from src.agents.base import BaseAgent
from src.utils.models import ProblemStructure
from src.utils.logger import get_logger
import json

logger = get_logger()

PARSER_PROMPT = """You are an expert at structuring math problems.

Given raw input, extract:
1. Clean problem text
2. Topic (algebra/calculus/probability/linear_algebra)
3. Difficulty (easy/medium/hard)
4. Variables involved
5. Any constraints
6. Question type (solve/prove/find/verify)
7. Whether clarification is needed
8. List any ambiguities

Return ONLY a JSON object with these fields:
{
  "problem_text": "...",
  "topic": "...",
  "difficulty": "...",
  "variables": [...],
  "constraints": [...],
  "question_type": "...",
  "needs_clarification": false,
  "ambiguities": [...]
}"""

class ParserAgent(BaseAgent):
    def __init__(self):
        super().__init__(PARSER_PROMPT, temperature=0.1)
    
    def parse(self, raw_input: str) -> ProblemStructure:
        """Parse raw input into structured problem."""
        logger.info("Parsing problem...")
        
        response = self.invoke(raw_input)
        
        # Extract JSON from response
        try:
            # Try to find JSON in response
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            json_str = response[json_start:json_end]
            
            data = json.loads(json_str)
            result = ProblemStructure(**data)
            logger.info(f"Parsed as {result.topic} problem")
            return result
        except Exception as e:
            logger.error(f"Parse failed: {e}")
            # Fallback
            return ProblemStructure(
                problem_text=raw_input,
                topic="algebra",
                needs_clarification=True,
                ambiguities=["Failed to parse structured format"]
            )
