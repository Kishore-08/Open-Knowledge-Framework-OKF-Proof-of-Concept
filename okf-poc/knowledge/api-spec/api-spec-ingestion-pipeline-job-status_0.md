---
id: api-spec-ingestion-pipeline-job-status
type: concept
title: Ingestion Pipeline Job Status
description: This document represents the status JSON of an ongoing data ingestion
  pipeline run. It indicates that the pipeline is currently in the 'converting' stage,
  processing cached documentation from Kubernetes sources with a progress level of
  48%.
category: api-spec
tags:
- Data Ingestion
- Pipeline Status
- Kubernetes Documentation
- JSON Schema
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 2c74974e7374.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786398962.3954916,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "2c74974e7374",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "kubernetes"
    ]
  },
  "processed": 0,
  "progress_percent": 48,
  "prompt_tokens_estimate": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Starting the ingestion pipeline from the cache folder",
  "started_at": 1786398962.3985777,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}