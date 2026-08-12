---
id: api-spec-ingestion-task-status-and-rate-limit-monitoring
type: concept
title: Ingestion Task Status and Rate Limit Monitoring
description: This document contains a JSON-formatted status report for a running data
  ingestion and indexing job. It tracks metrics such as fetched and indexed documents,
  token estimates, and includes warning messages regarding API embedding rate limit
  hits.
category: api-spec
tags:
- Data Ingestion
- Rate Limiting
- Job Status
- Indexing
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 7a614db9e3f4.json
---

{
  "completion_tokens_estimate": 125,
  "created_at": 1786448792.8067577,
  "current_source": "Adding custom resources",
  "discovered": 50,
  "error": null,
  "failed": 10,
  "fetched": 50,
  "finished_at": null,
  "id": "7a614db9e3f4",
  "indexed": 36,
  "indexed_documents": 36,
  "message": "\u26a0\ufe0f Embedding rate limit (429) hit for 'kubernetes-adding-custom-resources-0f516df7', retrying in 3s (attempt 1/3)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "python"
    ]
  },
  "processed": 52,
  "progress_percent": 90,
  "prompt_tokens_estimate": 374,
  "rate_limit_hits": 23,
  "result": null,
  "stage": "indexing",
  "stage_message": "Rate limited on 'Adding custom resources' \u2014 retrying in 3s",
  "started_at": 1786448792.8072796,
  "status": "running",
  "total_documents": 1492,
  "total_tokens_estimate": 499,
  "type": "ingest"
}