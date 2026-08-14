---
id: architecture-documentation-ingestion-pipeline-status
type: concept
title: Documentation Ingestion Pipeline Status
description: This document details the real-time execution status of a documentation
  ingestion and processing pipeline. It tracks the conversion of crawled FastAPI documentation
  into OKF knowledge files, showing progress metrics, source parameters, and current
  execution stage. The job is currently active and run
category: architecture
tags:
- data ingestion
- documentation crawler
- FastAPI
- pipeline status
source:
  name: Ingested document
  url: ''
created_at: '2026-08-14'
updated_at: '2026-08-14'
aliases: []
related: []
document_type: Architecture
trust_level: High
source_file: e6001e6cdc60.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786707193.3532462,
  "current_source": "",
  "discovered": 51,
  "error": null,
  "failed": 0,
  "fetched": 51,
  "finished_at": null,
  "id": "e6001e6cdc60",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "fastapi"
    ]
  },
  "processed": 51,
  "progress_percent": 69,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Converting cached raw data into OKF knowledge files",
  "started_at": 1786707193.3548312,
  "status": "running",
  "total_documents": 51,
  "total_tokens_estimate": 0,
  "type": "ingest"
}