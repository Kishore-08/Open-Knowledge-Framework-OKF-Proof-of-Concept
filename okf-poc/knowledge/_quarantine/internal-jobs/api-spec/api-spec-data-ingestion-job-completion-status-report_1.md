---
id: api-spec-data-ingestion-job-completion-status-report
type: concept
title: Data Ingestion Job Completion Status Report
description: This document represents a JSON status report for a completed data ingestion
  job. It details execution metadata such as start and finish times, document processing
  counts, token estimates, and the final success status of the ingestion pipeline.
category: api-spec
tags:
- Data Ingestion
- JSON Metadata
- Job Status
- Document Indexing
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: d2a0eb32e885.json
---

{
  "completion_tokens_estimate": 133,
  "created_at": 1786518860.4795687,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": 1786518864.5067687,
  "id": "d2a0eb32e885",
  "indexed": 2,
  "indexed_documents": 2,
  "message": "Ingestion completed",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": []
  },
  "processed": 2,
  "progress_percent": 100,
  "prompt_tokens_estimate": 359,
  "rate_limit_hits": 0,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786518860.480264,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 492,
  "type": "ingest"
}