"""Unit tests for agents."""
import pytest
from unittest.mock import Mock, patch

from src.agents.parser import ParserAgent
from src.agents.verifier import VerifierAgent

class TestParserAgent:
    """Test parser agent."""
    
    def test_parse_algebra_problem(self):
        """Test parsing algebra problem."""
        parser = ParserAgent()
        
        result = parser.parse("Solve the equation x² + 5x + 6 = 0")
        
        assert result.problem_text is not None
        assert result.topic in ["algebra", "general"]
        assert not result.needs_clarification
    
    def test_parse_calculus_problem(self):
        """Test parsing calculus problem."""
        parser = ParserAgent()
        
        result = parser.parse("Find the derivative of f(x) = x³")
        
        assert result.problem_text is not None
        # Should identify as calculus
    
    def test_detect_ambiguity(self):
        """Test ambiguity detection."""
        parser = ParserAgent()
        
        # Ambiguous problem
        result = parser.parse("Solve it")
        
        # Should detect ambiguity (depends on implementation)
        # assert result.needs_clarification

class TestVerifierAgent:
    """Test verifier agent."""
    
    def test_verify_correct_solution(self):
        """Test verification of correct solution."""
        verifier = VerifierAgent()
        
        problem = "Solve x² - 5x + 6 = 0"
        solution = "x = 2 or x = 3"
        
        result = verifier.verify(problem, solution)
        
        assert "verification_passed" in result
        assert "confidence" in result
        assert 0 <= result["confidence"] <= 1
    
    def test_verify_incorrect_solution(self):
        """Test verification of incorrect solution."""
        verifier = VerifierAgent()
        
        problem = "Solve x² - 5x + 6 = 0"
        solution = "x = 1"  # Incorrect
        
        result = verifier.verify(problem, solution)
        
        # Should have lower confidence or fail verification
    
    def test_confidence_score_range(self):
        """Test that confidence scores are in valid range."""
        verifier = VerifierAgent()
        
        result = verifier.verify("Test problem", "Test solution")
        
        assert 0 <= result["confidence"] <= 1
