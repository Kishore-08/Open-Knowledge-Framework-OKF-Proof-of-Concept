# Senior Review Follow-up: Repository Integrity, Duplicate Code, Test Suite, Ingestion Resilience

This follow-up review picks up where `ISSUE_RESOLUTION.md` left off. That
document fixed *ranking* behavior, but the delivered project itself was in a
broken state independent of ranking, and the root cause of the incomplete
Qdrant index it names as a "known limitation" was never actually fixed. Below
is everything found and fixed in this pass.

## 1. Critical: the live `knowledge/` directory was almost empty

**Symptom:** `app/core/config.py` sets `KNOWLEDGE_DIR = "knowledge"`, and
`docker-compose.yml` only mounts `./knowledge` into the containers. That is
the *only* directory the running app ever reads. As delivered, `knowledge/`
contained just **4** concept files (linux, apache, langchain) - zero
Kubernetes concepts - while the real 644 Kubernetes/tutorial/reference
concept files produced by the ingestion pipeline were still sitting in the
**old** `data/knowledge/` path from before a migration
(`scripts/migrate_data_structure.py`) was apparently run partway and never
completed.

**Effect:** every "what is X" style query in this deliverable would fail with
"I cannot answer this based on the OKF knowledge base" - not because of the
ranking bug `ISSUE_RESOLUTION.md` describes, but because there was
essentially no Kubernetes content for the app to find in the first place.

**Fix:** merged all 644 `data/knowledge/**/*.md` files into `knowledge/`
(verified zero filename collisions and that every file has valid YAML
frontmatter first). `knowledge/` now has 648 concepts and reproduces the
"Overview" top-result behavior documented in `ISSUE_RESOLUTION.md` for
"What is Kubernetes?". The old `data/` directory (fully redundant with
`cache/` for raw files, and now redundant with `knowledge/` for concepts) was
archived under `backups/data_dir_deprecated_<timestamp>/` rather than
deleted outright.

## 2. Duplicate function definitions in `app/okf/repository.py`

`search_concepts()` and `knowledge_stats()` were each defined **twice** in
the same file. The first `search_concepts` was a dead stub (docstring only,
implicitly returned `None`); the first `knowledge_stats` was an incomplete
earlier version. Python silently used the later definitions, so this never
raised an error, but it's exactly the kind of copy-paste-during-a-patch
artifact that turns into a real bug the next time someone edits "the"
function and edits the wrong copy. Removed the dead block.

## 3. `LLM_FALLBACK_MODEL` provided no actual fallback

`app/core/config.py` set `LLM_FALLBACK_MODEL` to the **same value** as
`LLM_MODEL`. `app/core/gemini_llm.complete()` also de-dupes identical model
names via a `seen` set before trying them, so the "fallback" path could never
fire - there was no real resilience against quota exhaustion despite the
retry machinery being built for it. Changed `LLM_FALLBACK_MODEL` to a
distinct model (`gemini-2.0-flash-lite`); verify against Gemini's current
model list for your account/quota tier before relying on it in production.

## 4. `.gitignore` was stale relative to the current architecture

It still ignored the *old* `data/raw/*` and `knowledge/*` paths - the
opposite of what the README's "Data Organization" section says post-
migration (`knowledge/` must be committed, `cache/` must be ignored). This is
exactly the kind of drift that produced issue #1 above and would keep
recreating it after every fresh clone. Rewritten to match the current
cache/ vs knowledge/ architecture, and extended to also ignore `backups/`
and `.venv-eval/` (a 926MB virtualenv was bundled directly into the
deliverable zip - it must never be committed; recreate it with
`pip install -r requirements/eval.txt`). Removed from this deliverable.

## 5. Root cause of the incomplete Qdrant index (only 79/874 docs) was never fixed

