from pydantic_settings import BaseSettings
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
    OPENAI_API_KEY: Optional[str] = None
    QDRANT_URL: str = "http://localhost:6333"
    API_HOST: str = "http://localhost:8000"

    # Data Directories
    RAW_DATA_DIR: str = "data/raw"
    OKF_DATA_DIR: str = "knowledge/source_1"

    # RAG Configuration Settings
    SIMILARITY_TOP_K: int = 5
    SPARSE_TOP_K: int = 5
    CHUNK_SIZE: int = 512
    CHUNK_OVERLAP: int = 50

    class Config:
        # Tells Pydantic to look for a .env file in the root directory
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore" # Ignore extra env vars not defined here

# Instantiate the settings object to be imported across the app
settings = Settings()