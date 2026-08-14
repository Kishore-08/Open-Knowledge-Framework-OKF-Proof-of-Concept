---
id: api-spec-ingestion-pipeline-job-status
type: concept
title: Ingestion Pipeline Job Status
description: This document represents a status report and configuration state of an
  active documentation ingestion pipeline job. It tracks progress metrics such as
  processing stage, document counts, token estimates, and directories used for caching
  and knowledge storage.
category: api-spec
tags:
- Ingestion Pipeline
- Job Status
- Data Processing
- System Monitoring
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 1b0baa21ac59.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786514146.7111847,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "1b0baa21ac59",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": []
  },
  "processed": 0,
  "progress_percent": 48,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Starting the ingestion pipeline from the cache folder",
  "started_at": 1786514146.712674,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}