---
id: api-spec-documentation-ingestion-pipeline-status-log
type: concept
title: Documentation Ingestion Pipeline Status Log
description: This document contains a JSON-formatted status log for a documentation
  ingestion pipeline processing Linux man pages. It tracks processing metrics such
  as completion status, error counts, progress percentage, and stage execution details.
category: api-spec
tags:
- documentation ingestion
- pipeline status
- cache processing
- Linux man pages
- system logs
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: bfd6658d5e69.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786488318.1957068,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "bfd6658d5e69",
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
  "started_at": 1786488318.196362,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}