"""LangGraph state machine for conditional agent orchestration."""
from langgraph.graph import StateGraph, END
from typing import Dict
import time

from src.orchestration.state import MathProblemState, create_initial_state
from src.agents.parser import ParserAgent
from src.agents.solver import SolverAgent
from src.agents.verifier import VerifierAgent
from src.agents.explainer import ExplainerAgent
from src.rag.vector_store import VectorStore
from src.memory.semantic_memory import semantic_memory
from src.memory.feedback_store import feedback_store
from src.utils.logger import get_logger

logger = get_logger()

class GraphOrchestrator:
    """
    LangGraph-based orchestrator with conditional routing.
    
    This replaces the simple linear orchestrator with a state machine
    that can route conditionally based on confidence, topic, and other factors.
    
    Now includes:
    - Semantic memory for concept dependencies and learning paths
    - Feedback store for active learning from corrections
    """
    
    def __init__(self):
        """Initialize agents and build graph."""
        logger.info("Initializing GraphOrchestrator...")
        
        # Initialize agents
        self.vector_store = VectorStore()
        self.parser = ParserAgent()
        self.solver = SolverAgent(self.vector_store)
        self.verifier = VerifierAgent()
        self.explainer = ExplainerAgent()
        
        # Build the state graph
        self.graph = self._build_graph()
        
        logger.info("GraphOrchestrator ready")

    
    def _build_graph(self) -> StateGraph:
        """
        Build the LangGraph state machine.
        
        Nodes: parse → solve → verify → explain
        Conditional edges based on state
        """
        # Create graph
        workflow = StateGraph(MathProblemState)
        
        # Add nodes
        workflow.add_node("parse", self._parse_node)
        workflow.add_node("solve", self._solve_node)
        workflow.add_node("verify", self._verify_node)
        workflow.add_node("explain", self._explain_node)
        workflow.add_node("handle_clarification", self._clarification_node)
        workflow.add_node("handle_review", self._review_node)
        
        # Set entry point
        workflow.set_entry_point("parse")
        
        # Conditional edge after parsing
        workflow.add_conditional_edges(
            "parse",
            self._should_clarify,
            {
                "clarify": "handle_clarification",
                "continue": "solve"
            }
        )
        
        # Linear edge: solve → verify
        workflow.add_edge("solve", "verify")
        
        # Conditional edge after verification
        workflow.add_conditional_edges(
            "verify",
            self._should_review,
            {
                "review": "handle_review",
                "continue": "explain"
            }
        )
        
        # Explain →  END
        workflow.add_edge("explain", END)
        
        # Handle clarification/review → END
        workflow.add_edge("handle_clarification", END)
        workflow.add_edge("handle_review", END)
        
        return workflow.compile()
    
    # ===== Node Functions =====
    
    def _parse_node(self, state: MathProblemState) -> Dict:
        """Parse the input problem."""
        logger.info("📍 Node: parse")
        
        state["agent_trace"].append({
            "agent": "parser",
            "timestamp": time.time(),
            "status": "started"
        })
        
        try:
            parsed = self.parser.parse(state["raw_input"])
            
            return {
                "parsed_problem": parsed,
                "needs_clarification": parsed.needs_clarification,
                "clarification_reason": ", ".join(parsed.ambiguities) if parsed.ambiguities else None,
                "topic": parsed.topic,
                "difficulty": parsed.difficulty,
                "question_type": parsed.question_type,
                "agent_trace": [{
                    "agent": "parser",
                    "timestamp": time.time(),
                    "status": "completed",
                    "confidence": 1.0 if not parsed.needs_clarification else 0.5
                }]
            }
        except Exception as e:
            logger.error(f"Parser error: {e}")
            return {
                "errors": [{"agent": "parser", "error": str(e)}],
                "status": "error"
            }
    
    def _solve_node(self, state: MathProblemState) -> Dict:
        """Solve the problem using RAG + tools."""
        logger.info("📍 Node: solve")
        
        state["agent_trace"].append({
            "agent": "solver",
            "timestamp": time.time(),
            "status": "started"
        })
        
        try:
            problem_text = state["parsed_problem"].problem_text
            topic = state["topic"] or "general"
            
            # Check feedback store for similar corrections
            similar_corrections = feedback_store.get_similar_corrections(problem_text, limit=3)
            if similar_corrections:
                logger.info(f"Found {len(similar_corrections)} similar past corrections")
            
            # Get concept info from semantic memory
            concept_info = semantic_memory.get_concept_info(topic)
            if concept_info:
                logger.info(f"Concept: {topic}, Prerequisites: {concept_info.get('prerequisites', [])}")
            
            solve_result = self.solver.solve(problem_text, topic)
            
            return {
                "current_solution": solve_result["solution"],
                "solution_attempts": [{
                    "attempt": 1,
                    "solution": solve_result["solution"],
                    "tool_used": solve_result.get("tool_used", False)
                }],
                "retrieved_context": solve_result["retrieved_context"],
                "retrieval_method": "hybrid",
                "similar_corrections": similar_corrections,  # Add to state
                "concept_info": concept_info,  # Add to state
                "agent_trace": [{
                    "agent": "solver",
                    "timestamp": time.time(),
                    "status": "completed"
                }]
            }
        except Exception as e:
            logger.error(f"Solver error: {e}")
            return {
                "errors": [{" agent": "solver", "error": str(e)}],
                "status": "error"
            }
    
    def _verify_node(self, state: MathProblemState) -> Dict:
        """Verify the solution."""
        logger.info("📍 Node: verify")
        
        state["agent_trace"].append({
            "agent": "verifier",
            "timestamp": time.time(),
            "status": "started"
        })
        
        try:
            problem_text = state["parsed_problem"].problem_text
            solution = state.get("current_solution") or ""
            
            # Skip verification if solver failed to produce a solution
            if not solution.strip():
                return {
                    "verification_passed": False,
                    "verification_confidence": 0.0,
                    "verification_issues": ["Solver did not produce a solution"],
                    "needs_human": True,
                    "human_trigger_reason": "Solver failed to produce output",
                    "agent_trace": [{"agent": "verifier", "timestamp": time.time(), "status": "skipped"}]
                }
            
            verification = self.verifier.verify(problem_text, solution)
            
            return {
                "verification_passed": verification["verification_passed"],
                "verification_confidence": verification["confidence"],
                "verification_issues": verification.get("issues", []),
                "needs_human": verification["confidence"] < 0.6,
                "human_trigger_reason": f"Low verification confidence: {verification['confidence']:.1%}" if verification["confidence"] < 0.6 else None,
                "agent_trace": [{
                    "agent": "verifier",
                    "timestamp": time.time(),
                    "status": "completed",
                    "confidence": verification["confidence"]
                }]
            }
        except Exception as e:
            logger.error(f"Verifier error: {e}")
            return {
                "errors": [{"agent": "verifier", "error": str(e)}],
                "status": "error"
            }
    
    def _explain_node(self, state: MathProblemState) -> Dict:
        """Generate student-friendly explanation."""
        logger.info("📍 Node: explain")
        
        state["agent_trace"].append({
            "agent": "explainer",
            "timestamp": time.time(),
            "status": "started"
        })
        
        try:
            problem_text = state["parsed_problem"].problem_text
            solution = state.get("current_solution") or ""
            
            if not solution.strip():
                return {
                    "explanation": "No solution was generated to explain.",
                    "status": "error",
                    "end_time": time.time(),
                    "agent_trace": [{"agent": "explainer", "timestamp": time.time(), "status": "skipped"}]
                }
            
            explanation = self.explainer.explain(problem_text, solution)
            
            return {
                "explanation": explanation,
                "status": "success",
                "end_time": time.time(),
                "agent_trace": [{
                    "agent": "explainer",
                    "timestamp": time.time(),
                    "status": "completed"
                }]
            }
        except Exception as e:
            logger.error(f"Explainer error: {e}")
            return {
                "errors": [{"agent": "explainer", "error": str(e)}],
                "status": "error"
            }
    
    def _clarification_node(self, state: MathProblemState) -> Dict:
        """Handle clarification needed."""
        logger.info("📍 Node: handle_clarification")
        
        return {
            "status": "needs_clarification",
            "end_time": time.time()
        }
    
    def _review_node(self, state: MathProblemState) -> Dict:
        """Handle human review needed."""
        logger.info("📍 Node: handle_review")
        
        # Still generate explanation even if review needed
        try:
            solution = state.get("current_solution") or ""
            if solution.strip():
                explanation = self.explainer.explain(
                    state["parsed_problem"].problem_text,
                    solution
                )
            else:
                explanation = "The solver could not generate a solution. Please try rephrasing your problem."
        except Exception as ex:
            logger.warning(f"Explanation in review node failed: {ex}")
            explanation = "Explanation generation failed."
        
        return {
            "explanation": explanation,
            "status": "needs_review",
            "end_time": time.time()
        }
    
    # ===== Conditional Edge Functions =====
    
    def _should_clarify(self, state: MathProblemState) -> str:
        """Decide if clarification is needed after parsing."""
        if state.get("needs_clarification", False):
            logger.info("⚠️  Conditional: Clarification needed")
            return "clarify"
        logger.info("✅ Conditional: Continue to solve")
        return "continue"
    
    def _should_review(self, state: MathProblemState) -> str:
        """Decide if human review is needed after verification."""
        if state.get("needs_human", False):
            logger.info("⚠️  Conditional: Human review needed")
            return "review"
        logger.info("✅ Conditional: Continue to explain")
        return "continue"
    
    # ===== Public Interface =====
    
    def process(self, raw_input: str, input_type: str = "text") -> Dict:
        """
        Process a math problem through the state graph.
        
        Args:
            raw_input: Raw problem text
            input_type: Type of input
            
        Returns:
            Final state as dict
        """
        logger.info("="*60)
        logger.info("🚀 Starting GraphOrchestrator")
        logger.info("="*60)
        
        # Create initial state
        initial_state = create_initial_state(raw_input, input_type)
        
        # Run the graph
        final_state = self.graph.invoke(initial_state)
        
        logger.info("="*60)
        logger.info(f"✅ GraphOrchestrator complete: {final_state['status']}")
        logger.info("="*60)
        
        return final_state
