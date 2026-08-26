# OKF PoC: Context, Deliverable, and End-to-End Runtime Flow

## 1. Project context and deliverable — very short

This project is a proof-of-concept enterprise knowledge assistant. It takes official documentation websites or user-uploaded files, converts them into validated Open Knowledge Framework (OKF) Markdown, stores that Markdown as the durable knowledge base, indexes it in Qdrant, and answers user questions with citations.

The deliverable is a working three-service application:

- a Streamlit frontend for ingestion, browsing, and chat;
- a FastAPI backend for HTTP APIs, background jobs, ingestion, search, and answers;
- Qdrant as a generated dense-vector search index.

The most important storage rule is:

> `knowledge/` is the source of truth. `cache/` is disposable input/state. Qdrant is a rebuildable search index.

---

## 2. Runtime architecture

```text
Browser
  |
  | localhost:8501
  v
Streamlit UI (app/ui/app.py)
  |
  | HTTP through API_HOST
  v
FastAPI (app/api/main.py, port 8000)
  |                         |                         |
  v                         v                         v
Job manager             knowledge/               Query engine
  |                    filesystem repo             |      |
  v                                                |      v
Ingestion pipeline                                 |   Gemini/Vertex LLM
  |                                                v
  +--> websites/uploads --> cache/              Qdrant
  +--> OKF conversion  --> knowledge/             ^
  +--> embeddings      ----------------------------+
```

Docker wiring is in `docker-compose.yml`:

- `ui` exposes port `8501` and calls `API_HOST`.
- `api` exposes port `8000`, mounts `app/`, `cache/`, `knowledge/`, and `config/`.
- `qdrant` exposes ports `6333` and `6334`, persisting data in `qdrant_storage/`.
- `vertex-token` periodically creates short-lived credentials when Vertex service-account impersonation is used.

`app/core/config.py::Settings` reads runtime environment variables and `.env`. Important values include `AI_PROVIDER`, model names, Qdrant URL and collection, directory paths, chunk settings, `TOP_K`, and citation score thresholds.

---

## 3. Application startup flow

### 3.1 Backend startup

1. Uvicorn imports `app/api/main.py::app`.
2. `FastAPI(...)` creates the API application.
3. `CORSMiddleware` allows the Streamlit/browser client to call the API. The PoC currently allows all origins, methods, and headers.
4. `app.include_router(...)` registers ingestion, query, concept, ask, and job routers under `/api/v1`.
5. Importing `app/api/routers/ingest.py` runs `job_manager.register_handler("ingest", _run_ingest_job)`. This connects the job type named `ingest` to the ingestion pipeline.
6. Importing `app/jobs/manager.py` creates the singleton `job_manager`. Its constructor creates `cache/.jobs/` and reloads persisted job JSON files.

### 3.2 Frontend startup and every Streamlit rerun

Streamlit executes `app/ui/app.py` top to bottom on initial load and after widget interactions.

1. The repository root is inserted at the front of `sys.path` so the script named `app.py` does not shadow the Python package named `app`.
2. `st.set_page_config(...)` configures the page.
3. `load_theme_css()` reads `base.css` and either `dark.css` or `light.css`.
4. missing session-state keys are initialized: theme, chat messages, ingestion job ID, running flag, overlay state, and upload messages.
5. `check_api_health()` calls `GET /health`.
6. The sidebar fetches configured sources with `get_available_sources()`.
7. The selected page is rendered: Chat Assistant or Knowledge Base.

---

## 4. System-health flow

### User-visible trigger

Opening or rerunning the Streamlit page automatically checks system health.

### Exact call path

```text
app/ui/app.py::check_api_health
  -> GET /health
  -> app/api/main.py::health_check
       -> app/retrieval/hybrid_search.py::get_qdrant_client
       -> Qdrant get_collections()
       -> app/core/config.py::Settings.has_gemini_api_key
  <- health JSON
  -> sidebar status pills
```

### Stage behavior

