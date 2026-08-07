from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio
from typing import Optional

# Import the orchestrator we built in Phase 2
from app.ingestion import run_ingestion_pipeline
from app.core.config import settings

# Tags help group endpoints neatly in the Swagger UI
router = APIRouter(prefix="/ingest", tags=["Ingestion"])

ingestion_status = {
    "status": "idle",
    "discovered": 0,
    "fetched": 0,
    "processed": 0,
    "failed": 0,
    "indexed": 0,
    "message": "No ingestion running",
}

@router.get("/status")
async def get_ingestion_status():
    return ingestion_status
async def _run_ingestion_background(raw_dir: str, okf_dir: str):
    global ingestion_status

    try:
        ingestion_status.update({
            "status": "running",
            "message": "Ingestion started",
            "discovered": 0,
            "fetched": 0,
            "processed": 0,
            "failed": 0,
            "indexed": 0,
        })

        result = await asyncio.to_thread(
            run_ingestion_pipeline,
            raw_dir=raw_dir,
            okf_dir=okf_dir,
        )

        ingestion_status.update({
            "status": "completed",
            "message": "Ingestion completed",
            "indexed": result.get("indexed_documents", 0),
        })

    except Exception as exc:
        ingestion_status.update({
            "status": "failed",
            "message": str(exc),
        })

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
    global ingestion_status
    """
    Triggers the OKF ingestion pipeline.
    Reads raw documents from `raw_dir`, generates OKF metadata, 
    saves them to `okf_dir`, and indexes them into Qdrant.
    """
    try:
        # Run the synchronous pipeline in a thread pool so FastAPI's event loop
        # is not blocked for the whole duration of the (possibly slow) ingest.
        if ingestion_status["status"] == "running":
            return {
                "status": "running",
                "message": "Ingestion is already running.",
            }
    
        ingestion_status.update({
            "status": "starting",
            "message": "Ingestion started",
            "discovered": 0,
            "fetched": 0,
            "processed": 0,
            "failed": 0,
            "indexed": 0,
        })

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
    
