# Tech Demo – Reviewer Questions Answered

## OKF DataOps Intern Project: implementation-backed review guide

**Transcript reviewed:** *Tech Demo _ DataOps December Interns – Cleaned Transcript.docx*  
**Transcript date:** 21 August 2026  
**Code reviewed:** current `okf-poc` repository  
**Report prepared:** 25 August 2026

---

## Purpose and scope

This report consolidates the Reviewer's repeated questions into meaningful technical topics. It answers each topic using the current application code, states whether the feature is implemented, identifies exact files and line numbers, explains what those lines do, and calls out gaps that should not be overstated in a future demonstration.

The line numbers refer to the repository as it existed when this report was generated. They can move after code edits.

### Implementation status legend

- **Implemented:** the current code contains the behavior and it is wired into the application.
- **Partially implemented:** a useful baseline exists, but it does not fully satisfy an enterprise interpretation of the question.
- **Not implemented:** the current code does not provide the capability.
- **Configuration-driven:** behavior exists, but sources or policies must be added to configuration rather than entered dynamically through the UI.

---

# 1. What does the application actually do, and what are its two flows?

### Reviewer questions covered

- Are there two flows?
- How do manual uploads and website ingestion differ?
- Where is the output stored?
- Is the output folder created automatically?

### Direct answer

The application has two main operational flows:

1. **Ingestion:** collects raw inputs, standardizes them as Markdown files with YAML metadata, and indexes those concepts in Qdrant.
2. **Query:** retrieves relevant concepts using keyword and semantic search, then gives the retrieved context to an LLM to produce a grounded answer with citations.

Ingestion itself has two input paths:

- **Configured website crawl:** selected documentation sources are discovered from seed URLs, an HTML index, or sitemaps. Changed HTML is cached, cleaned, converted to Markdown, split into concepts, saved under `knowledge/`, and indexed.
- **Manual upload:** PDF, Markdown, text, and JSON files are uploaded to `cache/`, converted into OKF documents, and indexed. Upload mode deliberately skips website crawling.

The canonical, portable output is the filesystem under `knowledge/<category>/`. Qdrant is an acceleration layer for semantic retrieval, not the only copy of the knowledge.

### Status

**Implemented.**

### Code locations and explanation

- `app/ingestion/pipeline.py:418-447` defines the complete pipeline contract and the distinction between `source_names` and `only_files`.
- `app/ingestion/pipeline.py:476-498` skips crawling in upload-only mode or calls `crawl_configured_sources()` for selected sites.
- `app/ingestion/pipeline.py:536-545` converts changed crawled HTML into OKF concept files.
- `app/ingestion/pipeline.py:641-697` extracts metadata and saves manually uploaded documents as OKF Markdown.
- `app/ingestion/pipeline.py:802-874` converts changed concepts into index documents, skips current vectors, and indexes only new or changed concepts.
- `app/converter/markdown.py:206-216` creates `knowledge/<category>/` automatically and writes `<concept_id>.md`.
- `app/okf/formatter.py:4-19` builds the portable OKF representation: YAML frontmatter between `---` markers followed by Markdown content.
- `app/indexing/indexer.py:42-58` converts each OKF concept into a LlamaIndex `Document`, carrying metadata into Qdrant.
- `app/query/engine.py:77-105` starts the query flow and invokes hybrid retrieval.

### Important correction for the demo

OKF standardization does not inherently require an LLM. In this PoC, however, uploaded-file metadata extraction can use Gemini/Vertex AI, with a heuristic fallback. Crawled web pages use deterministic heading-based concept splitting and do not require an LLM for the conversion itself.

---

# 2. How are base URLs, sitemap URLs, nested sitemaps, robots.txt, index URLs, and seed URLs used?

### Reviewer questions covered

- Are URLs supplied manually?
- Why are both `base_url` and `sitemap_url` present?
- How are the URLs scraped?
- What happens when a site has no sitemap?
- What is a seed URL and when is the optional parameter used?
- Does robots.txt identify URLs automatically?

### Direct answer

Each configured source has a `base_url` and may supply one of three discovery mechanisms:

1. **`seed_urls`:** an explicit list of final pages. These are used directly; the crawler does not recursively follow links from them.
2. **`index_url`:** an ordinary HTML page whose links are extracted, resolved to absolute URLs, filtered, and de-duplicated.
3. **Sitemap discovery:** use the configured `sitemap_url`; otherwise read `Sitemap:` entries from `/robots.txt`; if neither yields a sitemap, try `<base_url>/sitemap.xml`.

The Kubernetes root sitemap is a sitemap index. It contains child sitemap URLs, such as the English sitemap. The parser adds those nested sitemap URLs to a queue, visits them, extracts their final page URLs, applies `/docs/concepts/`, and stops at the configured maximum. This is why the application finds documentation pages even though the root XML shows only language sitemap files.

`base_url` supplies the site identity and provides a base for resolving relative URLs. `sitemap_url` points directly to a discovery document. `url_filter` is a plain substring inclusion rule. `exclude_filters` are substring exclusion rules.

### Status

**Implemented, with an important robots.txt limitation.**

### Code locations and explanation

- `config/sources.yaml:2-7` configures Kubernetes with its base URL, root sitemap, `/docs/concepts/` filter, category, and enabled state.
- `app/ingestion/crawler.py:189-238` implements discovery priority. Lines 212-217 return configured seed URLs; lines 219-226 use an HTML index; lines 228-230 select a configured sitemap, robots.txt sitemap entries, or the default `/sitemap.xml`; lines 231-238 invoke recursive sitemap discovery.
- `app/parser/sitemap.py:31-54` distinguishes final `<url>` records from nested `<sitemap>` records.
- `app/parser/sitemap.py:57-107` performs breadth-first sitemap traversal. Lines 74-81 manage the queue and prevent revisits; lines 89-99 extract, normalize, filter, and de-duplicate page URLs; lines 102-105 enqueue nested sitemaps.
- `app/parser/sitemap.py:110-156` extracts links from a configured HTML index and applies the same filters and limit.
- `app/parser/sitemap.py:19-28` parses only `Sitemap:` directives from robots.txt.

