"""
Knowledge Base Ingestion Script

This script loads all knowledge base content (formulas, examples, templates)
into the ChromaDB vector store. Run this script:
- Once during initial setup
- Whenever you update the knowledge base content

Usage:
    python ingest_knowledge.py
    
    # To force re-ingestion (clear existing data):
    python ingest_knowledge.py --force
"""

import sys
import argparse
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from src.rag.knowledge_builder import build_knowledge_base
from src.rag.vector_store import VectorStore
from src.utils.logger import get_logger

logger = get_logger()

def main():
    parser = argparse.ArgumentParser(description="Ingest knowledge base into vector store")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-ingestion by clearing existing collection"
    )
    args = parser.parse_args()
    
    logger.info("=" * 60)
    logger.info("KNOWLEDGE BASE INGESTION")
    logger.info("=" * 60)
    
    # Check if collection already exists and has documents
    vs = VectorStore()
    collection_count = vs.collection.count()
    
    if collection_count > 0 and not args.force:
        logger.warning(f"Collection already contains {collection_count} documents")
        logger.warning("Use --force flag to re-ingest and overwrite existing data")
        
        response = input("\nProceed anyway? (y/N): ").strip().lower()
        if response != 'y':
            logger.info("Ingestion cancelled")
            return
    
    # Clear existing data if force flag is set
    if args.force and collection_count > 0:
        logger.info(f"Clearing existing collection ({collection_count} documents)...")
        # Delete and recreate collection
        vs.client.delete_collection("math_knowledge")
        vs.collection = vs.client.create_collection(
            name="math_knowledge",
            metadata={"hnsw:space": "cosine"}
        )
        logger.info("Collection cleared")
    
    # Build knowledge base
    logger.info("Starting knowledge base ingestion...")
    build_knowledge_base()
    
    # Verify
    final_count = vs.collection.count()
    logger.info("=" * 60)
    logger.info(f"INGESTION COMPLETE: {final_count} documents indexed")
    logger.info("=" * 60)
    logger.info("Vector store is ready for use. You can now run the app.")

if __name__ == "__main__":
    main()
