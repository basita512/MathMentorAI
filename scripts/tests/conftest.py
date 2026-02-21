"""Pytest configuration and fixtures."""
import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

@pytest.fixture
def sample_algebra_problem():
    """Sample algebra problem for testing."""
    return "Solve the quadratic equation: x² - 5x + 6 = 0"

@pytest.fixture
def sample_calculus_problem():
    """Sample calculus problem for testing."""
    return "Find the derivative of f(x) = x³ + 2x² - 5x + 1"

@pytest.fixture
def sample_image_path(tmp_path):
    """Create a temporary test image."""
    from PIL import Image
    import numpy as np
    
    # Create simple test image with text
    img = Image.new('RGB', (200, 100), color='white')
    img_path = tmp_path / "test_problem.png"
    img.save(img_path)
    return str(img_path)

@pytest.fixture
def mock_vector_store():
    """Mock vector store for testing."""
    class MockVectorStore:
        def hybrid_search(self, query, top_k=3):
            return [
                {
                    "content": "Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a",
                    "metadata": {"source": "formulas/algebra.json"},
                    "score": 0.95
                }
            ]
    
    return MockVectorStore()

@pytest.fixture
def mock_llm_response():
    """Mock LLM response for testing."""
    return {
        "content": "x = 2 or x = 3",
        "usage": {"total_tokens": 100}
    }

@pytest.fixture(scope="session")
def cleanup_test_data():
    """Cleanup test data after all tests."""
    yield
    # Cleanup code here if needed
    import shutil
    test_dirs = ["data/test_plots", "data/test_feedback"]
    for d in test_dirs:
        if Path(d).exists():
            shutil.rmtree(d)
