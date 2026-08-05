from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    """
    Application settings, automatically populated by environment variables or a .env file.
    Provides a central, type-safe configuration hub for the OKF PoC.
    """
    # Project Metadata
    PROJECT_NAME: str = "OKF Knowledge Assistant PoC"
    VERSION: str = "1.0.0"

    # External APIs
     # NOTE: The current llama-index Gemini integrations read GOOGLE_API_KEY by default,
    # so we support both GEMINI_API_KEY and GOOGLE_API_KEY for maximum compatibility.
    GEMINI_API_KEY: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_COLLECTION: str = "okf_knowledge"
    QDRANT_CONCEPTS_COLLECTION: str = "okf_concepts"
    API_HOST: str = "http://localhost:8000"

    # Data Directories
    RAW_DATA_DIR: str = "data/raw"
    OKF_DATA_DIR: str = "knowledge/source_1"
    KNOWLEDGE_DIR: str = "knowledge"
    CACHE_DIR: str = "cache"
    SOURCES_CONFIG: str = "config/sources.yaml"

    # RAG Configuration Settings
    TOP_K: int = 5
    SPARSE_TOP_K: int = 5
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50
    ALPHA: float = 0.5

    # Concept extraction settings
    CONCEPT_MIN_CHARS: int = 200
    CONCEPT_MAX_CHARS: int = 4000

     # Models
    LLM_MODEL: str = "gemini-2.5-flash"
    EMBEDDING_MODEL: str = "models/text-embedding-004"
    TEMPERATURE: float = 0.1
 
    model_config = SettingsConfigDict(
        # Tells Pydantic to look for a .env file in the root directory
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra env vars not defined here
    )
 
    def get_gemini_api_key(self) -> str:
        """
        Returns a valid Gemini API key or raises a clear, actionable error.
        The placeholder value from .env.example is treated as missing.
        """
        key = self.GEMINI_API_KEY or self.GOOGLE_API_KEY
        if not key or key in ("your_gemini_api_key_here", "your_api_key_here", ""):
            raise ValueError(
                "Gemini API key is missing or still the placeholder value. "
                "Set GEMINI_API_KEY (or GOOGLE_API_KEY) in your .env file. "
                "Get a free key at https://aistudio.google.com/apikey and set "
                "GEMINI_API_KEY=AIza... before running the application."
            )
        return key
    
# Instantiate the settings object to be imported across the app

settings = Settings()