`ISSUE_RESOLUTION.md` treats "Qdrant Index Incomplete" as a known limitation
and compensates for it with ranking heuristics (5x boost for "overview"
titles, 3x boost for "X is a ..." descriptions, special-casing "what is/are"
queries). That's a symptom patch, and it overfits to the Kubernetes demo.

The actual root cause: `app/query/engine.py` (answer generation) has proper
429/quota retry-with-backoff around every Gemini call, but
`app/retrieval/hybrid_search.py:index_documents()` (embedding + indexing)
had **none** - it called `VectorStoreIndex.from_documents(documents, ...)`
once for the entire batch, so the *first* 429 anywhere in a run of hundreds
of documents raised and aborted everything after it. That asymmetry is why
indexing silently stopped at 79/874 documents while answer generation kept
working.

**Fix:**
- Added `app/core/retry.py`: a small shared `retry_with_backoff()` /
  `is_retryable_429()` used by *both* answer generation and indexing now,
  instead of engine.py's private duplicate.
- Rewrote `index_documents()` to build an empty `VectorStoreIndex` and then
  `index.insert(doc, ...)` one document at a time, each call wrapped in the
  same retry-with-backoff policy used for answer generation. A document that
  still fails after retries is skipped and reported (not aborting the rest
  of the batch), and the function now returns `(index, failed_ids)` so
  callers can log/retry the specific failures. Updated both callers
  (`app/ingestion/pipeline.py`, `app/indexing/indexer.py`) for the new
  return shape and to surface `failed_ids` in their status/result output.
- Added `tests/test_retry.py` covering the retry/backoff policy directly
  (transient-429-then-success, exhausted-retries, non-429-fails-fast).

This is slower per-document than a single batched call, but on a free-tier
API the previous "batch everything, abort on first 429" behavior was not
actually faster - it just failed silently after ~9% of the corpus.

## 6. The unit test suite could not run at all

`tests/test_crawler.py` was not a test - it was a sequence of bare
module-level `assert` statements referencing an undefined `result` variable.
This raised a `NameError` during pytest **collection**, which aborts the
entire run: no test in the whole `tests/` package (not just `test_crawler`)
was ever actually executing, silently. Rewrote it as real
`async def test_...()` functions using a mocked HTTP layer (no real network
calls) covering new/unchanged/changed/deleted/failed crawl outcomes.
`pytest-asyncio` was also missing from `requirements/dev.txt` (needed to run
async tests at all) and there was no `pytest.ini` configuring it - both
added.

Separately, 4 of 8 tests in `tests/test_repository.py` were failing even
before this pass: they hardcoded assumptions about "seed" concepts
(`k8s-deployment`, `k8s-service`, `k8s-pod`, a `networking` tag) that were
never actually present anywhere in this deliverable - not in
`data/knowledge/`, not in `knowledge/`. Rewrote those four tests to build
their own tiny, deterministic fixture repository under `tmp_path` (matching
the pattern already used by the file's own
`test_pipeline_written_okf_roundtrips_through_repository`), instead of
depending on the real, mutable, 600+-document ingested corpus.

**Full suite now: 35/35 passing** (up from a suite that couldn't even be
collected).

## 7. `index.insert()` regression from the fix in §5 (found post-deploy)

After deploying the §5 fix, ingestion logs showed every single document
failing:

```
❌ Failed to index 'kubernetes-what-s-next-5445bee6' after retries, skipping:
run_transformations() got multiple values for argument 'transformations'
```

**Cause:** `index_documents()` constructs
`VectorStoreIndex(nodes=[], storage_context=storage_context,
transformations=[splitter])`, which stores `splitter` on the index as
`self._transformations`. `BaseIndex.insert()` already forwards
`self._transformations` positionally into `run_transformations(...)`
internally - so the `transformations=[splitter]` kwarg I additionally passed
into `index.insert(doc, transformations=[splitter])` collided with it. This
made every document fail (worse than the original no-retry bug, since 100%
failed instead of ~91%), and the per-document `except Exception` handling
caught it silently rather than surfacing a code bug.

