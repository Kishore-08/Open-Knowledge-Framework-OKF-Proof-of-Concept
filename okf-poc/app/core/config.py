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
    QDRANT_CONCEPTS_COLLECTION: str = "okf_concepts"
    API_HOST: str = "http://localhost:8000"

    # Data Directories
    # Cache: Disposable data (crawled HTML, processing state) - can be deleted and rebuilt
    CACHE_DIR: str = "cache"

    # Knowledge: Source of truth (generated OKF Markdown files) - must be preserved
    KNOWLEDGE_DIR: str = "knowledge"

    # Configuration
    SOURCES_CONFIG: str = "config/sources.yaml"

    # RAG Configuration Settings
    TOP_K: int = 5
    # Citations below this score, or far below the best result for the same
    # query, are omitted.  This keeps weak vector neighbours out of the UI.
    CITATION_MIN_SCORE: float = 0.20
    CITATION_RELATIVE_SCORE: float = 0.75
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50

    # Concept extraction settings
    CONCEPT_MIN_CHARS: int = 200
    CONCEPT_MAX_CHARS: int = 4000

    # AI Provider
    AI_PROVIDER: str = "vertex"

    # Vertex AI
    VERTEX_AI_PROJECT_ID: Optional[str] = None
    VERTEX_AI_LOCATION: str = "global"

    VERTEX_LLM_MODEL: str = "gemini-3.5-flash"
    VERTEX_EMBEDDING_MODEL: str = "gemini-embedding-001"
    VERTEX_ACCESS_TOKEN: Optional[str] = None

    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = None



    # Models
    LLM_MODEL: str = "gemini-3.5-flash"

    # `gemini-3.5-flash-lite` as the alternate-quota fallback.
    LLM_FALLBACK_MODEL: str = "gemini-3.5-flash-lite"

    # gemini-embedding-2 has a separate quota pool and produces 3072-dim vectors.
    EMBEDDING_MODEL: str = "models/gemini-embedding-1"
    TEMPERATURE: float = 0.0

    # LLM resilience: retry Gemini calls on 429 quota/rate-limit errors.
    LLM_MAX_RETRIES: int = 3
    LLM_RETRY_BASE_DELAY: float = 3.0
    # Per-call timeout for Gemini REST calls. Kept short so a stalled request
    # cannot hold the query thread for a minute or more.
    LLM_TIMEOUT_SECONDS: float = 30.0
    # Answers are intentionally concise; bounding generation and disabling
    # extended thinking substantially reduces interactive query latency.
    LLM_MAX_OUTPUT_TOKENS: int = 512

    model_config = SettingsConfigDict(
        # Tells Pydantic to look for a .env file in the root directory
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra env vars not defined here
    )

    def is_vertex_enabled(self) -> bool:
        return self.AI_PROVIDER.lower() == "vertex"


    def is_gemini_enabled(self) -> bool:
        return self.AI_PROVIDER.lower() == "gemini"


    def validate_vertex_config(self) -> None:
        if not self.VERTEX_AI_PROJECT_ID:
            raise ValueError(
                "VERTEX_AI_PROJECT_ID is required when AI_PROVIDER=vertex"
            )

        if not self.VERTEX_AI_LOCATION:
            raise ValueError(
                "VERTEX_AI_LOCATION is required when AI_PROVIDER=vertex"
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
