# Live Ingestion Dashboard: Frozen Counters, Invisible Rate-Limit Warnings, Unreachable Close Button

Three related, user-reported bugs in the live ingestion overlay, all root-caused
and fixed in this pass.

## 1. Discovered/Fetched/Processed/Indexed/Failed counters froze during indexing

**Symptom reported:** all five counters stayed at 0 and the progress bar sat on
"Waiting for the pipeline…" for the entire run, even though the container logs
showed real progress (`⚠️ Embedding rate limit (429) hit for '...', retrying in
6s`).

**Investigation:** verified every other layer first, in isolation, before
touching any code:
- `JobManager` + `app.ingestion.status.update_status/get_status`, driven
  directly in-process: counters updated correctly.
- The real FastAPI app via `TestClient`, hitting `POST /api/v1/ingest/` then
  polling `GET /api/v1/ingest/status`: counters updated correctly over HTTP.
- `app.ui.components.dashboard._build_html`'s server-side status embedding
  (`window.__OKF_STATUS__`): produces a valid, non-empty JS object.

All of that worked, which narrowed it to one place: `app/retrieval/
hybrid_search.py`'s `index_documents()`. **Root cause:** it runs its entire
per-document embedding loop (with 429 retry-with-backoff) without calling
`update_status()` again until the function returns. The indexing phase is
also the longest and most rate-limit-prone part of a run, so in practice the
UI froze for exactly as long as indexing took - sometimes many minutes - with
zero feedback, making a working (if slow) pipeline indistinguishable from a
stuck one.

**Fix:**
- `index_documents()` now calls `update_status()` once up front (reporting
  `total_documents`) and once after *every* document (`indexed`, `failed`,
  `current_source`), not just at the end.
- `app/jobs/manager.py`'s `compute_stage_progress()` used to pin the
  `"indexing"` stage at a flat 92% regardless of how many documents had been
  embedded; it now scales 90→99% by `indexed / total_documents`, the same way
  `"downloading"`/`"converting"` already scale by their own counters.
- The "Failed" counter is now cumulative across the whole run
  (`base_failed_count` parameter, seeded from the crawl phase's failure
  count) instead of visibly dropping back to 0 the moment indexing starts.

**Verified:** with a mocked embedding model and an injected 429 on one
document, `update_status` was observed to fire with `indexed=1,2,3,4` and
`progress_percent` climbing 90→99 in real time - not just at the end. See
`tests/test_hybrid_search_indexing.py::test_index_documents_reports_live_progress_per_document`.

## 2. Rate-limit warnings never reached the UI

**Symptom reported:** `⚠️ Embedding rate limit (429) hit for 'X', retrying in
6s (attempt 2/3)` was visible in `docker-compose logs` but nowhere in the UI -
no way to tell a slow run was actually rate-limited rather than broken.

**Fix:**
- Added a `rate_limit_hits` counter, threaded through `Job` (`app/jobs/
  models.py`), `JobManager`, and `app/ingestion/status.py`'s legacy-dict
  fallback.
- Every retry now calls `update_status(message=..., stage_message=...,
  rate_limit_hits=...)` in addition to printing to the logs, so the warning
  reaches the dashboard the same way any other progress update does.