### Limitation that must be stated honestly

The crawler does **not** currently parse or enforce robots.txt `User-agent`, `Allow`, `Disallow`, or `Crawl-delay` rules. It uses robots.txt only to discover sitemap locations. Therefore, the earlier demo statement that URLs are filtered “using robots.txt” is too broad. URL inclusion is controlled by `url_filter` and `exclude_filters`; respecting robots exclusion policies is a separate missing feature.

### Recommended improvement

Add a standards-aware robots parser such as Python's `urllib.robotparser`, check `can_fetch(user_agent, page_url)` before each request, and support site-provided crawl delays. Also add a same-origin/domain check so a permissive sitemap or HTML index cannot lead the crawler outside the configured host.

---

# 3. How does URL filtering decide what is documentation and what is not?

### Reviewer questions covered

- Where is “documentation pages only” defined?
- How does it distinguish documentation from non-documentation?
- Is it based on the URL?
- Is the `/docs` rule coming from robots.txt?

### Direct answer

In the current PoC, documentation classification is **configuration-based URL substring matching**. For Kubernetes, a URL is included if the complete URL contains `/docs/concepts/`. It is not an AI classifier, content classifier, MIME classifier, or robots.txt rule.

For example:

- `https://kubernetes.io/docs/concepts/workloads/pods/` matches.
- `https://kubernetes.io/blog/...` does not match.
- A translated URL containing the same substring could also match unless a stricter filter or direct English sitemap is configured.

### Status

**Implemented as a simple rule; not enterprise-grade classification.**

### Code locations and explanation

- `config/sources.yaml:5` defines Kubernetes `url_filter: /docs/concepts/`.
- `app/parser/sitemap.py:90-99` applies inclusion and exclusion filters to sitemap page URLs. Line 94 checks `url_filter not in page`; lines 96-97 apply exclusions.
- `app/ingestion/crawler.py:212-217` applies the rules to explicit seed URLs.
- `app/parser/sitemap.py:139-153` applies the rules to links obtained from an HTML index.

### Limitations and recommended improvement

Substring filtering is easy to explain and deterministic, but it can admit unintended URLs or reject valid content when site structures change. A stronger implementation should support anchored regular expressions, allowed hosts, allowed path prefixes, content types, language selection, canonical URL handling, and per-source tests. For Kubernetes, pointing directly to `https://kubernetes.io/en/sitemap.xml` and requiring the full prefix `https://kubernetes.io/docs/concepts/` would make English-only intent clearer.

---

# 4. What do delay, timeout, crawl limit, and User-Agent mean? Is rate limiting implemented?

### Reviewer questions covered

- How are scraping API calls rate-limited?
- Are HTTP API calls used for scraping?
- Can you show the implementation?
- What User-Agent is sent? Chrome or Firefox?
- What does `max_urls_per_source` mean?

### Direct answer

Yes, scraping uses HTTP GET requests through `httpx.AsyncClient`.

The crawler configuration means:

- `delay: 0.05`: maintain at least 0.05 seconds between request starts made by this crawler instance.
- `timeout: 30`: allow an HTTP operation up to 30 seconds before it fails.
- `max_urls_per_source: 50`: return at most 50 matching final page URLs for each selected source. It does not mean “50 sources.”
- `user_agent: OKF-Crawler/1.0`: send a custom crawler identity. It is neither Chrome nor Firefox.

The fixed delay is a basic form of polite request pacing, but it is not complete adaptive rate-limit handling. The crawling code does not specially handle HTTP 429, `Retry-After`, exponential backoff, jitter, or per-host concurrency. A 429 currently becomes a failed request. Separate LLM and embedding calls do have retry/backoff logic.

### Status

**Partially implemented.** Fixed pacing and timeout are implemented; adaptive HTTP rate-limit handling is not.

### Code locations and explanation

- `config/sources.yaml:62-66` contains the live values.
- `app/ingestion/crawler.py:114-130` stores these settings, sleeps until the required interval has elapsed, creates an HTTP client, follows redirects, adds request headers, performs GET, and raises on non-success responses.
- `app/ingestion/crawler.py:132-177` applies the same pacing and headers to document requests that also capture ETag and Last-Modified.
- `app/ingestion/crawler.py:465-480` loads delay, timeout, User-Agent, and global maximum from YAML.
- `app/ingestion/crawler.py:516-529` passes the global maximum to each source, while allowing a per-source `max_urls` override.
- `app/parser/sitemap.py:77-107` stops discovery and returns no more than the maximum number of matching URLs.
- `app/ingestion/metadata_extractor.py:200-232` retries metadata LLM calls on quota/rate errors and falls back heuristically.
- `app/retrieval/hybrid_search.py:278-304` applies configurable retry/backoff to embedding calls and reports rate-limit hits to job status.

### User-Agent assessment

`OKF-Crawler/1.0` is a valid custom header value, but responsible production crawlers commonly include a product URL or operator contact, for example `OKF-Crawler/1.0 (+https://company.example/crawler-info)`. Pretending to be Chrome is usually the wrong design for an identifiable enterprise crawler. The correct approach is transparent identification plus robots-policy compliance.

---

# 5. Does the crawler scrape everything again? How is a changed page detected?

### Reviewer questions covered

