---
id: api-spec-aws-services-guide-ingest-status
type: concept
title: AWS Services Guide Ingest Status
description: This document contains a JSON status payload for an ingestion process
  indexing documentation into a Qdrant vector database. It tracks progress metrics,
  such as processed and indexed document counts, along with current operational stages
  and parameters.
category: api-spec
tags:
- AWS
- Qdrant
- Indexing
- Document Management
- JSON
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 7d2fcff8ddf6.json
---

{
  "completion_tokens_estimate": 121,
  "created_at": 1786445226.8790944,
  "current_source": "AWS Services Guide for OKF PoC Architecture",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "7d2fcff8ddf6",
  "indexed": 25,
  "indexed_documents": 25,
  "message": "Indexed 25/1497 document(s)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 2,
  "progress_percent": 90,
  "prompt_tokens_estimate": 370,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786445226.8796117,
  "status": "running",
  "total_documents": 1497,
  "total_tokens_estimate": 491,
  "type": "ingest"
}