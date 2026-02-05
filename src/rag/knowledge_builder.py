"""Build knowledge base from files."""
import json
from pathlib import Path
from src.rag.vector_store import VectorStore
from src.utils.logger import get_logger
from src.utils.config import config

logger = get_logger()

def build_knowledge_base():
    """Load and index knowledge base."""
    logger.info("Building knowledge base...")
    
    vs = VectorStore()
    kb_path = Path(config.KNOWLEDGE_BASE_PATH)
    
    texts = []
    metadatas = []
    ids = []
    doc_id = 0
    
    # Load formulas
    for json_file in kb_path.glob("formulas/*.json"):
        with open(json_file) as f:
            data = json.load(f)
            for formula in data.get('formulas', []):
                text = f"{formula['name']}: {formula['formula']}. {formula['use']}. Example: {formula['example']}"
                texts.append(text)
                metadatas.append({'source': json_file.name, 'type': 'formula'})
                ids.append(f"doc_{doc_id}")
                doc_id += 1
    
    # Load templates
    for md_file in kb_path.glob("templates/*.md"):
        with open(md_file) as f:
            content = f.read()
            texts.append(content)
            metadatas.append({'source': md_file.name, 'type': 'template'})
            ids.append(f"doc_{doc_id}")
            doc_id += 1
    
    # Load examples
    for md_file in kb_path.glob("examples/*.md"):
        with open(md_file) as f:
            content = f.read()
            texts.append(content)
            metadatas.append({'source': md_file.name, 'type': 'example'})
            ids.append(f"doc_{doc_id}")
            doc_id += 1
    
    if texts:
        vs.add_documents(texts, metadatas, ids)
    logger.info(f"Knowledge base built: {len(texts)} documents")
    
    return vs

if __name__ == "__main__":
    build_knowledge_base()