- Does it scrape every time?
- Is state stored before scraping again?
- What is compared?
- Is comparison based on content or metadata?
- What happens when the URL stays the same but the page content changes?
- Why is a hash needed?

### Direct answer

Every run rediscovers candidate URLs and makes conditional requests for them, but it does not necessarily download, rewrite, reconvert, or re-embed every page.

For each URL, the crawler stores:

- cached raw-file path;
- SHA-256 hash of the response body;
- HTTP ETag, if provided;
- HTTP Last-Modified value, if provided.

On the next run, it sends `If-None-Match` and/or `If-Modified-Since`. If the server returns `304 Not Modified`, the page is marked unchanged without downloading a response body. If the server returns content, the application hashes the bytes and compares that content hash with the previous content hash. Therefore, the same URL with different content is detected correctly even if the server does not provide useful cache validators.

### Status

**Implemented.** This was explained incorrectly during the demo: the URL hash is not the content-change test.

### Code locations and explanation

- `app/ingestion/crawler.py:48-56` hashes the URL only to create a short, safe cache filename. This solves filesystem naming; it does not determine whether content changed.
- `app/ingestion/crawler.py:107-109` computes SHA-256 over downloaded content.
- `app/ingestion/crawler.py:261-269` loads previous source state and retrieves the record keyed by the full URL.
- `app/ingestion/crawler.py:271-283` builds conditional request headers from the previous ETag and Last-Modified values.
- `app/ingestion/crawler.py:285-295` treats HTTP 304 as unchanged.
- `app/ingestion/crawler.py:297-334` hashes a returned body, compares it with the previous content hash, writes only new/changed content, and stores updated validators.
- `app/storage/state_manager.py:68-116` loads and atomically saves per-source crawler state under `cache/.state/<source>.json`.
- `app/ingestion/pipeline.py:294-320` processes only changed pages in normal operation, with a cache-recovery path for initial bootstrap.
- `app/indexing/vector_state.py:22-27` separately hashes each embeddable concept's text and ID.
- `app/indexing/vector_state.py:84-136` skips embedding when the concept hash is current and its `source_file` is already present in Qdrant.

### Distinguish the three hashes

1. **URL hash:** creates a compact cache filename.
2. **Raw content hash:** detects changes to a downloaded page or uploaded file.
3. **Vector-state content hash:** detects whether the generated concept text needs re-embedding.

These solve different problems and should be explained separately.

---

# 6. What are tags, IDs, created_at, and updated_at? Do timestamps detect changes?

### Reviewer questions covered

- What are tags?
- Where are tags stored?
- Where is `updated_at` stored?
- What does the ID identify?
- What actually identifies a change?

### Direct answer

These values are OKF metadata stored in the YAML frontmatter of each Markdown concept:

- **`id`:** stable identifier used for lookup, de-duplication, filenames, citations, and Qdrant metadata.
- **`tags`:** searchable labels describing topics. Keyword search gives matches in tags extra weight.
- **`created_at`:** intended creation date of the concept record.
- **`updated_at`:** intended last update date of the concept record.
- **`source`:** provenance containing source name and URL.
- **`related`:** IDs of related concepts.

However, the current generators set both `created_at` and `updated_at` to today's date whenever they rewrite a concept. They do not preserve the original creation date or copy the source page's published/modified date. These fields are not used for change detection; SHA-256 content hashes and HTTP validators perform that job.

### Status

**Metadata schema implemented; timestamp lifecycle partially implemented; automatic relationships not implemented.**

### Code locations and explanation

- `app/okf/schema.py:37-50` defines ID, title, category, tags, source, timestamps, aliases, and related IDs.
- `app/okf/schema.py:70-85` flattens those values into metadata stored with Qdrant documents.
- `app/converter/markdown.py:84-103` builds a stable crawled-page concept ID from category, heading title, and an eight-character hash of the source URL.
- `app/converter/markdown.py:140-150` creates frontmatter for crawled concepts and currently assigns today's date to both timestamps.
- `app/ingestion/pipeline.py:69-113` creates IDs, categories, tags, provenance, timestamps, and empty relationship lists for uploaded documents. Lines 81-86 map extracted topics to tags; lines 105-108 set dates and empty `aliases`/`related`.
- `app/ingestion/metadata_extractor.py:30-43` defines the LLM-produced metadata, including three to five topics.
- `app/okf/repository.py:208-255` makes title, aliases, description, tags, and content searchable.
- `app/okf/repository.py:298-315` weights title, alias, and tag hits more strongly than description/content hits.

### Recommended improvement

When rewriting a stable concept ID, read its existing frontmatter and preserve `created_at`; update `updated_at` only when normalized content or meaningful metadata changes. Capture source `lastmod` from sitemaps or document properties in a separate field such as `source_updated_at`, because source modification time and local processing time are different facts.

---

# 7. How is a concept created? Does one page create one file or many files?

### Reviewer questions covered

- What is a concept?
- How is a concept generated?
- How are different concepts identified?
- Is a concept based on a page, section, or heading?
- If there are 100 pages, are there 100 files?
- Can one page create multiple Markdown files?

### Direct answer

In this PoC, a **concept** is a portable unit of knowledge: one Markdown body plus validated YAML metadata such as ID, title, category, tags, source, and dates.

For crawled HTML, concept boundaries are deterministic and heading-based:

1. Remove navigation and page noise.
2. Convert semantic HTML to Markdown.
3. Split at H2 and H3 headings.
4. Treat pre-heading introduction text as a section.
5. Merge very short sections into the preceding section.
6. Truncate very long sections to the configured maximum.
7. Generate one OKF Markdown file for each resulting section.

