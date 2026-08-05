from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# Import the orchestrator we built in Phase 2
from app.ingestion import run_ingestion_pipeline
from app.core.config import settings

# Tags help group endpoints neatly in the Swagger UI
router = APIRouter(prefix="/ingest", tags=["Ingestion"])

class IngestRequest(BaseModel):
    """Payload definition for triggering ingestion."""
    raw_dir: str = settings.RAW_DATA_DIR
    okf_dir: str = settings.OKF_DATA_DIR
class IngestResponse(BaseModel):
    """Structured response confirming ingestion status."""
    status: str
    message: str
    indexed_documents: int = 0

@router.post("/", response_model=IngestResponse)
async def ingest_documents(request: IngestRequest):
    """
    Triggers the OKF ingestion pipeline.
    Reads raw documents from `raw_dir`, generates OKF metadata, 
    saves them to `okf_dir`, and indexes them into Qdrant.
    """
    try:
        # Run the synchronous pipeline
        # Note: For massive datasets in production, this should be dispatched as a background Celery/RabbitMQ task.
        result = run_ingestion_pipeline(raw_dir=request.raw_dir, okf_dir=request.okf_dir)
        
        status = result.get("status", "unknown")
        
        if status == "skipped":
            return IngestResponse(status="skipped", message=result.get("message", ""), indexed_documents=0)
            
        return IngestResponse(
            status=status,
            message="Ingestion pipeline completed successfully.",
            indexed_documents=result.get("indexed_documents", 0)
        )
        
    except Exception as e:
        print(f"❌ API Error during ingestion: {e}")
        raise HTTPException(status_code=500, detail=f"Ingestion pipeline failed: {str(e)}")