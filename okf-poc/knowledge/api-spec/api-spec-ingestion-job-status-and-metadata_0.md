---
id: api-spec-ingestion-job-status-and-metadata
type: concept
title: Ingestion Job Status and Metadata
description: This document contains execution metadata and status information for
  an active documentation crawling and ingestion job. It tracks key metrics such as
  processed documents, token estimates, and the current progress of importing Linux
  man pages into a knowledge base.
category: api-spec
tags:
- Data Ingestion
- Metadata
- Job Monitoring
- Knowledge Base
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 0962bae22cec.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786381039.2364135,
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "0962bae22cec",
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
  "progress_percent": 0,
  "prompt_tokens_estimate": 0,
  "result": null,
  "started_at": 1786381039.2387996,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}