Consequently, 100 pages do not imply exactly 100 concept files. A page with three qualifying sections can produce three files; a page without H2/H3 headings normally produces one. The precise total depends on structure and minimum-size merging.

Uploaded documents follow a different path. The raw loader may produce one or more LlamaIndex documents/pages, and the pipeline currently writes one OKF file for each loaded document unit. It does not pass uploads through the same H2/H3 concept splitter. Later, the indexer performs sentence-level chunks for embeddings, but those vector chunks are not separate OKF files.

### Status

**Implemented, but with two different concept-generation paths.**

### Code locations and explanation

- `app/parser/cleaner.py:14-93` lists navigation/noise elements to remove and semantic containers to retain.
- `app/parser/cleaner.py:96-136` selects main content, removes noise, resolves relative links, and removes empty blocks.
- `app/converter/markdown.py:28` defines H2/H3 as concept boundaries.
- `app/converter/markdown.py:43-77` performs the actual split, introduction handling, short-section merging, and long-section truncation.
- `app/core/config.py:41-43` configures concepts between 200 and 4,000 characters.
- `app/converter/markdown.py:155-190` gives each section a title and stable ID and serializes it into OKF content.
- `app/ingestion/pipeline.py:358-390` wires cleaning, Markdown conversion, concept splitting, old-concept replacement, and file writing into crawled ingestion.
- `app/ingestion/pipeline.py:602-608` loads uploaded files through `SimpleDirectoryReader`.
- `app/ingestion/pipeline.py:646-697` extracts metadata and writes one OKF file per returned uploaded-document unit.
- `app/retrieval/hybrid_search.py:230-240` separately configures vector chunks with `CHUNK_SIZE` and `CHUNK_OVERLAP`.

### Important limitations

- The crawler splitter is structural, not semantic. A heading is treated as a concept boundary even when meaning spans several headings.
- Content longer than 4,000 characters is truncated rather than recursively divided, so data can be lost from a concept file.
- Upload and crawl paths do not use the same concept-granularity policy.
- The comment about a future semantic splitter at `app/converter/markdown.py:168-173` is documentation, not an active implementation.

---

# 8. How are concepts related and how is mixed enterprise content segregated?

### Reviewer questions covered

- How are concepts brought together?
- How are relationships recorded?
- How would policies, business logic, and technical content be segregated?
- Is segregation based on source, metadata, content type, similarity, or a graph?

### Direct answer

The current structure provides three levels of organization:

1. **Filesystem category:** files are stored under `knowledge/<category>/`.
2. **Metadata:** category, tags, aliases, type, provenance, and optional related IDs accompany every concept.
3. **Vector similarity:** embeddings allow semantically related concepts to be retrieved even when they are in different files or do not share exact keywords.

This is useful organization, but it is not a complete enterprise taxonomy or knowledge graph. For crawled content, category currently defaults to the source name, so a Confluence source would tend to become one broad `confluence` category unless additional classification were added. For uploaded files, an LLM or heuristic assigns a document type and topics, but relationships are initialized as empty. No code automatically creates or validates graph edges between concepts.

### Status

**Partially implemented. Automatic relationship extraction and graph traversal are not implemented.**

### Code locations and explanation

- `app/ingestion/pipeline.py:369-376` uses the crawled source name as category and performs heading-based splitting.
- `app/ingestion/metadata_extractor.py:185-198` asks the LLM to infer title, summary, document type, topics, and trust level for uploads.
- `app/ingestion/pipeline.py:74-108` maps document type to category and topics to tags, but assigns `related: []`.
- `app/okf/schema.py:45-50` supports tags, aliases, and related concept IDs in the schema.
- `app/okf/schema.py:70-85` sends this metadata to Qdrant.
- `app/query/search.py:133-143` can apply an exact category filter during semantic retrieval.

### Recommended enterprise design

Introduce a controlled taxonomy independent of connector/source names: department, domain, document class, confidentiality, jurisdiction, product, version, owner, and effective dates. Classify sections using deterministic rules plus a reviewed model-assisted classifier. Generate relationship candidates such as `depends_on`, `supersedes`, `implements`, and `references`; validate their target IDs; and store typed edges in a graph-capable layer or explicit OKF relationship records. Preserve access-control metadata through indexing and enforce it during retrieval.

---

# 9. How does keyword, semantic, and hybrid search work? Who decides which one runs?

### Reviewer questions covered

- Does the assistant perform semantic or text search?
- Why are both needed?
- Who decides the logic?
- Is the decision in the router or retrieval component?
- Does the system search metadata first?

### Direct answer

The API router does not inspect each question and dynamically choose one search type. `generate_answer()` calls the search layer in `auto` mode. In `auto`, keyword and semantic searches run concurrently; successful results are combined, de-duplicated, score-filtered, and capped at five citations.

- **Keyword search** scans the filesystem knowledge repository and checks whole-token matches across title, aliases, description, tags, and content. Title, alias, and tag hits receive greater weight.
- **Semantic search** embeds the question and asks Qdrant for nearest vector matches. It can use an exact category metadata filter when a category is supplied.
- **Hybrid behavior** merges both result sets. If semantic retrieval is unavailable, the system degrades to keyword-only results.

Both are useful because exact identifiers, commands, product names, and error strings favor lexical matching, while paraphrases, synonyms, and conceptual similarity favor embeddings.

### Status

**Implemented.** The term “hybrid” here means application-level combination of dense semantic results and filesystem keyword results; the Qdrant store itself is configured dense-only in the current code.

### Code locations and explanation

