"""Unit tests for memory systems."""
import pytest
import json
from pathlib import Path

from src.memory.semantic_memory import SemanticMemory
from src.memory.feedback_store import FeedbackStore

class TestSemanticMemory:
    """Test semantic memory knowledge graph."""
    
    def test_initialization(self, tmp_path):
        """Test semantic memory initializes with base concepts."""
        memory = SemanticMemory(persist_path=tmp_path / "test_semantic.json")
        
        stats = memory.get_graph_stats()
        assert stats["total_concepts"] > 0
        assert "algebra" in memory.graph.nodes
        assert "calculus" in memory.graph.nodes
    
    def test_get_prerequisites(self, tmp_path):
        """Test prerequisite retrieval."""
        memory = SemanticMemory(persist_path=tmp_path / "test_semantic.json")
        
        prereqs = memory.get_prerequisites("calculus")
        assert "algebra" in prereqs
        assert "trigonometry" in prereqs
    
    def test_suggest_learning_path(self, tmp_path):
        """Test learning path suggestion."""
        memory = SemanticMemory(persist_path=tmp_path / "test_semantic.json")
        
        path = memory.suggest_learning_path("calculus")
        assert len(path) > 0
        # Algebra should come before calculus
        assert path.index("algebra") < path.index("calculus")
    
    def test_add_concept(self, tmp_path):
        """Test adding new concept."""
        memory = SemanticMemory(persist_path=tmp_path / "test_semantic.json")
        
        initial_count = memory.get_graph_stats()["total_concepts"]
        memory.add_concept("complex_analysis", level=4, category="advanced", 
                          prerequisites=["calculus"])
        
        new_count = memory.get_graph_stats()["total_concepts"]
        assert new_count == initial_count + 1
        assert "complex_analysis" in memory.graph.nodes
    
    def test_get_related_concepts(self, tmp_path):
        """Test finding related concepts."""
        memory = SemanticMemory(persist_path=tmp_path / "test_semantic.json")
        
        related = memory.get_related_concepts("algebra", max_distance=2)
        assert len(related) > 0
        # All should be within distance 2
        assert all(r["distance"] <= 2 for r in related)
    
    def test_persistence(self, tmp_path):
        """Test save and load."""
        persist_path = tmp_path / "test_semantic.json"
        
        # Create and save
        memory1 = SemanticMemory(persist_path=persist_path)
        memory1.add_concept("test_concept", level=2, category="test")
        memory1.save()
        
        # Load in new instance
        memory2 = SemanticMemory(persist_path=persist_path)
        assert "test_concept" in memory2.graph.nodes

class TestFeedbackStore:
    """Test feedback store."""
    
    def test_initialization(self, tmp_path):
        """Test feedback store initializes empty."""
        store = FeedbackStore(persist_path=tmp_path / "test_feedback.json")
        
        stats = store.get_statistics()
        assert stats["total_feedback"] == 0
    
    def test_add_correction(self, tmp_path):
        """Test adding correction feedback."""
        store = FeedbackStore(persist_path=tmp_path / "test_feedback.json")
        
        store.add_correction(
            problem="x² - 5x + 6 = 0",
            incorrect_solution="x = 1 or x = 2",
            correct_solution="x = 2 or x = 3",
            correction_reason="Incorrect factorization"
        )
        
        stats = store.get_statistics()
        assert stats["total_feedback"] == 1
        assert stats["corrections_count"] == 1
    
    def test_add_clarification(self, tmp_path):
        """Test adding clarification feedback."""
        store = FeedbackStore(persist_path=tmp_path / "test_feedback.json")
        
        store.add_clarification(
            original_problem="Solve equation",
            ambiguous_parts=["Which equation?"],
            clarified_problem="Solve x² + 2x + 1 = 0"
        )
        
        stats = store.get_statistics()
        assert stats["total_feedback"] == 1
        assert stats["clarifications_count"] == 1
    
    def test_add_review(self, tmp_path):
        """Test adding review feedback."""
        store = FeedbackStore(persist_path=tmp_path / "test_feedback.json")
        
        store.add_review(
            problem="Test problem",
            solution="Test solution",
            verification_confidence=0.6,
            user_approved=True,
            user_comments="Looks good"
        )
        
        stats = store.get_statistics()
        assert stats["total_feedback"] == 1
        assert stats["reviews_approved_rate"] == 1.0
    
    def test_get_similar_corrections(self, tmp_path):
        """Test finding similar corrections."""
        store = FeedbackStore(persist_path=tmp_path / "test_feedback.json")
        
        # Add multiple corrections
        store.add_correction(
            problem="Solve x² - 5x + 6 = 0",
            incorrect_solution="Wrong",
            correct_solution="Right",
            correction_reason="Test"
        )
        store.add_correction(
            problem="Solve x² + 3x - 10 = 0",
            incorrect_solution="Wrong",
            correct_solution="Right",
            correction_reason="Test"
        )
        
        # Search for similar
        similar = store.get_similar_corrections("Solve x² - 7x + 12 = 0", limit=5)
        assert len(similar) > 0
    
    def test_get_recent_feedback(self, tmp_path):
        """Test getting recent feedback."""
        store = FeedbackStore(persist_path=tmp_path / "test_feedback.json")
        
        # Add multiple types
        store.add_correction("prob1", "inc", "corr", "reason")
        store.add_clarification("prob2", ["amb"], "clarified")
        store.add_review("prob3", "sol", 0.8, True)
        
        # Get all recent
        recent = store.get_recent_feedback(limit=10)
        assert len(recent) == 3
        
        # Filter by type
        corrections = store.get_recent_feedback(limit=10, feedback_type="correction")
        assert len(corrections) == 1
        assert corrections[0]["type"] == "correction"
    
    def test_persistence(self, tmp_path):
        """Test save and load."""
        persist_path = tmp_path / "test_feedback.json"
        
        # Create and save
        store1 = FeedbackStore(persist_path=persist_path)
        store1.add_correction("test", "inc", "corr", "reason")
        
        # Load in new instance
        store2 = FeedbackStore(persist_path=persist_path)
        assert len(store2.feedback_entries) == 1
