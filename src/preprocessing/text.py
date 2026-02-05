"""Text cleaning."""
import re

class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        """Clean and normalize text."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Normalize operators
        text = text.replace('×', '*').replace('÷', '/')
        
        return text.strip()
    
    @staticmethod
    def extract_variables(text: str) -> list:
        """Extract variable names."""
        return list(set(re.findall(r'\b[a-z]\b', text, re.IGNORECASE)))