1. `check_api_health()` uses a two-second timeout and returns `None` on a connection error or non-200 response.
2. `health_check()` constructs separate `qdrant` and `llm` checks.
3. `get_qdrant_client()` connects using `QDRANT_URL`; `get_collections()` verifies Qdrant availability.
4. `Settings.has_gemini_api_key()` only checks Gemini/Google API-key presence. Consequently, the UI's LLM health pill can report “Key missing” when `AI_PROVIDER=vertex` even though Vertex authentication may work.
5. The endpoint deliberately returns HTTP 200 with `status: degraded` when Qdrant is unavailable. This distinguishes an online API with a broken dependency from an offline API.
6. In the UI, `is_healthy` means the API returned JSON, not that every dependency is healthy. Chat is therefore enabled for a degraded backend; retrieval can still fall back to keyword search.

---

## 5. Source selection flow

### When the sidebar is rendered

```text
app/ui/app.py::get_available_sources
  -> GET /api/v1/ingest/sources
  -> app/api/routers/ingest.py::list_available_sources
  -> app/ingestion/crawler.py::load_sources
  -> config/sources.yaml
```

`list_available_sources()` returns each source's name, base URL, category, and enabled flag. The Streamlit multiselect uses enabled sources as defaults.

The configuration controls discovery:

- `sitemap_url` selects sitemap discovery;
- `index_url` selects link discovery from an HTML index;
- `seed_urls` can supply explicit pages;
- `url_filter` includes matching URLs;
- `exclude_filters` remove unwanted URLs;
- `max_urls_per_source`, delay, timeout, and user-agent control crawler behavior.

Selecting items in the multiselect only changes Streamlit widget state. The YAML file is not modified until the user starts a non-upload ingestion.

---

## 6. Configured-website ingestion: click to Qdrant

This is the path taken when no upload is present and the user clicks **Trigger Ingestion**.

### 6.1 Frontend click

1. The button in `app/ui/app.py` is enabled only when the API is reachable and `st.session_state.ingestion_running` is false.
2. The click calls `trigger_ingestion(selected_sources)`.
3. `trigger_ingestion()` posts JSON such as `{"sources": ["kubernetes"]}` to `POST /api/v1/ingest/`.
4. On a successful response it stores the returned job ID, sets the running flag, opens the progress dialog, and calls `st.rerun()`.

### 6.2 API request validation and job submission

The request reaches `app/api/routers/ingest.py::ingest_documents` and is validated by `IngestRequest`.

1. `job_manager.has_active_jobs()` checks for queued, running, or cancelling work.
2. If any active job exists, this endpoint returns `status="queued"` but returns the existing active job ID and does **not** submit a second job. Despite the wording, this branch does not create a queued request.
3. Otherwise `crawler.update_sources_config(request.sources)` rewrites `enabled` flags in `config/sources.yaml` so the UI defaults reflect the last selection.
4. `job_manager.submit("ingest", params=...)` creates a `Job`, assigns a 12-character ID, persists it to `cache/.jobs/<id>.json`, puts it in the in-memory queue, and starts a daemon worker thread.
5. The API immediately returns `status="started"`; ingestion continues after the HTTP response.

### 6.3 Background-job execution

The path is:

```text
JobManager._worker_loop
  -> JobManager._execute
  -> ingest router::_run_ingest_job
  -> ingestion.pipeline::run_ingestion_pipeline
```

`JobManager._execute()` changes the job from `queued` to `running`, sets timestamps, makes it the active job, and invokes the registered handler. `_run_ingest_job()` passes directories, source names, upload file restrictions, and the cancellation event to the pipeline.

Every `app/ingestion/status.py::update_status()` call updates both:

- the legacy in-memory status used by `/ingest/status`; and
- the active `Job`, which is persisted and returned by `/jobs/{job_id}`.

`compute_stage_progress()` maps stages into ranges: discovery begins near 6%, downloading advances toward 48%, conversion/formatting advances toward 90%, indexing advances toward 99%, and completion is 100%.

### 6.4 Pipeline initialization

`app/ingestion/pipeline.py::run_ingestion_pipeline` resolves default paths, records whether this is upload-only, initializes counters, and publishes stage `starting`.

It then calls:

```text
asyncio.run(crawler.crawl_configured_sources(cache_dir, source_names))
```

### 6.5 Source discovery

`app/ingestion/crawler.py::crawl_configured_sources` loads `config/sources.yaml`, selects requested sources, constructs `DocsCrawler`, and processes sources sequentially.

For each source:

1. it publishes stage `discovering`;
2. calls `DocsCrawler.crawl()`;
3. `crawl()` calls `DocsCrawler.discover()` unless explicit URLs were supplied;
4. `discover()` chooses one discovery strategy:
   - explicit `seed_urls`;
   - `parser/sitemap.py::discover_urls_from_html_index` for `index_url`;
   - configured sitemap, sitemaps from `robots.txt`, or `<base>/sitemap.xml` through `discover_urls_from_sitemap`;
5. URL inclusion/exclusion filters and maximum URL count are applied.

`parser/sitemap.py` also handles sitemap indexes recursively and normalizes relative links discovered from HTML indexes.

### 6.6 Downloading and incremental crawl state

`DocsCrawler.crawl_source()` synchronizes discovered URLs to `cache/<source>/<URL hash>.html`.

For every URL:

1. `StateManager.load_crawler_state(source_name)` supplies prior ETag, Last-Modified, content hash, and cached filename data from `cache/.state/<source>.json`.
2. `_fetch_with_metadata()` performs a rate-limited HTTP request. Conditional `If-None-Match` and `If-Modified-Since` headers are sent when available.
3. HTTP 304 marks the page unchanged and avoids rewriting it.
4. HTTP 200 content is SHA-256 hashed.
5. New or changed bytes are written to a deterministic `raw_path()`, and an entry is added to `changed_pages`.
6. Identical content is counted as unchanged even if the server did not return 304.
7. A failed URL increments `failed`; previous state is retained to avoid treating a temporary network failure as deletion.
8. URLs formerly in state but absent from the new discovery set are treated as deleted, and their cached HTML is removed.
9. `StateManager.save_crawler_state()` atomically replaces the source state JSON.

Only changed pages continue to conversion. This is the first major quota-saving boundary.

### 6.7 Handling source deletions

Back in `run_ingestion_pipeline()`, deleted source URLs are passed to:

- `okf/repository.py::delete_concepts_by_source_urls`, which deletes matching Markdown concepts; and
- `retrieval/hybrid_search.py::delete_points_by_field`, which deletes Qdrant points with matching `source_url` payloads.

This keeps removed official pages out of both authoritative storage and retrieval.

### 6.8 Crawled HTML cleanup and conversion

`pipeline._process_crawled_html()` processes each changed page and checks cancellation between pages.

For each page:

1. the raw HTML is read from cache;
2. `parser/cleaner.py::clean_html()` removes scripts, navigation, cookie/UI clutter, hidden elements, and other non-content HTML, extracts the main article-like region, and normalizes links against the source URL;
3. `converter/markdown.py::html_to_markdown()` converts cleaned HTML to Markdown while retaining structures such as headings, lists, tables, and code;
4. `split_into_concepts()` splits at H2/H3 headings;
5. `_split_headings()` merges undersized sections and truncates sections exceeding configured maximum characters;
6. `_concept_id()` creates a stable ID from category, heading title, and an eight-character source-URL hash;
7. `generate_concept_file()` builds OKF YAML frontmatter with ID, title, description, category, tags, source name/URL, and dates;
8. `okf/formatter.py::format_okf_string()` serializes frontmatter plus body;
9. old concepts for the page URL are deleted before replacement;
10. `write_concept_file()` writes each concept to `knowledge/<category>/<concept-id>.md`.

This crawled-page path is deterministic and does not use the metadata-extraction LLM.

### 6.9 Local cached-file behavior during a source crawl

After HTML conversion the pipeline configures models and examines local files. When `source_names` is non-empty, it deliberately sets `changed_local_files=[]`. Therefore manually uploaded/cache-root PDF, Markdown, text, or JSON files are not accidentally mixed into an explicitly selected website crawl.

### 6.10 Loading and validating changed OKF files

