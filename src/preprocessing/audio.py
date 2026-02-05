"""Audio transcription."""
from faster_whisper import WhisperModel
from src.utils.logger import get_logger
from src.utils.config import config
from src.utils.models import AudioTranscript

logger = get_logger()

class AudioProcessor:
    def __init__(self):
        logger.info(f"Loading Whisper model: {config.WHISPER_MODEL}")
        # Use faster-whisper with CPU
        self.model = WhisperModel(config.WHISPER_MODEL, device="cpu", compute_type="int8")
        logger.info("Whisper loaded")
    
    def transcribe(self, audio_path: str) -> AudioTranscript:
        """Transcribe audio to text."""
        logger.info(f"Transcribing: {audio_path}")
        
        # Transcribe with faster-whisper
        segments, info = self.model.transcribe(audio_path, language="en")
        
        # Combine segments into full text
        text = " ".join([segment.text for segment in segments]).strip()
        
        # Normalize math phrases
        text = self._normalize_math(text)
        
        logger.info(f"Transcribed: {text[:50]}...")
        
        return AudioTranscript(text=text)
    
    def _normalize_math(self, text: str) -> str:
        """Normalize math phrases."""
        replacements = {
            "squared": "^2",
            "cubed": "^3",
            "square root": "√",
            "plus": "+",
            "minus": "-",
            "times": "×",
            "divided by": "÷",
            "equals": "=",
        }
        
        for phrase, symbol in replacements.items():
            text = text.replace(phrase, symbol)
        
        return text