- `app/query/engine.py:77-105` caps `top_k` at five and calls `search(..., mode="auto")`.
- `app/query/search.py:62-87` exposes explicit keyword and semantic modes.
- `app/query/search.py:89-126` implements auto mode, running keyword and semantic work in parallel and reporting whether the outcome was hybrid, semantic, or keyword.
- `app/query/search.py:43-59` de-duplicates results, removes weak citations, applies absolute/relative score thresholds, and returns at most five.
- `app/okf/repository.py:258-340` implements filesystem keyword search, metadata filters, whole-token matching, field weighting, score normalization, snippets, and ranking.
- `app/query/search.py:129-161` implements Qdrant semantic retrieval and category filters, returning an empty list on failure so keyword search remains usable.
- `app/retrieval/hybrid_search.py:45-48` configures the Qdrant vector store with `enable_hybrid=False`, confirming that sparse vectors are not active there.

### Clarification about metadata-first search

The system does not universally search metadata first and then content. Keyword mode evaluates searchable metadata and content in one scoring pass. Semantic mode searches embedded text and can pre-filter by category. Source-specific retrieval is possible through category in `/ask`, but there is no general `source_file` request filter exposed by the current API.

---

# 10. How does this scale better than opening millions of files and searching text?

### Reviewer questions covered

- How does the system focus on relevant content instead of scanning everything?
- How is it different from terminal text search?
- Will it load all files into memory?
- What happens with millions of documents?

### Direct answer

Semantic retrieval is the scalable path: concepts are embedded once during ingestion, stored as vectors in Qdrant, and retrieved using a nearest-neighbor index. At query time, the application asks Qdrant for a small top-k candidate set rather than reading every full document into the prompt. Only the strongest concepts are expanded and sent to the LLM.

However, the current keyword implementation is not yet designed for millions of files. It loads and validates all Markdown concepts into a process cache, then iterates over every concept and searchable field for each keyword query. The cache avoids repeated disk parsing when files have not changed, but the algorithm is still approximately linear in the number and size of concepts.

Therefore, the correct claim is:

- Qdrant semantic search provides indexed candidate retrieval.
- The current filesystem keyword fallback is suitable for a PoC or moderate collection, not a million-document production corpus.

### Status

**Semantic scaling implemented; large-scale lexical indexing not implemented.**

### Code locations and explanation

- `app/indexing/indexer.py:42-58` turns concepts into indexable documents with metadata.
- `app/retrieval/hybrid_search.py:230-240` splits text into overlapping chunks before vector insertion.
- `app/query/search.py:142-158` requests only `similarity_top_k` nodes from Qdrant.
- `app/query/search.py:167-186` caches the Qdrant index object while Qdrant itself reflects newly inserted points.
- `app/okf/repository.py:281-340` shows that keyword mode loops through every loaded concept and field.
- `app/okf/repository.py:20-105` discovers, parses, validates, and process-caches the filesystem knowledge repository.
- `app/query/engine.py:108-145` expands only retrieved concepts to full authoritative content before answer generation.

### Recommended production approach

Use a real inverted text index—OpenSearch/Elasticsearch, PostgreSQL full-text search, or Qdrant sparse vectors—for lexical retrieval. Apply tenant and ACL filters before scoring, use pagination, monitor index freshness, and measure recall/latency at realistic corpus sizes. Continue using the portable OKF files as the source of truth if that is a project requirement, but do not scan them all per request.

---

# 11. How does the system find information from one specific document and preserve citations?

### Reviewer questions covered

- If a question is specific to document one, how is that source identified?
- Does the system scan all files or use metadata?
- How are citations produced?

### Direct answer

Every concept carries provenance metadata. Crawled concepts store the source page's name and URL. Indexed concepts also receive a `source_file` path identifying the generated OKF file. Retrieval returns the concept ID, title, category, source URL, source file, score, and snippet. The answer engine reloads the full concept by ID and passes its content and URL to the LLM, then returns citations with the answer.

The current API can narrow `/ask` by category, but it does not expose a general document/source filter. A question mentioning a filename may match keyword metadata if that filename is represented, but strict “search only this document” behavior is not guaranteed without a dedicated filter.

### Status

**Citation provenance implemented; strict source-scoped retrieval partially implemented.**

### Code locations and explanation

- `app/converter/markdown.py:140-150` stores source name and URL in crawled concept frontmatter.
- `app/ingestion/pipeline.py:90-113` carries source provenance into uploaded-document metadata.
- `app/okf/schema.py:70-85` defines the metadata payload sent to Qdrant.
- `app/indexing/indexer.py:42-56` adds `source_file` and indexes full text plus metadata.
- `app/query/search.py:144-158` returns semantic provenance and scores.
- `app/query/engine.py:108-145` reloads full authoritative concept content and constructs the grounded context.
- `app/api/routers/query.py:34-74` returns citations for `/api/v1/query/`.
- `app/api/routers/query.py:87-129` exposes category and `top_k` for `/api/v1/ask/` and returns richer source evidence.

### Recommended improvement

Expose filters for `source_file`, `source_name`, `source_url`, document ID, tenant, and ACL. Apply the same filters consistently to keyword and semantic retrieval. The current auto path passes category to both searches, but a generalized filter object would make document-scoped answers reliable.

---

# 12. Where is job progress and result information stored, and how does the UI receive it?

### Reviewer questions covered

- Is job status streamed to the UI?
- Is an API endpoint called?
- Where are job details and results stored?
- What fields are stored?

### Direct answer

The UI does **polling**, not server push or true streaming. Starting ingestion creates a 12-character job ID. A background worker processes one job at a time. Pipeline status updates are copied onto the active `Job`, serialized to JSON under `cache/.jobs/<job_id>.json`, and returned by the job API. The UI repeatedly requests `/api/v1/jobs/<job_id>` and redraws progress.