The pipeline combines paths produced from crawled pages and local documents, then calls `okf/repository.py::load_concepts_from_paths()`.

For each file:

1. `okf/parser.py::parse_okf_file()` splits YAML frontmatter from Markdown body;
2. `OKFConcept.model_validate()` in `okf/schema.py` validates IDs, fields, lists, dates, and source provenance;
3. `_is_usable_concept()` rejects empty, placeholder, or invalid titles/categories;
4. valid records become `OKFConceptFile` objects.

`indexing/indexer.py::concepts_to_documents()` turns these into LlamaIndex `Document` objects. `OKFConcept.metadata_payload()` flattens the frontmatter into Qdrant payload fields, and `source_file` is added for idempotent replacement.

### 6.11 Deciding whether embeddings are needed

`indexing/vector_state.py::filter_documents_for_indexing()` compares three things:

- the candidate document content hash;
- `cache/.state/vector_index.json`, which records the last successfully indexed hash;
- Qdrant's actual set of `source_file` payloads from `get_indexed_source_files()`.

A document needs indexing if it is absent from Qdrant or its successful hash is stale. If local vector state exists but Qdrant is empty, the state is cleared and documents are re-indexed. Unchanged documents skip embedding calls.

### 6.12 Chunking, embedding, and Qdrant insertion

`retrieval/hybrid_search.py::index_documents()` performs the write path.

1. Previous Qdrant points for candidate `source_file` values are deleted because LlamaIndex chunks receive new UUIDs on each run.
2. `get_qdrant_vector_store()` creates a Qdrant-backed vector store for the configured collection.
3. `SentenceSplitter` uses `CHUNK_SIZE` and `CHUNK_OVERLAP`.
4. An initially empty `VectorStoreIndex` is connected to the Qdrant storage context.
5. Each document is inserted separately. LlamaIndex chunks it, the configured embedding provider produces dense vectors, and Qdrant stores vectors, text, and metadata.
6. `retry_with_backoff()` retries rate-limit/quota failures. Retry details are published to the progress dashboard.
7. A document that exhausts retries is recorded as failed, but later documents continue.
8. Cancellation is checked between documents.
9. `mark_documents_indexed()` atomically records successful content hashes in `vector_index.json`.

Despite names and UI copy mentioning hybrid Qdrant search, `get_qdrant_vector_store()` sets `enable_hybrid=False`. Qdrant stores dense vectors only because the pinned sparse-vector libraries are incompatible. Hybrid behavior occurs later by merging semantic Qdrant results with filesystem keyword results.

### 6.13 Completion

The pipeline publishes `completed`, final counters, and returns indexed/skipped/failed counts. `JobManager._finish()` stores this result, sets `finished_at`, removes the job from the queue, clears the active-job pointer, persists final JSON, and makes progress 100%.

---

## 7. Uploaded-file ingestion: click to Qdrant

This flow starts when one or more files are present and the user clicks **Process & Index Documents**.

### 7.1 Frontend upload request

`app/ui/app.py::upload_files()`:

1. resets each Streamlit `UploadedFile` to offset zero;
2. builds a multipart list under repeated field name `files`;
3. posts to `/api/v1/ingest/upload` with a 30-second request timeout;
4. ignores selected crawl sources by sending an empty `sources` form value.

### 7.2 Backend validation and cache write

`app/api/routers/ingest.py::upload_documents()`:

1. rejects an empty request;
2. returns HTTP 409 if another job is active;
3. accepts only `.pdf`, `.md`, `.txt`, and `.json` through `_validate_file_extension()`;
4. `_sanitize_filename()` removes path components, replaces unsafe characters, prevents hidden filenames, and limits filename length;
5. reads the entire uploaded file into memory;
6. rejects content over 50 MiB;
7. writes accepted bytes to the root of `cache/`;
8. submits an ingestion job with `sources=[]` and `only_files=[accepted filenames]`.

Partial success is allowed: valid files are processed and per-file errors are returned for invalid files.

Code caveat: if every upload is rejected, the response branch refers to `job.id` before `job` has been created. That branch can raise `UnboundLocalError` instead of returning the intended structured failure response.

