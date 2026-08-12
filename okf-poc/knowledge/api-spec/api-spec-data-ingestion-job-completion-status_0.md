---
id: api-spec-data-ingestion-job-completion-status
type: concept
title: Data Ingestion Job Completion Status
description: This JSON document provides the execution details and status of a completed
  data ingestion process. It records performance metrics such as token estimates,
  rate limit hits, document processing counts, and confirms that the knowledge has
  been successfully indexed in OKF format.
category: api-spec
tags:
- Data Ingestion
- Metadata
- Job Status
- OKF Format
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 1b0baa21ac59.json
---

{
  "completion_tokens_estimate": 121,
  "created_at": 1786514146.7111847,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 2,
  "fetched": 0,
  "finished_at": 1786514169.0053856,
  "id": "1b0baa21ac59",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Ingestion completed",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": []
  },
  "processed": 2,
  "progress_percent": 100,
  "prompt_tokens_estimate": 359,
  "rate_limit_hits": 4,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786514146.712674,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 480,
  "type": "ingest"
}