**Fix:** removed the redundant `transformations=[splitter]` argument from
the `index.insert(doc)` call - the index already has it from construction.

**Verified:**
- Reproduced the exact call chain with `MockEmbedding` (no network calls),
  confirmed `index.insert(doc)` now succeeds.
- Added `tests/test_hybrid_search_indexing.py`, which drives the real
  `index_documents()` end-to-end (mocking only the Qdrant vector store and
  Gemini embedding, both swapped for in-memory/deterministic equivalents).
  Confirmed this test fails with the exact reported error message when the
  bug is reintroduced, and passes with the fix.
- Full suite: **36/36 passing.**

## 8. Score-scale inconsistency between keyword and semantic search

Keyword search scores (`app.okf.repository.search_concepts`) were an
unbounded sum of weighted token-hit counts, then optionally multiplied by up
to 15x for definition-style queries ("what is X") — production values of
`27.0` and `135.0` were observed for the same query. Semantic search
(`app.query.search._semantic_search`) reports cosine similarity, always
`0.0-1.0`. Both lists get merged in `app.query.search.search()` (mode=
`"auto"`) and are exposed verbatim via the API's `Citation.score` field,
documented as *"The retrieval relevance score (0.0 to 1.0)"* — so a raw
keyword score leaking through both violated that documented contract and
made keyword vs. semantic hits visually incomparable to any API consumer
(e.g. a UI trying to show a relevance bar).

**Fix:** added `_normalize_keyword_score()` in `app/okf/repository.py`,
squashing the raw score into `[0.0, 1.0)` via `score / (score + K)`. This
transform is monotonic, so it does not change result ordering (still sorted
by the pre-normalization raw score's relative order) — it only rescales the
reported number. `K = 8.0` was chosen so a solid single-field keyword match
(score ≈ 4–6) lands in a similar range to a good semantic match (~0.5–0.7)
rather than always looking artificially weak next to it.

**Verified:** re-ran the "What is Kubernetes?" query — ranking is unchanged
("Overview" is still the top result) and every score is now in `[0.0, 1.0)`
(e.g. `0.944`, `0.849`, `0.833` instead of raw values in the hundreds). Added
`test_search_concepts_score_is_normalized` in `tests/test_repository.py`,
covering both a plain query and a definition-style (max-boost) query.

## 9. Dead LlamaIndex query-engine path — already removed, no action needed

`app/api/routers/query.py`'s own module docstring claims *"This removes the
old duplicate LlamaIndex query-engine path
(`app.retrieval.query_engine.get_query_engine`)"*. Checked: that function no
longer exists anywhere in the codebase (`grep -rn "get_query_engine" app`
only matches this one docstring comment). `app/retrieval/query_engine.py`
still exists, but only contains `configure_llm_settings()`, which *is*
actively used elsewhere (`app/ingestion/pipeline.py`,
`app/indexing/indexer.py`, `app/query/search.py`) to configure the shared
LlamaIndex `Settings.llm`/`Settings.embed_model` used for semantic search's
retriever. So there is no dead code left here — this item is already
resolved and required no change.

## Verified (final state, all fixes in this document)

```bash
$ python3 -m pytest tests/ -q
37 passed in ~5s
```

```python
>>> from app.okf.repository import load_all_concepts, search_concepts
>>> len(load_all_concepts())
648
>>> results = search_concepts("What is Kubernetes?")
>>> results[0]["title"], results[0]["score"]
('Overview', 0.944)
>>> all(0.0 <= r["score"] < 1.0 for r in results)
True
```

## Still open (flagged, not fixed in this pass)

- **Logging**: 59 bare `print()` calls across `app/` instead of the
  `logging` module - fine for a PoC, worth addressing before this goes
  beyond that.
- No CI configured to actually run `pytest tests/` on push/PR, which is how
  the broken test suite (§6) went unnoticed for as long as it did.