### 7.3 Upload-only pipeline mode

`run_ingestion_pipeline()` sets `upload_only=True` when `only_files` is non-empty. It creates a zeroed crawl result and never calls the crawler. It then constructs exact paths only for the just-uploaded names; it does not scan unrelated cached files.

`StateManager.load_processing_state()` loads `cache/.state/processing.json`. `_file_hash()` compares each upload with its prior processed hash. Re-uploading identical bytes therefore avoids repeating metadata and embedding work.

### 7.4 File parsing

For every changed upload the pipeline creates `SimpleDirectoryReader(input_files=[file_path])` and calls `load_data()`.

LlamaIndex chooses a reader based on extension:

- PDF text is extracted by the installed PDF reader;
- Markdown and text are read as text;
- JSON is loaded into textual document content.

A file can yield one or more `Document` objects. Parse failures are logged and do not abort other files.

`app/ingestion/loaders.py::load_raw_documents()` is a general cache loader, but the current master pipeline uses `SimpleDirectoryReader` directly for its per-file incremental path.

### 7.5 Metadata extraction

Local/upload documents take a different conversion route from crawled HTML. Up to three documents are processed concurrently through the nested `pipeline._extract()` function.

`_extract()` calls `ingestion/metadata_extractor.py::generate_okf_metadata()`:

1. empty documents return `None`;
2. only the first 3,000 characters are sent to the model;
3. `_llm_complete()` selects `vertex_llm.complete()` or `gemini_llm.complete()` based on `AI_PROVIDER`;
4. the prompt requests one JSON object containing title, summary, document type, topics, and trust level;
5. `_parse_json_response()` tolerates Markdown fences or surrounding prose;
6. `OKFMetadata` validates the response;
7. estimated token counts are accumulated into the live job;
8. rate-limit failures retry briefly;
9. missing Gemini credentials, malformed model output, exhausted retries, or other model failure invokes `_heuristic_fallback()`;
10. the heuristic derives a title from a heading/first line/JSON title/filename, guesses a category from keywords, extracts simple topic words, and returns `None` for unusable content.

### 7.6 Building and writing uploaded-file OKF

For each successful metadata result:

1. `pipeline._build_okf_frontmatter()` maps extracted fields to the project's full OKF schema, creates a stable slug-like ID, attaches file provenance, dates, tags, and source information;
2. `okf/formatter.py::format_and_save_okf()` writes YAML frontmatter plus the complete parsed document text;
3. output goes to `knowledge/<derived-category>/<id>_<document-index>.md`;
4. `StateManager.update_file_state()` records source content hash and generated OKF filename;
5. `save_processing_state()` atomically persists the result.

The resulting changed OKF files then use exactly the validation, vector-state, chunking, embedding, Qdrant, and completion stages described in sections 6.10–6.13.

---

## 8. Live progress and cancellation flow

### 8.1 Progress dialog

After job creation, `app/ui/app.py::ingestion_overlay()` gets the exact job through `get_job_status(job_id)` and calls `ui/components/dashboard.py::render_live_dashboard()`.

The dashboard:

- embeds server-fetched initial status into its HTML;
- uses `/api/v1/jobs/<job-id>` when a job ID is available;
- runs browser-side polling as an enhancement;
- maps raw stages to pipeline labels, counters, progress, rate-limit notices, and terminal state.

The exact-job endpoint is `api/routers/jobs.py::get_job()`, which calls `job_manager.get_job()` and serializes `Job.to_dict()`.

The sidebar also calls the legacy `get_ingestion_status()` endpoint. `ingestion/status.py::get_status()` prefers the current active job and otherwise returns its legacy in-memory snapshot.

Closing the dialog calls `_dismiss_ingestion_overlay()` and only hides the UI. It does not stop backend work.

### 8.2 Stop button

```text
sidebar Stop button
  -> POST /api/v1/jobs/{job_id}/cancel
  -> api/routers/jobs.py::cancel_job
  -> JobManager.cancel
```

