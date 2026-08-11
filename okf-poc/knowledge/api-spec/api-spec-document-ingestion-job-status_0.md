---
id: api-spec-document-ingestion-job-status
type: concept
title: Document Ingestion Job Status
description: This document represents the JSON status output of an ongoing document
  ingestion and formatting process. It details the progress metrics, including fetched,
  processed, and total document counts for the knowledge base.
category: api-spec
tags:
- data ingestion
- job status
- knowledge base
- processing metrics
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 25cabf949028.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786369169.1582313,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "25cabf949028",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Formatting crawled HTML into OKF knowledge",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge"
  },
  "processed": 38,
  "progress_percent": 76,
  "prompt_tokens_estimate": 0,
  "result": null,
  "started_at": 1786369169.1599154,
  "status": "running",
  "total_documents": 50,
  "total_tokens_estimate": 0,
  "type": "ingest"
}