---
id: api-spec-ingestion-pipeline-job-status-log
type: concept
title: Ingestion Pipeline Job Status Log
description: This document contains a JSON-formatted status report for an ingestion
  pipeline run, specifically showing the progress of processing crawled documentation.
  It tracks metrics such as active stages, estimated tokens, and task parameters configuration,
  indicating a current status of 'running' at 48% pr
category: api-spec
tags:
- Data Ingestion
- Pipeline Monitoring
- JSON Schema
- Task Automation
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 21aa420c3c19.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786440705.2595544,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "21aa420c3c19",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 0,
  "progress_percent": 48,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Starting the ingestion pipeline from the cache folder",
  "started_at": 1786440705.2610922,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}