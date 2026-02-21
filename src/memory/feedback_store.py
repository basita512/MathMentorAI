"""Feedback store for human-in-the-loop corrections and active learning."""
import json
from typing import Dict, List, Optional
from pathlib import Path
from datetime import datetime
import hashlib

from src.utils.logger import get_logger

logger = get_logger()

class FeedbackStore:
    """
    Store and manage user feedback for active learning.
    
    Tracks:
    - Incorrect solutions that were corrected
    - Ambiguous problems that needed clarification
    - Low-confidence results that were reviewed
    """
    
    def __init__(self, persist_path: str = "data/feedback/feedback_store.json"):
        """Initialize feedback store."""
        self.persist_path = Path(persist_path)
        self.persist_path.parent.mkdir(parents=True, exist_ok=True)
        
        self.feedback_entries = []
        
        if self.persist_path.exists():
            self.load()
    
    def add_correction(
        self,
        problem: str,
        incorrect_solution: str,
        correct_solution: str,
        correction_reason: str,
        metadata: Optional[Dict] = None
    ):
        """
        Record a user correction.
        
        Args:
            problem: Original problem text
            incorrect_solution: Solution that was wrong
            correct_solution: User-provided correct solution
            correction_reason: Why the solution was wrong
            metadata: Additional context
        """
        entry = {
            "id": self._generate_id(problem),
            "type": "correction",
            "timestamp": datetime.now().isoformat(),
            "problem": problem,
            "incorrect_solution": incorrect_solution,
            "correct_solution": correct_solution,
            "correction_reason": correction_reason,
            "metadata": metadata or {}
        }
        
        self.feedback_entries.append(entry)
        self.save()
        
        logger.info(f"Added correction feedback for problem: {problem[:50]}...")
    
    def add_clarification(
        self,
        original_problem: str,
        ambiguous_parts: List[str],
        clarified_problem: str,
        metadata: Optional[Dict] = None
    ):
        """Record a clarification interaction."""
        entry = {
            "id": self._generate_id(original_problem),
            "type": "clarification",
            "timestamp": datetime.now().isoformat(),
            "original_problem": original_problem,
            "ambiguous_parts": ambiguous_parts,
            "clarified_problem": clarified_problem,
            "metadata": metadata or {}
        }
        
        self.feedback_entries.append(entry)
        self.save()
        
        logger.info(f"Added clarification feedback")
    
    def add_review(
        self,
        problem: str,
        solution: str,
        verification_confidence: float,
        user_approved: bool,
        user_comments: Optional[str] = None,
        metadata: Optional[Dict] = None
    ):
        """Record a human review of low-confidence solution."""
        entry = {
            "id": self._generate_id(problem),
            "type": "review",
            "timestamp": datetime.now().isoformat(),
            "problem": problem,
            "solution": solution,
            "verification_confidence": verification_confidence,
            "user_approved": user_approved,
            "user_comments": user_comments,
            "metadata": metadata or {}
        }
        
        self.feedback_entries.append(entry)
        self.save()
        
        logger.info(f"Added review feedback: approved={user_approved}")
    
    def get_similar_corrections(self, problem: str, limit: int = 5) -> List[Dict]:
        """Find similar problems that were corrected."""
        corrections = [e for e in self.feedback_entries if e["type"] == "correction"]
        
        # Simple similarity: keyword overlap (can be improved with embeddings)
        problem_words = set(problem.lower().split())
        
        scored = []
        for correction in corrections:
            correction_words = set(correction["problem"].lower().split())
            if not correction_words:
                continue
            similarity = len(problem_words & correction_words) / len(problem_words | correction_words)
            scored.append((similarity, correction))
        
        scored.sort(reverse=True, key=lambda x: x[0])
        return [c for _, c in scored[:limit]]
    
    def get_statistics(self) -> Dict:
        """Get feedback statistics."""
        total = len(self.feedback_entries)
        
        by_type = {}
        for entry in self.feedback_entries:
            entry_type = entry["type"]
            by_type[entry_type] = by_type.get(entry_type, 0) + 1
        
        reviews = [e for e in self.feedback_entries if e["type"] == "review"]
        approved = sum(1 for r in reviews if r["user_approved"])
        
        return {
            "total_feedback": total,
            "by_type": by_type,
            "reviews_approved_rate": approved / len(reviews) if reviews else 0,
            "corrections_count": by_type.get("correction", 0),
            "clarifications_count": by_type.get("clarification", 0)
        }
    
    def get_recent_feedback(self, limit: int = 10, feedback_type: Optional[str] = None) -> List[Dict]:
        """
        Get recent feedback entries.
        
        Args:
            limit: Maximum number of entries to return
            feedback_type: Filter by type (correction, clarification, review), None for all
        """
        if feedback_type:
            entries = [e for e in self.feedback_entries if e["type"] == feedback_type]
        else:
            entries = self.feedback_entries
        
        # Sort by timestamp descending
        sorted_entries = sorted(entries, key=lambda x: x["timestamp"], reverse=True)
        return sorted_entries[:limit]
    
    def _generate_id(self, problem: str) -> str:
        """Generate unique ID for problem."""
        timestamp = datetime.now().isoformat()
        unique_string = f"{problem}{timestamp}"
        return hashlib.md5(unique_string.encode()).hexdigest()[:12]
    
    def save(self):
        """Persist feedback to disk."""
        with open(self.persist_path, 'w') as f:
            json.dump(self.feedback_entries, f, indent=2)
    
    def load(self):
        """Load feedback from disk."""
        with open(self.persist_path, 'r') as f:
            self.feedback_entries = json.load(f)
        
        logger.info(f"Loaded {len(self.feedback_entries)} feedback entries")

# Global instance
feedback_store = FeedbackStore()
