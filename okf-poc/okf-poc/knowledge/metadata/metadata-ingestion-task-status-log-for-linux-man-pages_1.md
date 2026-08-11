---
id: metadata-ingestion-task-status-log-for-linux-man-pages
type: concept
title: Ingestion Task Status Log for Linux Man Pages
description: This document contains a JSON-formatted status report for an active documentation
  ingestion task. It tracks the progress of converting cached raw Linux man pages
  into structured knowledge files, indicating the current stage, processed documents,
  and overall system metrics.
category: metadata
tags:
- Data Ingestion
- Linux Man Pages
- JSON Schema
- Knowledge Base Processing
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Metadata
trust_level: High
source_file: 9c28f045ef7e.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786439903.3613122,
  "current_source": "",
  "discovered": 59,
  "error": null,
  "failed": 1,
  "fetched": 59,
  "finished_at": null,
  "id": "9c28f045ef7e",
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
  "processed": 59,
  "progress_percent": 69,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Converting cached raw data into OKF knowledge files",
  "started_at": 1786439903.3619843,
  "status": "running",
  "total_documents": 59,
  "total_tokens_estimate": 0,
  "type": "ingest"
}