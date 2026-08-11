---
id: api-spec-data-ingest-job-status-record
type: concept
title: Data Ingest Job Status Record
description: This document contains a JSON-formatted status report for a data ingestion
  job, detailing metrics such as token estimates, processed documents, and execution
  progress. It reflects the operational state of a knowledge caching and indexing
  pipeline.
category: api-spec
tags:
- data ingestion
- job status
- token estimation
- pipeline metrics
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
  "completion_tokens_estimate": 130,
  "created_at": 1786350759.7373877,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "fbce4e645b42",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Saving OKF file 2/2",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge"
  },
  "processed": 52,
  "progress_percent": 100,
  "prompt_tokens_estimate": 317,
  "result": null,
  "started_at": 1786350759.7411835,
  "status": "running",
  "total_documents": 52,
  "total_tokens_estimate": 447,
  "type": "ingest"
}