Job data includes lifecycle status, parameters, messages, errors, final result, timestamps, discovered/fetched/processed/failed/indexed counts, token estimates, rate-limit hits, stage, stage message, and current source. Knowledge documents themselves are stored separately under `knowledge/`; raw crawl and state data live under `cache/`.

### Status

**Implemented.** Call it polling rather than streaming.

### Code locations and explanation

- `app/jobs/models.py:32-81` defines the job record and live counters.
- `app/jobs/models.py:83-111` serializes the job fields returned by the API and written to disk.
- `app/jobs/manager.py:135-149` generates an ID, queues the job, persists it, and starts the worker.
- `app/jobs/manager.py:217-227` copies pipeline status fields to the active job and persists every update.
- `app/jobs/manager.py:266-313` executes jobs in the worker and stores the final result or error.
- `app/jobs/manager.py:317-340` writes atomic JSON records under `cache/.jobs/` and reloads history after restart.
- `app/api/routers/jobs.py:23-50` provides list, detail, and cancellation endpoints.
- `app/api/routers/ingest.py:78-125` creates an ingestion job and returns its ID.
- `app/ui/app.py:84-118` starts ingestion and stores the returned job ID in Streamlit session state.
- `app/ui/app.py:139-155` polls the exact job endpoint.
- `app/ingestion/crawler.py:344-355` updates download counters after each page.
- `app/retrieval/hybrid_search.py:257-323` updates indexing progress after each concept and surfaces 429 retries.

### Operational limitation

Jobs survive process restart as history, but active jobs do not resume. `Job.from_dict()` marks stale queued/running records as failed after restart (`app/jobs/models.py:139-147`). This is appropriate for a local PoC, but distributed production execution would normally use a durable queue and workers.

---

# 13. How are new sources added? Is the UI enough, and is a restart required?

### Reviewer questions covered

- What is the process to add another source?
- Is a code change required?
- Can any URL be entered directly in the UI?
- Is source configuration controlled entirely through the UI?
- Is an application restart required?

### Direct answer

The current UI can enable or disable sources that already exist in `config/sources.yaml`. It cannot create an arbitrary source definition or accept a new crawl URL directly.

To add a source, add a YAML entry containing at least a unique name, base URL, category, and a discovery strategy. Add filters and authentication only if the implementation supports them. This is normally a configuration change, not a Python-code change.

A backend restart is generally **not required** for a simple YAML change because `load_sources()` reads the YAML file each time it is called. The UI must rerun or refresh its available-sources request to display the new entry. A restart may still be needed in a deployment if configuration is baked into an immutable container image rather than mounted at runtime.

### Status

**Configuration-driven; arbitrary UI source creation is not implemented.**

### Code locations and explanation

- `app/ingestion/crawler.py:58-68` reads `sources.yaml` from disk on demand.
- `app/api/routers/ingest.py:40-56` returns all configured sources to the UI.
- `app/ui/app.py:74-81` requests the configured source list from the backend.
- `app/ingestion/crawler.py:70-104` persists only the selected/enabled flags; it does not create new source definitions.
- `app/api/routers/ingest.py:105-116` updates selection and submits selected source names.
- `app/ingestion/crawler.py:458-463` resolves those names against configured entries.

### Recommended improvement

Provide a validated source-management API and admin-only UI with fields for discovery type, filters, credentials reference, crawl policy, and test discovery. Never accept an arbitrary URL and immediately crawl it without SSRF protections, DNS/IP validation, scheme restrictions, redirect checks, allowlists, and authorization.

---

# 14. Can Confluence or SharePoint be ingested, including secure enterprise pages?

### Reviewer questions covered

- How would a knowledge base be created from Confluence and SharePoint?
- What about authentication for enterprise URLs?
- Will simply adding those URLs to source configuration work?

### Direct answer

Public HTML pages with usable sitemaps or index pages could fit the current generic crawler. Authenticated Confluence and SharePoint cannot be handled correctly merely by adding their URLs to `sources.yaml`.

A production connector needs:

1. connector-specific authentication, such as OAuth 2.0/service credentials;
2. API-based pagination rather than public sitemap assumptions;
3. recursive enumeration of spaces/sites, pages, attachments, and versions;
4. conversion of platform-specific rich content;
5. rate-limit and retry handling;
6. incremental cursors, version IDs, ETags, or modified timestamps;
7. preservation and query-time enforcement of user/group permissions;
8. secure secret storage and audit logs.

For Confluence, this generally means using its REST APIs to enumerate permitted spaces/pages and fetch page bodies/attachments. For SharePoint, it generally means Microsoft Graph or SharePoint APIs to enumerate sites, drives, lists, pages, and permissions. The connector must map source IDs and versions into OKF provenance and state records.

### Status

**Not implemented.** The repository contains no Confluence or SharePoint connector and the generic crawler has no source authentication mechanism.

### Code evidence

- `config/sources.yaml:1-66` contains only public documentation-style sources and no credential references.
- `app/ingestion/crawler.py:123-129` and `155-160` build anonymous HTTP clients with User-Agent and Accept headers only.
- `app/ingestion/crawler.py:189-238` supports sitemap/index/seed discovery, not connector APIs or pagination tokens.
- `app/core/gcp_auth.py` handles Google/Vertex model credentials; it is unrelated to authenticating crawl sources.
- `app/api/main.py:14-22` currently allows broad CORS for the PoC and is not an enterprise authentication layer.

### Recommended implementation boundary

Create a connector interface such as `discover_changes()`, `fetch_document()`, `fetch_permissions()`, and `checkpoint()`. Implement Confluence and SharePoint adapters separately. Store only secret references in source configuration, not tokens. Carry ACL principals into OKF/Qdrant metadata and require caller identity when querying. Without retrieval-time ACL enforcement, ingesting secured enterprise content would create a serious data-leak risk.

