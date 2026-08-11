---
id: api-spec-ingest-job-status-and-progress-metadata
type: concept
title: Ingest Job Status and Progress Metadata
description: This document contains a JSON-formatted status report for an active documentation
  ingestion and processing job. It details execution timestamps, processing metrics
  such as documents crawled and fetched, and the configuration parameters used during
  execution.
category: api-spec
tags:
- Data Ingestion
- Job Monitoring
- JSON Schema
- Web Crawling
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: b02ede32b967.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786347518.8434668,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 50,
  "finished_at": null,
  "id": "b02ede32b967",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge"
  },
  "processed": 50,
  "progress_percent": 100,
  "prompt_tokens_estimate": 0,
  "result": null,
  "started_at": 1786347518.844804,
  "status": "running",
  "total_documents": 50,
  "total_tokens_estimate": 0,
  "type": "ingest"
}