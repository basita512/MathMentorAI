"""Build knowledge base from files."""
import json
from pathlib import Path
from src.rag.vector_store import VectorStore
from src.utils.logger import get_logger
from src.utils.config import config

logger = get_logger()

def build_knowledge_base():
    """Load and index knowledge base with semantic chunking."""
    logger.info("Building knowledge base...")
    
    vs = VectorStore()
    kb_path = Path(config.KNOWLEDGE_BASE_PATH)
    
    texts = []
    metadatas = []
    ids = []
    doc_id = 0
    
    # 1. Load Formulas (Keep as is - they are already granular)
    # -------------------------------------------------------
    for json_file in kb_path.glob("formulas/*.json"):
        try:
            with open(json_file, encoding='utf-8') as f:
                data = json.load(f)
                topic = json_file.stem
                for formula in data.get('formulas', []):
                    # Build text with all available fields
                    text_parts = [
                        f"Formula: {formula['name']}",
                        f"Expression: {formula['formula']}",
                        f"Description: {formula.get('description', '')}",
                    ]
                    if 'example' in formula:
                        text_parts.append(f"Example: {formula['example']}")
                    
                    text = "\n".join(text_parts)
                    texts.append(text)
                    metadatas.append({
                        'source': json_file.name, 
                        'type': 'formula', 
                        'id': formula.get('id', ''),
                        'topic': topic
                    })
                    ids.append(f"formula_{doc_id}")
                    doc_id += 1
        except Exception as e:
            logger.error(f"Error loading {json_file}: {e}")
    
    # 2. Load Templates (Chunk by H2 headers '## ')
    # -------------------------------------------------------
    for md_file in kb_path.glob("templates/*.md"):
        try:
            with open(md_file, encoding='utf-8') as f:
                content = f.read()
                topic = md_file.stem.replace('_template', '')
                
                # Split by H2 headers
                sections = content.split('\n## ')
                
                # Handle first chunk (title/intro)
                if sections:
                    intro = sections[0].strip()
                    if intro:
                        texts.append(f"Topic Overview: {topic}\n{intro}")
                        metadatas.append({
                            'source': md_file.name,
                            'type': 'template_overview',
                            'topic': topic
                        })
                        ids.append(f"template_{doc_id}")
                        doc_id += 1
                
                # Handle subsequent sections
                for i, section in enumerate(sections[1:], 1):
                    if not section.strip(): continue
                    
                    # Extract section title (first line)
                    lines = section.split('\n')
                    section_title = lines[0].strip()
                    section_body = '\n'.join(lines[1:]).strip()
                    
                    full_text = f"Method: {section_title}\nTopic: {topic}\n\n{section_body}"
                    
                    texts.append(full_text)
                    metadatas.append({
                        'source': md_file.name,
                        'type': 'template_method',
                        'topic': topic,
                        'section': section_title
                    })
                    ids.append(f"template_{doc_id}")
                    doc_id += 1
        except Exception as e:
            logger.error(f"Error loading {md_file}: {e}")
            
    # 3. Load Examples (Chunk by '## Example')
    # -------------------------------------------------------
    for md_file in kb_path.glob("examples/*.md"):
        try:
            with open(md_file, encoding='utf-8') as f:
                content = f.read()
                topic = md_file.stem.replace('_examples', '')
                
                # Split by "## Example"
                examples = content.split('## Example')
                
                # Skip preamble if it doesn't contain useful info, or index it
                # We'll focus on the actual examples
                for i, ex in enumerate(examples[1:], 1): # Skip first part if it's just header
                    if not ex.strip(): continue
                    
                    # reconstruct the header
                    full_text = f"Example Problem ({topic}):\n## Example{ex}"
                    
                    texts.append(full_text)
                    metadatas.append({
                        'source': md_file.name,
                        'type': 'example_solution',
                        'topic': topic
                    })
                    ids.append(f"example_{doc_id}")
                    doc_id += 1
        except Exception as e:
            logger.error(f"Error loading {md_file}: {e}")
    
    if texts:
        logger.info(f"Ingesting {len(texts)} chunks into vector store...")
        vs.add_documents(texts, metadatas, ids)
    else:
        logger.warning("No documents found to ingest!")
        
    logger.info(f"Knowledge base built: {len(texts)} chunks")
    
    return vs

if __name__ == "__main__":
    build_knowledge_base()
