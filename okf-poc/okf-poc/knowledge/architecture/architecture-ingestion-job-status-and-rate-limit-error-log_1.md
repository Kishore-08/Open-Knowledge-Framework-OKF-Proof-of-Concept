---
id: architecture-ingestion-job-status-and-rate-limit-error-log
type: concept
title: Ingestion Job Status and Rate Limit Error Log
description: This document contains the execution status of a knowledge ingestion
  process that encountered an embedding rate limit error. It details the system progress,
  showing that 396 documents have been indexed, and tracks the retries for a Kubernetes-related
  source document. The ingestion job is currently r
category: architecture
tags:
- Data Ingestion
- Rate Limiting
- Kubernetes Pod Priority
- System Monitoring
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: 9c28f045ef7e.json
---

{
  "completion_tokens_estimate": 137,
  "created_at": 1786439903.3613122,
  "current_source": "Pod Priority based graceful node shutdown",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 59,
  "finished_at": null,
  "id": "9c28f045ef7e",
  "indexed": 396,
  "indexed_documents": 396,
  "message": "\u26a0\ufe0f Embedding rate limit (429) hit for 'kubernetes-pod-priority-based-graceful-node-shutdown-e5a13667', retrying in 3s (attempt 1/3)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 76,
  "progress_percent": 93,
  "prompt_tokens_estimate": 323,
  "rate_limit_hits": 10,
  "result": null,
  "stage": "indexing",
  "stage_message": "Rate limited on 'Pod Priority based graceful node shutdown' \u2014 retrying in 3s",
  "started_at": 1786439903.3619843,
  "status": "running",
  "total_documents": 1117,
  "total_tokens_estimate": 460,
  "type": "ingest"
}