"""State definitions for LangGraph orchestration."""
from typing import TypedDict, List, Dict, Optional, Annotated
from src.utils.models import ProblemStructure
import operator

class MathProblemState(TypedDict):
    """
    Comprehensive state for math problem solving pipeline.
    
    This state is shared across all agents and updated as the problem
    flows through the graph.
    """
    
    # Input
    raw_input: str
    input_type: str  # "text", "image", "audio"
    input_metadata: Optional[Dict]  # OCR confidence, audio quality, etc.
    
    # Parsing
    parsed_problem: Optional[ProblemStructure]
    needs_clarification: bool
    clarification_reason: Optional[str]
    
    # Topic & Routing
    topic: Optional[str]  # "algebra", "calculus", "probability", "linear_algebra"
    difficulty: Optional[str]  # "easy", "medium", "hard"
    question_type: Optional[str]  # "solve", "prove", "find", "verify"
    
    # RAG Retrieval
    retrieved_context: Annotated[List[Dict], operator.add]  # Accumulate all retrievals
    retrieval_quality: Optional[float]  # 0-1 score
    retrieval_method: Optional[str]  # "hybrid", "dense", "sparse"
    
    # Solution
    solution_attempts: Annotated[List[Dict], operator.add]  # Track all attempts
    current_solution: Optional[str]
    tool_results: Optional[Dict]
    
    # Verification
    verification_passed: bool
    verification_confidence: Optional[float]  # 0-1
    verification_issues: Annotated[List[str], operator.add]  # Accumulate issues
    
    # Explanation
    explanation: Optional[str]
    
    # HITL & Status
    needs_human: bool
    human_trigger_reason: Optional[str]
    status: str  # "processing", "needs_clarification", "needs_review", "success", "error"
    
    # Errors & Debugging
    errors: Annotated[List[Dict], operator.add]  # Track all errors
    agent_trace: Annotated[List[Dict], operator.add]  # Agent execution log
    
    # Metrics
    start_time: Optional[float]
    end_time: Optional[float]
    total_tokens: Optional[int]


def create_initial_state(raw_input: str, input_type: str = "text") -> MathProblemState:
    """
    Create initial state for a new problem.
    
    Args:
        raw_input: Raw problem text
        input_type: Type of input
        
    Returns:
        Initial state dict
    """
    import time
    
    return MathProblemState(
        # Input
        raw_input=raw_input,
        input_type=input_type,
        input_metadata=None,
        
        # Parsing
        parsed_problem=None,
        needs_clarification=False,
        clarification_reason=None,
        
        # Topic & Routing
        topic=None,
        difficulty=None,
        question_type=None,
        
        # RAG
        retrieved_context=[],
        retrieval_quality=None,
        retrieval_method=None,
        
        # Solution
        solution_attempts=[],
        current_solution=None,
        tool_results=None,
        
        # Verification
        verification_passed=False,
        verification_confidence=None,
        verification_issues=[],
        
        # Explanation
        explanation=None,
        
        # HITL
        needs_human=False,
        human_trigger_reason=None,
        status="processing",
        
        # Errors
        errors=[],
        agent_trace=[],
        
        # Metrics
        start_time=time.time(),
        end_time=None,
        total_tokens=0
    )
