# OKF Platform Architecture

## Overview

The Open Knowledge Framework (OKF) platform is a RAG-based AI knowledge assistant that ingests documentation, converts it to a standardized format, and enables semantic search and question-answering with strict citation requirements.

## Core Principles

1. **Cache vs. Source of Truth Separation**
   - `cache/`: Disposable data that can be regenerated
   - `knowledge/`: Authoritative OKF Markdown files (expensive to regenerate)

2. **Schema-Driven Knowledge**
   - Every concept is a Markdown file with validated YAML frontmatter
   - Consistent metadata enables reliable search and citation

3. **Filesystem as Source of Truth**
   - The vector database (Qdrant) is an acceleration layer only
   - All knowledge is readable/editable Markdown files
   - No vendor lock-in: the knowledge base is portable

4. **LLM as Last Resort**
   - Crawling, parsing, indexing work without API keys
   - LLM is only used for metadata extraction and answer generation
   - Fallback to keyword search when embeddings unavailable

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                           │
│                      (Streamlit / API)                           │
└────────────────────────────┬────────────────────────────────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐   ┌─────────────────┐   ┌─────────────┐
│   Ingestion  │   │   Query Engine  │   │  Repository │
│   Pipeline   │   │                 │   │  (Browse)   │
└──────────────┘   └─────────────────┘   └─────────────┘
        │                    │                    │
        │                    │                    │
        ▼                    ▼                    ▼
┌──────────────┐   ┌─────────────────┐   ┌─────────────┐
│    cache/    │   │   Qdrant Index  │   │ knowledge/  │
│  (crawler    │   │  (dense/sparse) │   │ (OKF .md)   │
│   + raw)     │   │                 │   │             │
└──────────────┘   └─────────────────┘   └─────────────┘
```

## Data Flow

### 1. Ingestion Pipeline

```
Official Docs      Raw Files
     │                 │
     ▼                 ▼
┌─────────────────────────────┐
│     Web Crawler             │  (cache HTML, track state)
│  + Local File Loader        │
└─────────┬───────────────────┘
          │
          ▼
     cache/.state/  (sync tracking)
     cache/<source>/  (HTML files)
          │
          ▼