- A queued job is removed and immediately marked cancelled.
- A running job becomes `cancelling`; its `threading.Event` is set.
- `pipeline._check_cancelled()` checks at major stage boundaries and crawled-page loops.
- `index_documents()` checks between documents.
- Detection raises `JobCancelledError`.
- `JobManager._execute()` catches it and finishes the job as cancelled.

Cancellation is cooperative. It cannot interrupt a network/model call already executing; it takes effect at the next check.

---

## 9. Knowledge Base page flows

Clicking **Knowledge Base** changes only `st.session_state.page`. Streamlit reruns and calls `render_knowledge_base()`.

### 9.1 Statistics

```text
GET /api/v1/knowledge/stats
  -> api/routers/concepts.py::stats
  -> okf/repository.py::knowledge_stats
  -> repository.load_all_concepts
```

`load_all_concepts()` scans Markdown recursively, skips `_quarantine`, parses frontmatter, validates `OKFConcept`, rejects unusable concepts, and caches loaded objects until file count/latest modification time changes. `knowledge_stats()` counts concepts by category, unique tags, sources, and files.

### 9.2 Search box

Typing a non-empty value triggers:

```text
GET /api/v1/knowledge/search?q=<text>
  -> concepts.py::search
  -> repository.py::search_concepts
```

This page uses filesystem keyword search only—not Qdrant.

`search_concepts()`:

1. tokenizes and removes stop words;
2. applies optional category/tag filters;
3. searches complete terms across weighted fields such as title, aliases, tags, description, and body;
4. boosts overview/introduction concepts for definition queries;
5. normalizes scores into a semantic-like range;
6. creates a snippet around the first match;
7. sorts descending.

The UI displays description, tags, snippet, and official source link in expanders.

### 9.3 Category selection and concept listing

1. `GET /knowledge/categories` calls `repository.list_categories()`.
2. Changing the select box reruns Streamlit.
3. `GET /knowledge/concepts?category=...` calls `repository.list_concepts()`.
4. The backend returns lightweight metadata rather than full Markdown bodies.

### 9.4 View full concept

Clicking **View full concept** calls `GET /knowledge/concepts/{concept_id}`.

`repository.get_concept_dict()` uses `get_concept()` to match an exact ID or alias, then returns metadata and body. The frontend renders the Markdown body below that concept's metadata.

---

## 10. Chat question: click/Enter to grounded answer

### 10.1 Frontend

When the user submits `st.chat_input`:

1. the prompt is appended to `st.session_state.messages`;
2. it is immediately rendered as a user message;
3. the UI posts `{"query": prompt}` to `/api/v1/query/` with a 120-second timeout;
4. a successful answer is streamed locally word by word by `simulated_typing_effect()`—the backend response itself is not streamed;
5. answer, citations, and retrieval mode are stored in session state;
6. Streamlit reruns and renders history and citation expanders.

### 10.2 API boundary

`api/routers/query.py::query_knowledge_base()` validates `QueryRequest` and calls:

```python
await asyncio.to_thread(generate_answer, request.query)
```

The worker thread prevents retrieval/model work from blocking FastAPI's event loop. The endpoint converts internal sources into the legacy `Citation` response shape: title, snippet/content, and score.

The richer `/api/v1/ask/` endpoint calls the same engine but accepts optional category and `top_k`, and returns IDs, categories, descriptions, source URLs, scores, and snippets.

### 10.3 Pre-retrieval special paths

`query/engine.py::generate_answer()` caps citations at five.

Before general retrieval:

1. `_taxonomy_clarification()` catches a specifically ambiguous “types of Python packages” question and returns a clarification without search or LLM use.
2. `_matching_supplements()` reads `config/context_supplements.yaml`; if a configured match term occurs in the query, its explicitly sourced content becomes high-confidence `curated` retrieval and bypasses embedding/Qdrant.

### 10.4 Auto/hybrid retrieval

Ordinary questions call `query/search.py::search(mode="auto")`.

Two operations run concurrently:

```text
Filesystem branch                         Semantic branch
repository.search_concepts(query)         _semantic_search(query)
  -> parse/search knowledge/                 -> _get_cached_semantic_index
                                              -> configure_llm_settings
                                              -> get_qdrant_vector_store
                                              -> retriever.retrieve(query)
                                              -> query embedding + Qdrant similarity
```

The semantic index object is cached, but each retrieval still queries Qdrant and therefore sees newly inserted vectors.

`_rank_and_filter()` then:

1. removes records resembling accidentally indexed internal job-status JSON;
2. deduplicates by concept ID/source/title, keeping the higher score;
3. sorts by score;
4. requires the configured absolute minimum score and a score relative to the best result;
5. returns no more than five.

The reported mode is:

- `hybrid` when both semantic and keyword branches returned results;
- `semantic` when only Qdrant returned results;
- `keyword` when semantic retrieval failed or returned nothing.

Semantic failure is intentionally caught inside `_semantic_search()`, so missing credentials, unavailable Qdrant, or embedding errors degrade to keyword results instead of failing the HTTP request.

### 10.5 Hydrating full authoritative context

Retrieval results contain short snippets or vector chunks. `generate_answer()` calls `repository.get_concept_dict()` for every result ID and replaces its snippet with up to `CONCEPT_MAX_CHARS` from the complete authoritative Markdown concept.

This is important: Qdrant chooses relevant concepts, but the final model context is hydrated from `knowledge/`, preventing an arbitrary vector chunk from being treated as the complete source.

If no sources remain, the engine returns a deterministic “could not find matching concepts” answer without calling an LLM.

### 10.6 Prompt construction and model call

For every result, the engine creates a numbered context section containing title, source URL, and hydrated content. `_call_llm()` chooses:

- `core/vertex_llm.py::complete()` when `AI_PROVIDER=vertex`; or
- `core/gemini_llm.py::complete()` otherwise.

The prompt tells the model to use only supplied context, cite source titles inline, refuse unsupported answers, fill all requested answer parts, stay concise, and avoid inventing taxonomies from examples.

Provider `complete()` functions create the appropriate Google GenAI client, apply configured model/temperature/output limits/timeouts, and use retry helpers for transient quota behavior.

### 10.7 LLM failure fallback

If generation fails after retrieval, `generate_answer()` does not throw away successful search.

1. `_format_search_fallback()` selects the strongest result.
2. It strips Markdown links/headings and chooses the first substantive paragraph.
3. It returns an extractive answer noting AI generation is unavailable.
4. Sources are reduced to the one result actually used.

The API only returns HTTP 500 for exceptions that escape this broader graceful-degradation path.

---

## 11. Data objects and ownership

### Raw/cache layer

- `cache/<source>/<hash>.html`: downloaded official pages.
- `cache/<uploaded-name>`: raw uploaded files.
- `cache/.state/<source>.json`: URL synchronization state.
- `cache/.state/processing.json`: uploaded/local-file conversion hashes.
- `cache/.state/vector_index.json`: successfully embedded concept hashes.
- `cache/.jobs/<job-id>.json`: persisted job history and progress.

All cache state is rebuildable, though deleting it loses incremental knowledge about prior work.

### Durable OKF layer

`knowledge/<category>/<concept>.md` contains validated YAML frontmatter and Markdown. It is used by browsing, keyword search, citation hydration, and Qdrant rebuilds. It should be versioned and preserved.

### Vector layer

Qdrant collection `okf_concepts` contains dense vectors and flattened OKF metadata. It accelerates semantic retrieval but is not authoritative.

### In-memory layer

- Streamlit session state owns current page, chat history, theme, and tracked job ID.
- the FastAPI process owns the job worker thread, active queue, repository cache, semantic index wrapper cache, and legacy status snapshot.
- restarting the API interrupts active work; persisted job history remains, but running jobs are not automatically resumed.

---

## 12. Error and resilience behavior

