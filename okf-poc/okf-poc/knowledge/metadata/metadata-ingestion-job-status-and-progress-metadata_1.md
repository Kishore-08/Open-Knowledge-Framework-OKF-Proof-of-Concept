---
id: metadata-ingestion-job-status-and-progress-metadata
type: concept
title: Ingestion Job Status and Progress Metadata
description: This document contains the JSON metadata for an ongoing data ingestion
  and indexing job. It tracks progress, document counts, and processing stages as
  knowledge source documents like Linux man pages are indexed into a Qdrant vector
  database.
category: metadata
tags:
- Data Ingestion
- Search Indexing
- Qdrant
- Vector Database
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Metadata
trust_level: High
source_file: 21aa420c3c19.json
---

{
  "completion_tokens_estimate": 153,
  "created_at": 1786440705.2595544,
  "current_source": "Networking and security",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "21aa420c3c19",
  "indexed": 332,
  "indexed_documents": 332,
  "message": "Indexed 332/1119 document(s)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 2,
  "progress_percent": 92,
  "prompt_tokens_estimate": 415,
  "rate_limit_hits": 10,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786440705.2610922,
  "status": "running",
  "total_documents": 1119,
  "total_tokens_estimate": 568,
  "type": "ingest"
}