---

# 15. How are upload formats handled, and what happens when a new format is required?

### Reviewer questions covered

- If there is a new format, is it handled through the UI?
- What formats are currently supported?
- Is backend work required to support another type?

### Direct answer

The UI is only the entry point. Format support is enforced and implemented in the backend. The current upload API accepts PDF, Markdown, text, and JSON, with a maximum of 50 MB per file. Adding a format requires coordinated changes to validation, UI file-type selection, the document loader/parser, tests, and potentially cleaning or metadata extraction.

XML and RMarkdown were mentioned during the presentation, but they are not accepted by the current upload endpoint. The demo should not claim they are currently supported.

### Status

**Four formats implemented; generic plug-in format support not implemented.**

### Code locations and explanation

- `app/api/routers/ingest.py:160-164` accepts only `.pdf`, `.md`, `.txt`, and `.json`.
- `app/api/routers/ingest.py:180-199` documents the upload behavior and supported formats.
- `app/api/routers/ingest.py:228-266` validates extensions, sanitizes filenames, reads content, enforces 50 MB, and writes successful uploads to cache.
- `app/storage/state_manager.py:159-192` discovers the same four file extensions for local ingestion.
- `app/ingestion/loaders.py:22-35` assigns `PyMuPDFReader` to PDFs and uses `SimpleDirectoryReader` for the supported set.
- `app/ingestion/pipeline.py:602-608` loads each selected uploaded file.

### Recommended improvement

Create a parser registry keyed by MIME type and extension, validate the actual file signature instead of trusting only the filename, set per-type size/page limits, sandbox risky parsers, and test malformed inputs. DOCX support would require a Word parser; XML requires a schema/content strategy rather than treating every XML file as equivalent.

---

# 16. What API endpoints are involved, and what are their result limits?

### Reviewer questions covered

- Is an endpoint called for job status?
- Which endpoints serve query, concepts, and sources?
- How many results are fetched?

### Direct answer

The application registers all functional routers under `/api/v1`.

- `GET /api/v1/ingest/sources`: all configured crawl sources; no pagination.
- `GET /api/v1/ingest/status`: legacy active-job status.
- `POST /api/v1/ingest/`: start configured-source ingestion.
- `POST /api/v1/ingest/upload`: upload files and start upload-only ingestion.
- `GET /api/v1/jobs/`: job history, optional unvalidated `limit`; all jobs if omitted.
- `GET /api/v1/jobs/{job_id}`: one exact job.
- `POST /api/v1/jobs/{job_id}/cancel`: request cancellation.
- `GET /api/v1/knowledge/concepts`: all concepts, optional category; no pagination.
- `GET /api/v1/knowledge/search`: all lexical matches; no pagination.
- `POST /api/v1/query/`: answer plus at most five citations.
- `POST /api/v1/ask/`: category-aware answer plus at most five sources.

Crawler discovery is separately limited to 50 matching URLs **per source** by current YAML configuration.

### Status

**Implemented, but list endpoints need production pagination and validation.**

### Code locations and explanation

- `app/api/main.py:24-30` registers the routers under `/api/v1`.
- `app/api/routers/ingest.py:40-125` defines source listing, status, and ingestion start.
- `app/api/routers/ingest.py:180-301` defines upload ingestion.
- `app/api/routers/jobs.py:23-50` defines job list/detail/cancellation.
- `app/api/routers/concepts.py:16-59` defines knowledge statistics, categories, concepts, search, and tags.
- `app/api/routers/query.py:53-74` and `110-129` define both query endpoints.
- `app/core/config.py:33-37` sets `TOP_K=5` and citation thresholds.
- `app/query/search.py:43-59` enforces the final five-result maximum.
- `config/sources.yaml:65` sets 50 URLs per source.

### Recommended improvement

Add validated `limit` and cursor/offset parameters with safe defaults and maximums to jobs, concepts, search, tags, and sources. Reject negative limits. Return pagination metadata and avoid loading all filesystem concepts for large collections.

---

# 17. What should be said about authentication and security in the current PoC?

### Reviewer questions covered

- Has authentication been implemented?
- How will secure documents be protected?

### Direct answer

Authentication for end users, source systems, and authorization-aware retrieval is not implemented as an application-wide feature. The PoC has credentials for its AI provider, but that is not user authentication and does not grant safe access to Confluence or SharePoint.

The API currently allows all CORS origins, and the shown routers do not require an authenticated principal. Uploaded and generated documents are local files. Qdrant payloads do not contain enforced ACLs. Therefore, this PoC should be demonstrated only with non-sensitive test data unless it is placed behind trusted infrastructure controls.

### Status

**Not implemented for enterprise users and source ACLs.**

### Code locations and explanation

- `app/api/main.py:14-22` configures permissive PoC CORS and no authentication middleware.
- `app/api/routers/ingest.py`, `jobs.py`, `concepts.py`, and `query.py` expose routes without user dependencies or authorization checks.
- `app/core/gcp_auth.py` handles model-provider credentials only.
- `app/okf/schema.py:70-85` shows the indexed metadata payload; it has no tenant, user, group, or ACL fields.

### Required enterprise controls

Add SSO/OIDC authentication, role-based administration, connector credential vaulting, tenant separation, encryption, malware scanning for uploads, SSRF protection for configured URLs, audit trails, data-retention rules, and retrieval-time document ACL filters. Permission trimming must happen before results are returned to the LLM, not after answer generation.

---

# 18. What were the unclear code comments/files the Reviewer asked about?

### Reviewer questions covered

