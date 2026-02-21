"""Audio transcription using Groq STT API."""
from groq import Groq
from pathlib import Path
from src.utils.logger import get_logger
from src.utils.config import config
from src.utils.models import AudioTranscript

logger = get_logger()

class AudioProcessor:
    def __init__(self):
        logger.info("Initializing Groq STT client")
        self.client = Groq(api_key=config.GROQ_API_KEY)
        # Use whisper-large-v3 by default (faster) or whisper-large-v3-turbo
        self.model = getattr(config, 'WHISPER_MODEL', 'whisper-large-v3')
        logger.info(f"Groq STT ready with model: {self.model}")
    
    def transcribe(self, audio_path: str) -> AudioTranscript:
        """Transcribe audio to text using Groq API."""
        logger.info(f"Transcribing: {audio_path}")
        
        try:
            # Open audio file
            with open(audio_path, 'rb') as audio_file:
                # Call Groq transcription API (matching user's provided snippet)
                transcription = self.client.audio.transcriptions.create(
                    file=audio_file,
                    model=self.model,
                    language="en",  # English for math problems
                    temperature=0.0,
                    response_format="verbose_json", # Use verbose_json for better data handling
                    prompt="Specify math context: solve, evaluate, differentiate, integrate" 
                )
            
            # Get text from response object
            text = transcription.text.strip()
            
            # Normalize math phrases
            text = self._normalize_math(text)
            
            logger.info(f"Transcribed: {text[:50]}...")
            
            return AudioTranscript(text=text)
            
        except Exception as e:
            logger.error(f"Transcription failed: {e}")
            raise
    
    def transcribe_bytes(self, audio_bytes: bytes, suffix: str = ".wav") -> AudioTranscript:
        """Transcribe raw audio bytes (from st.audio_input) using Groq API."""
        import tempfile, os
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(audio_bytes)
            tmp_path = tmp.name
        
        try:
            result = self.transcribe(tmp_path)
        finally:
            os.unlink(tmp_path)
        
        return result
    
    def _normalize_math(self, text: str) -> str:
        """Normalize math phrases."""
        replacements = {
            "squared": "^2",
            "cubed": "^3",
            "square root of": "√",
            "square root": "√",
            "plus": "+",
            "minus": "-",
            "times": "×",
            "multiplied by": "×",
            "divided by": "÷",
            "equals": "=",
            "is equal to": "=",
            "integral": "∫",
            "derivative": "d/dx",
            "pi": "π",
            "theta": "θ",
            "alpha": "α",
            "beta": "β",
        }
        
        for phrase, symbol in replacements.items():
            text = text.replace(phrase, symbol)
        
        return text

