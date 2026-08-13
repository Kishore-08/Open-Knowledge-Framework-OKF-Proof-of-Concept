# Open Knowledge Framework Enterprise PoC

An enterprise knowledge-assistant proof of concept built with FastAPI,
Streamlit, Qdrant, and LlamaIndex. It crawls documentation or accepts uploaded
files, converts the content into structured Open Knowledge Framework (OKF)
Markdown, indexes it for hybrid retrieval, and returns grounded answers with
source citations.

## What it includes

- Documentation crawling from sources configured in `config/sources.yaml`
- Upload support for PDF, Markdown, text, and JSON files
- LLM-assisted metadata extraction and OKF Markdown generation
- Dense and sparse retrieval through Qdrant
- Grounded question answering with source citations
- Background ingestion jobs with progress reporting and cancellation
- A Streamlit interface for ingestion, browsing, search, and chat
- A Ragas-based evaluation suite with retrieval, answer, grounding, and
  citation metrics

## Architecture

```text
Configured websites / uploaded files
                 |
                 v
          Disposable cache
                 |
                 v
       Parse + extract metadata
                 |
                 v
       OKF Markdown knowledge base
                 |
                 v
          Qdrant hybrid index
                 |
                 v
       Retrieval + grounded answer
                 |
                 v
        Streamlit UI / FastAPI
```

The repository deliberately separates intermediate data from durable project
assets:

- `cache/` contains downloaded pages, uploads, and ingestion state. It is
  disposable and ignored by Git.
- `knowledge/` contains the generated OKF Markdown files used by search and
  question answering. It is the source of truth and should be versioned.
- `qdrant_storage/` contains the local vector index. It is generated data and
  is ignored by Git.

## Project layout

```text
okf-poc/
├── app/
│   ├── api/          # FastAPI application and route handlers
│   ├── converter/    # OKF Markdown conversion
│   ├── core/         # Settings, authentication, and model clients
│   ├── indexing/     # Qdrant indexing and vector state
│   ├── ingestion/    # Crawling, loading, metadata extraction, pipeline
│   ├── jobs/         # Background-job management
│   ├── okf/          # OKF schema, parser, formatter, and repository
│   ├── parser/       # Sitemap discovery and HTML cleaning
│   ├── query/        # Search and answer generation
│   ├── retrieval/    # Retrieval integrations
│   ├── storage/      # Persistent ingestion state
│   └── ui/           # Streamlit application
├── cache/            # Disposable source cache
├── config/           # Crawl sources and context supplements
├── docs/             # Architecture and implementation notes
├── evaluation/       # Dataset, scoring guide, evaluator, and results
├── knowledge/        # Versioned OKF knowledge files
├── requirements/     # API, UI, development, and evaluation dependencies
├── scripts/          # Conversion, migration, cleanup, and backfill tools
├── docker-compose.yml
├── Dockerfile.api
├── Dockerfile.ui
└── .env.example
```

## Quick start

### Prerequisites

- Docker with Docker Compose
- A Gemini Developer API key, or Google Cloud credentials for Vertex AI
- Python 3.11+ only if you intend to run the evaluation suite locally

### 1. Configure the environment

```bash
cp .env.example .env
```

The simplest local configuration uses the Gemini Developer API:

```env
AI_PROVIDER=gemini
GEMINI_API_KEY=your_api_key

LLM_MODEL=gemini-3.5-flash
LLM_FALLBACK_MODEL=gemini-3.5-flash-lite
EMBEDDING_MODEL=models/gemini-embedding-2
```

To use Vertex AI instead, keep `AI_PROVIDER=vertex` and configure the Vertex
project, location, models, and authentication values documented in
`.env.example`. Do not commit `.env` or credentials.

The container defaults in `.env.example` already point the UI to
`http://api:8000` and the API to `http://qdrant:6333`.

### 2. Start the stack

```bash
docker compose up --build -d
```

This starts:

| Service | URL |
| --- | --- |
| Streamlit UI | <http://localhost:8501> |
| FastAPI documentation | <http://localhost:8000/docs> |
| API health check | <http://localhost:8000/health> |
| Qdrant dashboard | <http://localhost:6333/dashboard> |

Check service logs with:

```bash
docker compose logs -f api ui qdrant
```

### 3. Ingest content

Open the Streamlit UI and either:

- select one or more configured documentation sources and start ingestion, or
- upload supported files and process them in upload-only mode.

Source definitions, URL filters, crawl limits, and enabled defaults live in
`config/sources.yaml`. Uploaded and crawled source files are written beneath
`cache/`; generated OKF documents are written beneath `knowledge/`.

### 4. Search and ask questions

Use the Knowledge Base page to browse or search concepts. Use the chat page to
ask a question; the response includes citations to the retrieved OKF sources.

## API overview

All application routes, except `/health`, are under `/api/v1`.

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/health` | API and dependency health |
| `GET` | `/api/v1/ingest/sources` | Available crawl sources |
| `GET` | `/api/v1/ingest/status` | Current ingestion status |
| `POST` | `/api/v1/ingest/` | Start an ingestion job |
| `POST` | `/api/v1/ingest/upload` | Upload files and start ingestion |
| `GET` | `/api/v1/jobs/` | List background jobs |
| `GET` | `/api/v1/jobs/{job_id}` | Inspect a job |
| `POST` | `/api/v1/jobs/{job_id}/cancel` | Cancel a job |
| `POST` | `/api/v1/query/` | Retrieve matching concepts |
| `POST` | `/api/v1/ask/` | Generate a grounded answer |
| `GET` | `/api/v1/knowledge/stats` | Knowledge-base statistics |
| `GET` | `/api/v1/knowledge/categories` | Available categories |
| `GET` | `/api/v1/knowledge/concepts` | Browse concepts |
| `GET` | `/api/v1/knowledge/search?q=...` | Search concepts |

The OpenAPI page at <http://localhost:8000/docs> contains complete request and
response schemas.

## Data migration

Older checkouts used `data/raw/` and `data/knowledge/`. Migrate that layout with:

```bash
python scripts/migrate_data_structure.py
```

The migration creates timestamped backups, moves raw data to `cache/`, moves
generated knowledge to `knowledge/`, and preserves state files. Review the
result before removing any backup.

## Evaluation

The evaluator uses a pinned Ragas 0.1.9-compatible environment. Keep it
separate from the application environment:

```bash
python3 -m venv .venv-eval
source .venv-eval/bin/activate
pip install -r requirements/eval.txt
```

With Qdrant populated and the required Gemini credentials available, run:

```bash
GEMINI_API_KEY=your_api_key \
GEMINI_EVAL_MODEL=gemini-3.5-flash \
python evaluation/evaluate_ragas.py
```

Results are written to `evaluation/results/` as timestamped detail CSV and
summary JSON files. The latest run is also copied to:

```text
evaluation/results/evaluation_details_FINAL.csv
evaluation/results/evaluation_summary_FINAL.json
```

See `evaluation/SCORING.md` for metric definitions, aggregation rules, and
guidance on interpreting the scores. Do not upgrade Ragas independently of the
pinned evaluation requirements; newer releases use a different metrics API.

## Local development

Install all application and development dependencies with:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
```

Run the backend and UI in separate terminals (Qdrant must also be reachable):

```bash
uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000
```

```bash
API_HOST=http://localhost:8000 streamlit run app/ui/app.py
```

For local execution, set `QDRANT_URL=http://localhost:6333` in `.env` instead of
the Docker service hostname.

## Operational notes

- `docker compose down` stops the stack without deleting the bind-mounted
  Qdrant data in `qdrant_storage/`.
- Removing `cache/` is safe, but the next ingestion must fetch or upload the
  source material again.
- Preserve and version `knowledge/`; regenerating it requires model calls.
- Changing embedding models or vector dimensions requires rebuilding the
  Qdrant collection.

## License

No license file is currently included. Treat this repository as an internal
proof of concept unless the project owner specifies other terms.