- What is this comment and why is it needed?
- Why does the platform need this file?
- Can it be removed?
- Is anything besides keywords used?

### Direct answer

The transcript does not identify the exact on-screen file or comment, so it is unsafe to claim one definitive target. The nearby discussion aligns with the defensive filtering in `app/query/search.py` and repository validation:

- internal job-status JSON accidentally indexed as knowledge is rejected;
- unusable concepts with missing/placeholder titles or categories are skipped;
- search uses semantic similarity, title, aliases, description, tags, content, scores, category filters, and provenance—not only raw keywords.

These guards should not be removed without understanding the failure they prevent. Removing a comment is harmless; removing the corresponding validation can allow monitoring records or low-quality placeholder documents to appear as citations.

### Status

**Defensive filtering implemented; exact transcript reference indeterminate.**

### Code locations and explanation

- `app/query/search.py:20-40` detects internal job records using known status markers and ID/title patterns.
- `app/query/search.py:43-59` rejects internal records and weak citations.
- `app/okf/repository.py:53-67` rejects concepts with unusable titles or missing categories.
- `app/okf/repository.py:208-255` defines searchable metadata and content fields.
- `app/query/search.py:129-158` adds vector similarity and optional category filtering.

---

# Demo-ready summary answers

The following concise responses can be used in a future review before opening the referenced code.

## Crawling

“A source is configuration-driven. We discover exact seed pages first, otherwise links from an index page, otherwise a configured or discovered sitemap. Sitemap indexes are traversed recursively. URL inclusion and exclusion are explicit substring rules. The current robots implementation only discovers sitemap directives; full robots policy enforcement is a known gap.”

## Rate limits and identity

“The crawler sends ordinary HTTP GET requests using a transparent custom User-Agent, waits at least 50 milliseconds between requests, times out after 30 seconds, and caps discovery at 50 matching pages per source. This is basic pacing, not complete 429 handling; adaptive backoff and `Retry-After` support are still required.”

## Incremental ingestion

“The URL hash only creates a cache filename. Actual update detection uses conditional ETag/Last-Modified requests plus a SHA-256 content hash fallback. Only changed pages are rewritten and converted, and only changed concepts are embedded again.”

## Concepts

“An OKF concept is a Markdown knowledge unit with validated YAML metadata. Crawled pages are split deterministically at H2/H3 headings, so one page can generate multiple concepts. Uploaded files use metadata extraction and currently follow a different, document-unit path. Automatic semantic relationship generation is not yet implemented.”

## Retrieval

“The answer engine always requests auto retrieval. Keyword and semantic searches run together, their candidates are merged and filtered, and at most five strong citations are returned. Semantic retrieval uses Qdrant; keyword retrieval currently scans the cached filesystem repository and is not yet suitable for millions of documents.”

## Enterprise connectors

“Public documentation fits the generic crawler. Authenticated Confluence and SharePoint need dedicated API connectors, OAuth/service credentials, pagination, incremental checkpoints, attachment support, and ACL-aware retrieval. That capability is not present in this PoC.”

## Job tracking

“Starting ingestion creates a persisted job record. The UI polls the job-specific REST endpoint; it is not a push stream. Status, counters, timestamps, errors, and the final result are saved under `cache/.jobs`, while raw data and canonical OKF knowledge are stored separately.”

---

# Prioritized follow-up backlog

## High priority: correctness and security

1. Enforce robots.txt rules, same-origin restrictions, redirect safety, and SSRF protection.
2. Add adaptive crawl retries for 429/5xx responses with `Retry-After`, exponential backoff, and jitter.
3. Add authentication, authorization, tenant/ACL metadata, and permission-filtered retrieval before using secure enterprise sources.
4. Implement dedicated Confluence and SharePoint connectors rather than treating them as public websites.
5. Preserve `created_at` and model source modification time separately from local processing time.

## Medium priority: quality and consistency

6. Unify concept generation for crawled and uploaded documents.
7. Replace destructive 4,000-character truncation with recursive splitting.
8. Add controlled taxonomy classification and typed concept relationships.
9. Expose reliable source/document filters in both keyword and semantic search.
10. Add a true inverted lexical index for large corpora.

## Operational improvements

11. Add pagination and validated caps to list/search endpoints.
12. Add an admin source-management API/UI with safe URL validation.
13. Use a durable distributed job queue if jobs must resume or scale across processes.
14. Add metrics for crawl response codes, retry counts, latency, cache hits, changed pages, embedding cost, and retrieval quality.
15. Add integration tests for sitemap indexes, robots policies, redirects, 304 responses, 429 retries, source deletion, ACL filters, and large-corpus queries.

---

# Final implementation assessment

The PoC has a credible end-to-end foundation: configuration-based public documentation discovery, nested sitemap traversal, incremental HTTP synchronization, HTML cleaning, portable OKF files, job persistence, Qdrant indexing, and combined keyword/semantic retrieval are all present in code.

The strongest corrections to the original demo are:

- basic crawl pacing **is** implemented, although adaptive 429 handling is not;
- change detection uses ETag/Last-Modified and content hashes, not URL hashes;
- robots.txt is used only for sitemap discovery, not access-policy enforcement;
- crawled concepts are heading-based, not semantically inferred;
- automatic relationships/knowledge-graph behavior are not implemented;
- Confluence/SharePoint authentication and ACL-aware retrieval are not implemented;
- filesystem keyword search is not a million-document search architecture;
- UI job updates are polling, not true streaming;
- XML and RMarkdown uploads are not currently supported.

These distinctions make the future presentation more accurate and defensible: demonstrate what the code does today, label PoC constraints explicitly, and present enterprise connectors, security, large-scale lexical indexing, and relationship extraction as the next engineering phase.
