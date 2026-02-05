"""OCR processing."""
import easyocr
from PIL import Image
import numpy as np
from src.utils.logger import get_logger
from src.utils.config import config
from src.utils.models import OCRResult

logger = get_logger()

class OCRProcessor:
    def __init__(self):
        logger.info("Initializing EasyOCR...")
        # Initialize EasyOCR with English language
        self.reader = easyocr.Reader(['en'], gpu=False)
        logger.info("OCR initialized")
    
    def process(self, image_path: str) -> OCRResult:
        """Extract text from image."""
        logger.info(f"Processing: {image_path}")
        
        # Read text from image
        result = self.reader.readtext(image_path)
        
        if not result:
            return OCRResult(text="", confidence=0.0, needs_review=True)
        
        # Extract text and confidence scores
        texts = []
        confidences = []
        
        for detection in result:
            # detection is (bbox, text, confidence)
            texts.append(detection[1])
            confidences.append(detection[2])
        
        full_text = " ".join(texts)
        avg_conf = float(np.mean(confidences)) if confidences else 0.0
        
        needs_review = avg_conf < config.OCR_CONFIDENCE_THRESHOLD
        
        logger.info(f"Extracted: {full_text[:50]}... (conf: {avg_conf:.2f})")
        
        return OCRResult(
            text=full_text,
            confidence=avg_conf,
            needs_review=needs_review
        )

