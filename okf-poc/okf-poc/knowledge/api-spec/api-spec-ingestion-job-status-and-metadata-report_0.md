---
id: api-spec-ingestion-job-status-and-metadata-report
type: concept
title: Ingestion Job Status and Metadata Report
description: This document contains the JSON metadata and execution status of a completed
  document ingestion job. It details execution timestamps, processed item counts,
  configuration parameters, and the final successful status of the conversion stage.
category: api-spec
tags:
- Ingestion
- Metadata
- Job Status
- JSON Schema
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
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