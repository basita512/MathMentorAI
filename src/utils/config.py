"""Configuration management with YAML and .env support."""
from dotenv import load_dotenv
import os
import yaml
from pathlib import Path
from typing import Any, Dict, Optional

load_dotenv()

class Config:
    """
    Configuration manager supporting both .env and YAML files.
    
    Priority order (highest to lowest):
    1. Environment variables
    2. YAML configuration files
    3. Default values
    """
    
    def __init__(self, config_dir: str = "config"):
        """Initialize configuration."""
        self.config_dir = Path(config_dir)
        self._yaml_configs = {}
        
        # Load YAML configurations if available
        if self.config_dir.exists():
            self._load_yaml_configs()
        
        # API Keys (always from .env for security)
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        
        # LLM Configuration
        self.LLM_MODEL = self._get("llm.model", "LLM_MODEL", "llama-3.3-70b-versatile")
        self.GROQ_TEMPERATURE = float(self._get("llm.temperature", "GROQ_TEMPERATURE", "0.2"))
        self.MAX_TOKENS = int(self._get("llm.max_tokens", "MAX_TOKENS", "4000"))
        
        # Paths
        self.VECTOR_STORE_PATH = self._get("vector_store.persist_path", "VECTOR_STORE_PATH", "./data/vector_store")
        self.KNOWLEDGE_BASE_PATH = self._get("knowledge_base.formulas_path", "KNOWLEDGE_BASE_PATH", "./knowledge_base")
        
        # OCR
        self.OCR_CONFIDENCE_THRESHOLD = float(self._get("ocr.confidence_threshold", "OCR_CONFIDENCE_THRESHOLD", "0.75"))
        
        # Whisper
        self.WHISPER_MODEL = self._get("whisper.model", "WHISPER_MODEL", "whisper-large-v3")
        
        # Web Search
        self.TAVILY_API_KEY = self._get("web_search.tavily_api_key", "TAVILY_API_KEY", None)
        self.WEB_SEARCH_ENABLED = self._get_bool("web_search.enabled", "WEB_SEARCH_ENABLED", True)
        self.WEB_SEARCH_THRESHOLD = float(self._get("web_search.threshold", "WEB_SEARCH_THRESHOLD", "0.3"))
        
        # RAG Configuration
        self.TOP_K = int(self._get("hybrid_retrieval.top_k", "TOP_K_RETRIEVAL", "5"))
        self.CHUNK_SIZE = int(self._get("knowledge_base.chunk_size", "CHUNK_SIZE", "512"))
        self.CHUNK_OVERLAP = int(self._get("knowledge_base.chunk_overlap", "CHUNK_OVERLAP", "50"))
        self.BM25_WEIGHT = float(self._get("hybrid_retrieval.bm25.weight", "BM25_WEIGHT", "0.3"))
        self.DENSE_WEIGHT = float(self._get("hybrid_retrieval.dense.weight", "DENSE_WEIGHT", "0.7"))
        
        # Memory
        self.MEMORY_COLLECTION = self._get("memory.collection_name", "MEMORY_COLLECTION_NAME", "math_solutions")
        
        # HITL Configuration
        self.HITL_ENABLED = self._get_bool("hitl.enabled", "HITL_ENABLED", True)
        self.HITL_CONFIDENCE_THRESHOLD = float(self._get("hitl.confidence_threshold", "HITL_CONFIDENCE_THRESHOLD", "0.7"))
        
        # Embedding Model
        self.EMBEDDING_MODEL = self._get("embeddings.model", "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
        
    def _load_yaml_configs(self):
        """Load all YAML configuration files."""
        yaml_files = ["agent_config.yaml", "rag_config.yaml", "model_config.yaml"]
        
        for yaml_file in yaml_files:
            file_path = self.config_dir / yaml_file
            if file_path.exists():
                with open(file_path, 'r') as f:
                    config_name = yaml_file.replace(".yaml", "")
                    self._yaml_configs[config_name] = yaml.safe_load(f)
    
    def _get(self, yaml_path: str, env_key: str, default: Any) -> Any:
        """
        Get configuration value with priority: env > yaml > default.
        
        Args:
            yaml_path: Dot-notation path in YAML (e.g., "llm.model")
            env_key: Environment variable name
            default: Default value if not found
        """
        # First check environment variable
        env_value = os.getenv(env_key)
        if env_value is not None:
            return env_value
        
        # Then check YAML configs
        yaml_value = self._get_from_yaml(yaml_path)
        if yaml_value is not None:
            return yaml_value
        
        # Finally return default
        return default
    
    def _get_bool(self, yaml_path: str, env_key: str, default: bool) -> bool:
        """Get boolean configuration value."""
        value = self._get(yaml_path, env_key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ("true", "1", "yes", "on")
        return bool(value)
    
    def _get_from_yaml(self, path: str) -> Optional[Any]:
        """Get value from YAML configs using dot notation."""
        parts = path.split(".")
        
        # Try each YAML config file
        for config in self._yaml_configs.values():
            current = config
            try:
                for part in parts:
                    current = current[part]
                return current
            except (KeyError, TypeError):
                continue
        
        return None
    
    def get_agent_config(self, agent_name: str) -> Dict[str, Any]:
        """Get specific agent configuration."""
        agent_config = self._yaml_configs.get("agent_config", {})
        agents = agent_config.get("agents", {})
        return agents.get(agent_name, {})
    
    def get_model_override(self, agent_name: str) -> Dict[str, Any]:
        """Get model-specific overrides for an agent."""
        model_config = self._yaml_configs.get("model_config", {})
        overrides = model_config.get("overrides", {})
        return overrides.get(agent_name, {})

config = Config()

