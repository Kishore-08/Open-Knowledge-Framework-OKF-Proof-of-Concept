---
id: api-spec-data-ingestion-and-knowledge-conversion-job-status
type: concept
title: Data Ingestion and Knowledge Conversion Job Status
description: This document contains a JSON-formatted status report for an active data
  ingestion and conversion process. It tracks the progress of converting cached raw
  Linux man-pages into official knowledge files, showing that 59 documents have been
  discovered and processed with a 69 percent completion rate.
category: api-spec
tags:
- Data Ingestion
- Knowledge Base
- Linux Man Pages
- Job Monitoring
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: d6ed8d808191.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786444835.7079487,
  "current_source": "",
  "discovered": 59,
  "error": null,
  "failed": 1,
  "fetched": 59,
  "finished_at": null,
  "id": "d6ed8d808191",
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
  "started_at": 1786444835.708815,
  "status": "running",
  "total_documents": 59,
  "total_tokens_estimate": 0,
  "type": "ingest"
}