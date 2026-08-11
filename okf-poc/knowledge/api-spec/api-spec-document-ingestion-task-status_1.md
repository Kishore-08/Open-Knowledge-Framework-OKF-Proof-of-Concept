---
id: api-spec-document-ingestion-task-status
type: concept
title: Document Ingestion Task Status
description: This JSON document provides the running status and metrics of a documentation
  ingestion process. It tracks metrics such as discovered, fetched, indexed, and processed
  document counts along with timestamps and configuration parameters.
category: api-spec
tags:
- documentation ingestion
- status monitoring
- data processing
- task metrics
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: fbce4e645b42.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786350759.7373877,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "fbce4e645b42",
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
  "started_at": 1786350759.7411835,
  "status": "running",
  "total_documents": 50,
  "total_tokens_estimate": 0,
  "type": "ingest"
}