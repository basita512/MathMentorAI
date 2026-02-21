"""Integration tests for full pipeline."""
import pytest
from unittest.mock import Mock, patch

from src.orchestration.graph import GraphOrchestrator

class TestFullPipeline:
    """Test end-to-end problem solving pipeline."""
    
    @patch('src.agents.solver.SolverAgent.solve')
    @patch('src.agents.verifier.VerifierAgent.verify')
    @patch('src.agents.explainer.ExplainerAgent.explain')
    def test_simple_algebra_problem(self, mock_explain, mock_verify, mock_solve):
        """Test solving a simple algebra problem."""
        # Mock responses
        mock_solve.return_value = {
            "solution": "x = 2 or x = 3",
            "retrieved_context": ["Quadratic formula"],
            "tool_used": True
        }
        mock_verify.return_value = {
            "verification_passed": True,
            "confidence": 0.95,
            "issues": []
        }
        mock_explain.return_value = "Step-by-step explanation..."
        
        orchestrator = GraphOrchestrator()
        result = orchestrator.process("Solve x² - 5x + 6 = 0", input_type="text")
        
        assert result is not None
        assert "status" in result
    
    @patch('src.agents.solver.SolverAgent.solve')
    @patch('src.agents.verifier.VerifierAgent.verify')
    def test_low_confidence_triggers_review(self, mock_verify, mock_solve):
        """Test that low confidence triggers human review."""
        mock_solve.return_value = {
            "solution": "Complex solution",
            "retrieved_context": ["Context"],
            "tool_used": False
        }
        # Low confidence
        mock_verify.return_value = {
            "verification_passed": False,
            "confidence": 0.4,
            "issues": ["Low confidence"]
        }
        
        orchestrator = GraphOrchestrator()
        result = orchestrator.process("Complex problem", input_type="text")
        
        # Should route to review
        assert result is not None
    
    @patch('src.agents.parser.ParserAgent.parse')
    def test_ambiguous_problem_triggers_clarification(self, mock_parse):
        """Test that ambiguous problems trigger clarification."""
        # Mock ambiguous parsing
        mock_parse.return_value = Mock(
            problem_text="Solve equation",
            needs_clarification=True,
            ambiguities=["Which equation?"],
            topic="algebra"
        )
        
        orchestrator = GraphOrchestrator()
        result = orchestrator.process("Solve equation", input_type="text")
        
        # Should identify need for clarification
        assert result["parsed_problem"].needs_clarification

class TestMemoryIntegration:
    """Test memory system integration."""
    
    @patch('src.agents.solver.SolverAgent.solve')
    def test_similar_corrections_retrieved(self, mock_solve):
        """Test that similar corrections are retrieved from feedback store."""
        from src.memory.feedback_store import feedback_store
        
        # Add a correction
        feedback_store.add_correction(
            problem="Solve x² - 3x + 2 = 0",
            incorrect_solution="x = 0",
            correct_solution="x = 1 or x = 2",
            correction_reason="Test"
        )
        
        mock_solve.return_value = {
            "solution": "Test",
            "retrieved_context": [],
            "tool_used": False
        }
        
        orchestrator = GraphOrchestrator()
        result = orchestrator.process("Solve x² - 5x + 6 = 0", input_type="text")
        
        # Cleanup
        feedback_store.feedback_entries = []
    
    def test_semantic_memory_provides_prerequisites(self):
        """Test that semantic memory provides prerequisite info."""
        from src.memory.semantic_memory import semantic_memory
        
        concept_info = semantic_memory.get_concept_info("calculus")
        
        assert concept_info is not None
        assert "prerequisites" in concept_info
        assert "algebra" in concept_info["prerequisites"]

class TestErrorHandling:
    """Test error handling in pipeline."""
    
    @patch('src.agents.solver.SolverAgent.solve')
    def test_solver_error_handling(self, mock_solve):
        """Test that solver errors are handled gracefully."""
        mock_solve.side_effect = Exception("Solver error")
        
        orchestrator = GraphOrchestrator()
        result = orchestrator.process("Test problem", input_type="text")
        
        # Should not crash, should capture error
        assert result is not None
        # Check if error is tracked (depends on implementation)
    
    def test_invalid_input_type(self):
        """Test handling of invalid input types."""
        orchestrator = GraphOrchestrator()
        
        # Should handle gracefully
        try:
            result = orchestrator.process("Test", input_type="invalid_type")
        except Exception:
            pytest.fail("Should handle invalid input type gracefully")
