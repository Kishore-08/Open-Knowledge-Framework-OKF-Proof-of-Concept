---
id: architecture-ingestion-task-execution-metadata
type: concept
title: Ingestion Task Execution Metadata
description: This document contains the execution metadata and status metrics for
  an ingestion process. It details the task's start and end times, processed documents,
  parameter configurations, and final successful completion state.
category: architecture
tags:
- Ingestion pipeline
- Metadata
- Job monitoring
- JSON schema
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Architecture
trust_level: High
source_file: 7f78c40064ee.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786399660.946725,
  "current_source": "",
  "discovered": 5,
  "error": null,
  "failed": 0,
  "fetched": 3,
  "finished_at": 1786399662.0513413,
  "id": "7f78c40064ee",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": []
  },
  "processed": 2,
  "progress_percent": 100,
  "prompt_tokens_estimate": 0,
  "result": {
    "ok": true
  },
  "stage": "converting",
  "stage_message": "",
  "started_at": 1786399660.9475758,
  "status": "completed",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}