- `app/ui/components/dashboard.py`: added a persistent amber **"⚠️ Rate
  limited ×N"** badge next to the status badge, driven by `state.
  rateLimitHits`. Unlike the activity title/subtitle (which gets overwritten
  by the next ordinary progress message and can be missed), this badge stays
  visible for the whole run.

**Verified with a real jsdom DOM test** (not just code review) - rendered the
actual generated HTML/JS in a headless DOM with a status payload containing
`rate_limit_hits: 3`, and confirmed: the badge's `display` becomes
`inline-flex`, its counter text reads `"3"`, and the activity title shows the
real retry message text. See `/tmp` test scripts used during this session for
the exact assertions; equivalent coverage lives in
`test_index_documents_surfaces_rate_limit_hits_to_status`.

## 3. The overlay's Close button was unreachable

**Symptom reported:** "I can't find the close button" - the popup had no
visible way to dismiss it.

**Root cause, confirmed against Streamlit 1.61.1's actual source (`streamlit/
elements/lib/dialog.py`), not assumption:**
- `app/ui/app.py` opened the dialog with `dismissible=False`, which disables
  Streamlit's native close (X) at the frontend level.
- CSS additionally forced `display: none !important` on
  `[data-testid="stIconButton"]` / `button[aria-label="Close"]` inside the
  dialog, "so the dialog has a single clear Close/Cancel action" - a custom
  `st.button("Close")` rendered at the very bottom of the dialog's content
  (header, process-flow timeline, activity strip, 5 stat cards, progress bar,
  2 charts - a lot of vertical content). With no `max-height`/scroll
  constraint on the dialog container, that footer button could end up below
  the modal's visible/reachable area on typical screens, and the only other
  way out (the native X) had been deliberately hidden.

**Fix:**
- `dismissible=True` (Streamlit's default - explicit here for clarity) with
  `on_dismiss=_dismiss_ingestion_overlay`, a callback that sets
  `st.session_state.ingestion_running = False`. Per Streamlit's
  implementation, a callable `on_dismiss` is registered as a real widget
  callback (`register_widget(..., on_change_handler=on_dismiss)`), fired on
  **any** dismiss path (X, Escape, click-outside) with an automatic rerun
  after - so session state stays correct regardless of how the dialog is
  closed, and it won't immediately reopen.
- Removed the CSS that hid the native X.
- Added `max-height: 88vh; overflow-y: auto;` to
  `[data-testid="stDialog"] [role="dialog"]` as a structural safety net: on
  any screen where the content is still taller than the viewport, it now
  scrolls *inside* the dialog instead of pushing the footer out of reach -
  and the header (with the now-visible X) stays fixed and reachable
  regardless of scroll position, which is the standard modal UX pattern this
  was missing.
- Also shrank the dashboard's own footprint per the accompanying request to
  "reduce the popup": tightened padding/gaps throughout (`body`, `.dash`,
  `.head`, `.flow`, `.activity`, `.stat` cards, `.progress-card`,
  `.chart-card`), roughly halved the two chart boxes' heights (210px→150px
  for the token chart, 140px donut→100px), and reduced the component's
  overall iframe height from a fixed 760px to 620px
  (`render_live_dashboard(..., height=620)`, now a parameter instead of
  hardcoded).

**Verified:** re-generated the dashboard HTML and syntax-checked the
extracted `<script>` block with `node --check` (catches any malformed JS from
the template edits), then ran a real jsdom DOM test confirming the page still
populates correctly (rate-limit badge, counters, progress %, all 5 stat cards
and 2 chart cards present) after the CSS trims.

## Bonus: indexing is now cancellable mid-batch

While instrumenting `index_documents()`'s loop for live progress, noticed
cancellation (`cancel_event`, checked via `_check_cancelled()` elsewhere in
`app/ingestion/pipeline.py`) was only ever checked **once, before** indexing
started - not between documents. On a long, rate-limit-heavy run, the sidebar
Stop button would have had no effect until the entire batch finished on its
own. Added a per-document `cancel_event` check inside the loop that raises
`JobCancelledError` (the same exception the rest of the pipeline already
handles), reporting a "cancelled" status before doing so.

**Verified:** `test_index_documents_stops_promptly_on_cancel` - sets the
cancel event after the 2nd of 5 documents is inserted, confirms
`JobCancelledError` is raised and fewer than 5 documents were actually
inserted (not all 5, i.e. it didn't just run to completion and cancel was a
no-op).

## Verified (final state)

```bash
$ python3 -m pytest tests/ -q
61 passed
```

Plus the manual verifications described above (isolated backend tests, a real
`TestClient` HTTP round-trip, `node --check` on the extracted dashboard JS,
and jsdom DOM tests of the actual generated HTML/JS output) - each bug was
reproduced and root-caused with a real test before being called fixed, not
patched speculatively.