┌─────────────────────────────┐
│   HTML Cleaner & Parser     │  (extract content)
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│  Markdown Converter         │  (HTML → Markdown)
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│  Metadata Extractor (LLM)   │  (title, category, tags...)
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│  OKF Schema Validator       │  (validate frontmatter)
└─────────┬───────────────────┘
          │
          ▼
     knowledge/<category>/*.md
          │
          ▼
┌─────────────────────────────┐
│  Indexer (LlamaIndex)       │  (chunk + embed)
└─────────┬───────────────────┘
          │
          ▼
       Qdrant
```

### 2. Query Flow

```
User Question
     │
     ▼
┌─────────────────────────────┐
│   Query Engine              │
└─────────┬───────────────────┘
          │
      ┌───┴───┐
      ▼       ▼
  Semantic  Keyword
   Search    Search
   (Qdrant) (Filesystem)
      │       │
      └───┬───┘
          │
          ▼
┌─────────────────────────────┐
│  Context Builder            │  (retrieve concept texts)
└─────────┬───────────────────┘
          │
          ▼
┌─────────────────────────────┐
│  LLM (Answer Generation)    │  (grounded prompting)
└─────────┬───────────────────┘
          │
          ▼
   Answer + Citations
```

## Module Organization

### `app/core/`
- **config.py**: Central configuration (paths, models, API keys)
- **gemini_llm.py**: Gemini API wrapper with retry logic

### `app/storage/`
- **state_manager.py**: Processing state, crawler state, file tracking
- Handles incremental ingestion (only process changed files)

### `app/ingestion/`
- **crawler.py**: Web crawler with sitemap discovery and caching
- **loaders.py**: Local file loader (PDF, Markdown, TXT, JSON)
- **pipeline.py**: Orchestrates the ingestion process
- **metadata_extractor.py**: LLM-powered metadata extraction
- **status.py**: Shared ingestion status for UI progress

### `app/parser/`
- **sitemap.py**: Sitemap.xml parsing and URL discovery
- **cleaner.py**: HTML cleaning (remove nav, ads, scripts)

### `app/converter/`
- **markdown.py**: HTML → Markdown conversion, concept splitting

### `app/okf/`
- **schema.py**: Pydantic models for OKF frontmatter validation
- **parser.py**: Parse .md files into (metadata, content) tuples
- **formatter.py**: Format and save OKF Markdown files
- **repository.py**: Filesystem-based knowledge repository
  - Load/list/search concepts from `knowledge/`
  - Source of truth for the knowledge base

### `app/indexing/`
- **indexer.py**: Convert concepts to LlamaIndex Documents, index into Qdrant

### `app/retrieval/`
- **hybrid_search.py**: Qdrant integration (dense + sparse vectors)
- **query_engine.py**: LLM configuration and retrieval setup

### `app/query/`
- **search.py**: Unified search (keyword, semantic, auto)
- **engine.py**: AI answer generation with citation enforcement

### `app/api/`
- **main.py**: FastAPI application entry point
- **routers/ingest.py**: Ingestion API endpoints
- **routers/query.py**: Query/ask API endpoints
- **routers/concepts.py**: Concept browsing API

### `app/ui/`
- **app.py**: Streamlit frontend

## State Management

### Crawler State (`cache/.state/<source>.json`)

Tracks HTTP ETags, Last-Modified headers, and content hashes for each crawled URL:

```json
{
  "version": 1,
  "source": "kubernetes-docs",
  "pages": {
    "https://kubernetes.io/docs/concepts/": {
      "raw_file": "kubernetes-docs/abc123.html",
      "content_hash": "sha256...",
      "etag": "\"abc123\"",
      "last_modified": "Tue, 01 Jan 2024 00:00:00 GMT"
    }
  }
}
```

### Processing State (`cache/.state/processing.json`)

Tracks local raw files to enable incremental ingestion:

```json
{
  "files": {
    "docker-tutorial.pdf": {
      "content_hash": "sha256...",
      "okf_file": "docker-tutorial_0.md"
    }
  }
}
```

## OKF Concept Schema

Every knowledge concept is a Markdown file with validated YAML frontmatter:

```markdown
---
id: k8s-deployment
type: concept
title: Kubernetes Deployment
description: Declarative controller for managing Pods
category: kubernetes
tags: [deployment, workload, controller]
source:
  name: Kubernetes Documentation
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
created_at: 2026-08-05
updated_at: 2026-08-05
aliases: [Deployment, K8s Deployment]
related: [k8s-replicaset, k8s-pod]
---

# Kubernetes Deployment

A Deployment provides declarative updates for Pods and ReplicaSets...
```

### Required Fields
- `id`: Unique identifier (slug)
- `title`: Human-readable title
- `category`: Knowledge category
- `type`: Concept type (concept, tutorial, reference...)

### Optional Fields
- `description`: One-sentence summary
- `tags`: Searchable keywords
- `source`: Official documentation provenance
- `aliases`: Alternative names for lookup
- `related`: Links to related concepts
- `created_at`, `updated_at`: ISO date strings

## Configuration

### Environment Variables (`.env`)

```env
# Required
GEMINI_API_KEY=your_key_here

# Optional - Paths
CACHE_DIR=cache
KNOWLEDGE_DIR=knowledge
SOURCES_CONFIG=config/sources.yaml

# Optional - Qdrant
QDRANT_URL=http://localhost:6333
QDRANT_CONCEPTS_COLLECTION=okf_concepts

# Optional - Models
LLM_MODEL=gemini-flash-lite-latest
EMBEDDING_MODEL=models/gemini-embedding-001
TEMPERATURE=0.1

# Optional - RAG
TOP_K=5
CHUNK_SIZE=512
CHUNK_OVERLAP=50
```

### Source Configuration (`config/sources.yaml`)

```yaml
crawler:
  delay: 0.5  # seconds between requests
  timeout: 30
  max_urls_per_source: 500
  user_agent: "OKF-Crawler/1.0"

sources:
  - name: kubernetes-docs
    base_url: https://kubernetes.io
    sitemap_url: https://kubernetes.io/sitemap.xml
    url_filter: "^https://kubernetes.io/docs/"
    enabled: true

  - name: docker-docs
    base_url: https://docs.docker.com
    enabled: true
```

## Design Decisions

### Why Filesystem as Source of Truth?

1. **Portability**: Knowledge base is just a folder of Markdown files
2. **Reviewability**: Diffs show exactly what changed
3. **Editability**: Concepts can be manually refined
4. **Resilience**: No database corruption can destroy the knowledge base
5. **Simplicity**: No complex database schema to maintain

### Why Separate Cache and Knowledge?

1. **Cost**: Metadata extraction requires LLM API calls (expensive)
2. **Versioning**: Knowledge should be version-controlled, cache should not
3. **Clarity**: Disposable data vs. valuable assets clearly separated
4. **Rebuilds**: Can re-crawl without losing curated knowledge

### Why Incremental State Tracking?

1. **Efficiency**: Don't re-process unchanged documents
2. **Speed**: Only extract metadata for new/modified files
3. **Cost**: Avoid unnecessary LLM API calls
4. **UX**: Faster ingestion means better user experience

## Error Handling

### Graceful Degradation

- **No API key**: Ingestion stores raw documents, skips metadata extraction
- **Qdrant down**: Keyword search still works via filesystem
- **LLM timeout**: Retry with exponential backoff, then skip document

### Validation

- **OKF Schema**: Pydantic validates frontmatter before saving
- **Unusable Concepts**: Documents with placeholder titles are skipped
- **File Hash**: Prevents duplicate processing of identical files

## Performance Considerations

### Indexing

- **Batch Size**: 10 documents per Qdrant batch (avoid timeouts)
- **Parallel Metadata**: ThreadPoolExecutor for LLM calls (3 workers)
- **Caching**: Repository caches loaded concepts (invalidate on mtime change)

### Search

- **Hybrid**: Combines dense (semantic) and sparse (keyword) retrieval
- **Fallback**: Keyword search always available, even without embeddings
- **Top-K**: Default 5 results to balance relevance and context size

### Crawler

- **Rate Limiting**: Configurable delay between requests
- **Conditional Requests**: Uses ETags and Last-Modified headers
- **Incremental**: Only downloads changed pages

## Future Enhancements

1. **Service Layer**: Extract services for crawler, converter, indexer
2. **Validation Layer**: Comprehensive input/output validation
3. **Async Pipeline**: Full async/await for ingestion
4. **Graph Relations**: Index `related` field for concept graph
5. **Versioning**: Track concept history and changes over time
6. **Multi-tenancy**: Support multiple knowledge bases
7. **Plugin System**: Pluggable converters for new document types
