"""Data models."""
from pydantic import BaseModel, Field
from typing import Optional, List, Literal

class ProblemStructure(BaseModel):
    problem_text: str
    topic: Literal["algebra", "calculus", "probability", "linear_algebra"]
    difficulty: Literal["easy", "medium", "hard"] = "medium"
    variables: List[str] = []
    constraints: List[str] = []
    question_type: str = "solve"
    needs_clarification: bool = False
    ambiguities: List[str] = []

class OCRResult(BaseModel):
    text: str
    confidence: float
    needs_review: bool = False

class AudioTranscript(BaseModel):
    text: str
    confidence: float = 1.0
    unclear_sections: List[str] = []

class Solution(BaseModel):
    steps: List[str]
    final_answer: str
    confidence: float
    retrieved_context: List[str] = []
    verification_passed: bool = False
