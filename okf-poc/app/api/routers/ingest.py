from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio
from typing import Optional

# Import the orchestrator we built in Phase 2
from app.ingestion import run_ingestion_pipeline
from app.core.config import settings
from app.ingestion.status import get_status, update_status

# Tags help group endpoints neatly in the Swagger UI
router = APIRouter(prefix="/ingest", tags=["Ingestion"])

@router.get("/status")
async def get_ingestion_status():
    status = get_status()
    if "indexed_documents" not in status and "indexed" in status:
        status["indexed_documents"] = status["indexed"]
    return status

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
        current = get_status()
        if current.get("status") in {"running", "starting"}:
            return IngestResponse(
                status=current.get("status", "running"),
                message="Ingestion is already running.",
                indexed_documents=current.get("indexed_documents", current.get("indexed", 0)),
            )

        update_status(
            status="starting",
            message="Ingestion started",
            discovered=0,
            fetched=0,
            processed=0,
            failed=0,
            indexed=0,
            indexed_documents=0,
        )

        asyncio.create_task(
            asyncio.to_thread(
                run_ingestion_pipeline,
                raw_dir=request.raw_dir,
                okf_dir=request.okf_dir,
            )
        )

        return IngestResponse(
            status="started",
            message="Ingestion pipeline started in the background.",
            indexed_documents=0,
        )

    except Exception as e:
        print(f"❌ API Error during ingestion: {e}")
        raise HTTPException(status_code=500, detail=f"Ingestion pipeline failed: {str(e)}")
    
