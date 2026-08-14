---
id: api-spec-data-ingestion-task-status-and-metrics
type: concept
title: Data Ingestion Task Status and Metrics
description: This document contains a JSON-formatted status report for a data ingestion
  process involving Python sources. It tracks metrics such as discovered, fetched,
  indexed, and failed documents along with token estimates and timestamps.
category: api-spec
tags:
- data ingestion
- python
- metrics
- status tracking
- json
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 5a752c3d5912.json
---

{
  "completion_tokens_estimate": 114,
  "created_at": 1786383801.6818833,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 50,
  "finished_at": null,
  "id": "5a752c3d5912",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Saving OKF file 1/1",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "python"
    ]
  },
  "processed": 51,
  "progress_percent": 100,
  "prompt_tokens_estimate": 328,
  "result": null,
  "started_at": 1786383801.6828582,
  "status": "running",
  "total_documents": 51,
  "total_tokens_estimate": 442,
  "type": "ingest"
}