---
id: api-spec-ingestion-process-status-report
type: concept
title: Ingestion Process Status Report
description: This document contains JSON-formatted metrics and status data for a document
  ingestion process, including token estimates, cache directories, and completion
  statistics. It reports that the job is currently running with 100 percent progress,
  50 fetched documents, and 68 processed items.
category: api-spec
tags:
- data ingestion
- status monitoring
- token estimation
- cache management
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: b02ede32b967.json
---

{
  "completion_tokens_estimate": 127,
  "created_at": 1786347518.8434668,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 50,
  "finished_at": null,
  "id": "b02ede32b967",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Saving OKF file 18/18",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge"
  },
  "processed": 68,
  "progress_percent": 100,
  "prompt_tokens_estimate": 740,
  "result": null,
  "started_at": 1786347518.844804,
  "status": "running",
  "total_documents": 68,
  "total_tokens_estimate": 867,
  "type": "ingest"
}