- A frontend API connection error is displayed without crashing Streamlit.
- Crawl failures are counted per URL; other URLs continue.
- Conditional HTTP caching and hashes prevent needless conversion.
- Bad/empty uploaded documents can be skipped independently.
- Metadata extraction falls back to heuristics.
- Invalid OKF files are skipped during repository loading.
- Embedding failures retry per document; exhausted documents are skipped while the batch continues.
- Semantic query failure falls back to filesystem keyword retrieval.
- Answer-model failure falls back to an extractive answer.
- Qdrant loss can be recovered by rebuilding from `knowledge/`.
- job progress survives as JSON history, but execution itself is in-process and is not resumable after an API restart.

---

## 13. Important implementation caveats

1. “Hybrid search” means two application-level result sets are merged. Qdrant sparse retrieval is disabled.
2. The `/ingest/` active-job branch says a request is queued, but it does not submit the new request; it returns the current job ID.
3. The all-files-rejected upload branch uses `job.id` before `job` exists.
4. The health endpoint's LLM readiness check is API-key-oriented and does not accurately describe Vertex credential readiness.
5. Website ingestion and uploaded-file ingestion intentionally use different concept-generation methods: deterministic heading sections for web HTML, LLM/heuristic metadata plus whole loaded documents for uploads.
6. Streamlit's typewriter display is client-side presentation after the full API answer arrives; it is not token streaming from the model.
7. The dashboard has two status mechanisms: server-embedded status and browser-side polling. The embedded value protects deployments where a browser cannot resolve Docker's internal API hostname.

---

## 14. Endpoint-to-function reference

| Method and endpoint | Route function | Main downstream function | Purpose |
|---|---|---|---|
| `GET /health` | `api.main.health_check` | `hybrid_search.get_qdrant_client` | API/dependency status |
| `GET /api/v1/ingest/sources` | `ingest.list_available_sources` | `crawler.load_sources` | Read configured sources |
| `GET /api/v1/ingest/status` | `ingest.get_ingestion_status` | `status.get_status` | Legacy current progress |
| `POST /api/v1/ingest/` | `ingest.ingest_documents` | `job_manager.submit` | Start website/cached ingestion |
| `POST /api/v1/ingest/upload` | `ingest.upload_documents` | `job_manager.submit` | Save and process exact uploads |
| `GET /api/v1/jobs/` | `jobs.list_jobs` | `job_manager.list_jobs` | Job history |
| `GET /api/v1/jobs/{id}` | `jobs.get_job` | `job_manager.get_job` | Exact-job progress/detail |
| `POST /api/v1/jobs/{id}/cancel` | `jobs.cancel_job` | `job_manager.cancel` | Cooperative cancellation |
| `GET /api/v1/knowledge/stats` | `concepts.stats` | `repository.knowledge_stats` | Repository counts |
| `GET /api/v1/knowledge/categories` | `concepts.categories` | `repository.list_categories` | Category names |
| `GET /api/v1/knowledge/concepts` | `concepts.concepts` | `repository.list_concepts` | Browse metadata |
| `GET /api/v1/knowledge/concepts/{id}` | `concepts.concept` | `repository.get_concept_dict` | Full concept body |
| `GET /api/v1/knowledge/search` | `concepts.search` | `repository.search_concepts` | Filesystem search |
| `GET /api/v1/knowledge/tags` | `concepts.tags` | `query.search.search_tags` | Tag list |
| `POST /api/v1/query/` | `query.query_knowledge_base` | `query.engine.generate_answer` | Legacy chat response |
| `POST /api/v1/ask/` | `query.ask` | `query.engine.generate_answer` | Rich grounded answer |

---

## 15. One complete mental model

When a user ingests data, the backend first creates a tracked job. Website content is discovered and synchronized into cache, while uploads are validated and saved directly. Changed inputs become OKF Markdown in `knowledge/`. Valid changed concepts are chunked, embedded, and inserted into Qdrant, with state hashes preventing unnecessary repeat work.

When a user asks a question, keyword search reads the authoritative Markdown and semantic search queries Qdrant concurrently. Strong results are deduplicated and hydrated back from the Markdown source of truth. The selected LLM receives only that bounded source context and produces a cited answer. If Qdrant or the LLM is unavailable, the system degrades to keyword retrieval and an extractive response instead of losing all functionality.
