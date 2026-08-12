---
id: api-spec-ingest-job-status-and-progress-metadata
type: concept
title: Ingest Job Status and Progress Metadata
description: This document contains JSON metadata for an active ingestion job, tracking
  progress metrics such as processed documents, errors, and token estimates. It also
  records an API rate limit error event and indicates a pending retry attempt for
  the 'apache-httpd' knowledge source.
category: api-spec
tags:
- Ingestion Pipeline
- Job Status
- Rate Limiting
- Metadata
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 718a083c9c90.json
---

{
  "completion_tokens_estimate": 133,
  "created_at": 1786455387.6625743,
  "current_source": "Ingest Job Status and Progress Metadata",
  "discovered": 0,
  "error": null,
  "failed": 7,
  "fetched": 0,
  "finished_at": null,
  "id": "718a083c9c90",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "\u26a0\ufe0f Embedding rate limit (429) hit for 'api-spec-ingest-job-status-and-progress-metadata', retrying in 6s (attempt 2/3)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "apache-httpd"
    ]
  },
  "processed": 2,
  "progress_percent": 90,
  "prompt_tokens_estimate": 399,
  "rate_limit_hits": 16,
  "result": null,
  "stage": "indexing",
  "stage_message": "Rate limited on 'Ingest Job Status and Progress Metadata' \u2014 retrying in 6s",
  "started_at": 1786455387.6650522,
  "status": "running",
  "total_documents": 1494,
  "total_tokens_estimate": 532,
  "type": "ingest"
}