---
id: kubernetes-ingestion-pipeline-status-log
type: concept
title: Kubernetes Ingestion Pipeline Status Log
description: This JSON document provides real-time status metrics for a data ingestion
  pipeline processing Kubernetes sources. It includes error tracking, rate limit hits,
  token estimates, and progress percentages for the current indexing stage.
category: kubernetes
tags:
- Ingestion Pipeline
- Rate Limiting
- Kubernetes
- System Monitoring
- Task Status
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Kubernetes
trust_level: Medium
source_file: 04596aa63047.json
---

{
  "completion_tokens_estimate": 117,
  "created_at": 1786475933.1581435,
  "current_source": "*Deploy* lifecycle phase",
  "discovered": 50,
  "error": null,
  "failed": 4,
  "fetched": 50,
  "finished_at": null,
  "id": "04596aa63047",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "\u26a0\ufe0f Embedding rate limit (429) hit for 'kubernetes-deploy-lifecycle-phase-4d305e15', retrying in 3s (attempt 1/3)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "kubernetes"
    ]
  },
  "processed": 52,
  "progress_percent": 90,
  "prompt_tokens_estimate": 366,
  "rate_limit_hits": 9,
  "result": null,
  "stage": "indexing",
  "stage_message": "Rate limited on '*Deploy* lifecycle phase' \u2014 retrying in 3s",
  "started_at": 1786475933.1592777,
  "status": "running",
  "total_documents": 642,
  "total_tokens_estimate": 483,
  "type": "ingest"
}