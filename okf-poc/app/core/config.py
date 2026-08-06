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
    # gemini-3.5-flash also works, but the free-tier quota for it is very
    # tight (20 requests/day for fresh keys). gemini-flash-lite-latest has a
    # larger free allowance and produces good grounded answers for this PoC.
    LLM_MODEL: str = "gemini-flash-lite-latest"
    # If LLM_MODEL fails (400 unknown model / 429 quota exhausted), fall back to
    # this model. It shares the same API key but has a separate quota pool.
    LLM_FALLBACK_MODEL: str = "gemini-flash-lite-latest"
    EMBEDDING_MODEL: str = "models/gemini-embedding-001"
    TEMPERATURE: float = 0.1

    # LLM resilience: retry Gemini calls on 429 quota/rate-limit errors.
    LLM_MAX_RETRIES: int = 3
    LLM_RETRY_BASE_DELAY: float = 3.0
    # Per-call timeout for Gemini REST calls. Kept short so a stalled request
    # cannot hold the query thread for a minute or more.
    LLM_TIMEOUT_SECONDS: float = 30.0
 
    model_config = SettingsConfigDict(
        # Tells Pydantic to look for a .env file in the root directory
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra env vars not defined here
    )
 
    def has_gemini_api_key(self) -> bool:
        """
        Returns True only when a real (non-placeholder) Gemini API key is set.
        The placeholder value from .env.example is treated as missing.
        """
        key = self.GEMINI_API_KEY or self.GOOGLE_API_KEY
        return bool(key and key not in ("your_gemini_api_key_here", "your_api_key_here", ""))

    def get_gemini_api_key(self) -> str:
        """
        Returns a valid Gemini API key or raises a clear, actionable error.
        The placeholder value from .env.example is treated as missing.
        """
        key = self.GEMINI_API_KEY or self.GOOGLE_API_KEY
        if not self.has_gemini_api_key():
            raise ValueError(
                "Gemini API key is missing or still the placeholder value. "
                "Set GEMINI_API_KEY (or GOOGLE_API_KEY) in your .env file. "
                "Get a free key at https://aistudio.google.com/apikey and set "
                "GEMINI_API_KEY=AIza... before running the application."
            )
        return key
    
# Instantiate the settings object to be imported across the app

settings = Settings()