---
id: linux-ingestion-status-report-for-linux-man-pages-knowledge-base
type: concept
title: Ingestion Status Report for Linux Man Pages Knowledge Base
description: This document provides the status of an ongoing ingestion process for
  the 'linux-man-pages' data source into a Qdrant vector database. It includes performance
  metrics such as estimated tokens, processing progress at 92%, and active indexing
  counts. The job is currently in a running state under the '
category: linux
tags:
- Data Ingestion
- Vector Database
- Qdrant
- Man Pages
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Linux
trust_level: Medium
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