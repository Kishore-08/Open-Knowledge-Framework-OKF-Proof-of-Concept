"""
Self-contained live ingestion dashboard.

Rendered as a Streamlit HTML component so the counters, progress bar, process
flow and charts animate smoothly in the browser instead of re-rendering on every
Streamlit rerun. The component eases every number toward its target one step at
a time (+1 increments), which is what makes the "live progress" feel smooth.

Process flow
------------
The dashboard renders a horizontal stage timeline that mirrors the real
architecture: source selection -> discovering docs -> downloading from the
official website -> storing raw data in the cache folder -> running the
ingestion pipeline from cache -> OKF knowledge files -> indexed into Qdrant.
The backend reports the current ``stage`` (see ``app.ingestion.status``) and the
component highlights the matching step.

Data flow
---------
The Streamlit server fetches ``/api/v1/ingest/status`` itself and embeds the
result into the component on every rerun (see ``render_live_dashboard``). This
means the counters update even when the browser cannot reach the API directly
(e.g. when the app is served through a preview domain and ``API_HOST`` is a
docker-internal host). The component additionally tries to poll the API from
the browser as an enhancement, but never relies on it.
"""

import html as _html
import json as _json
from typing import Optional

import streamlit as st


def browser_api_base(configured: str) -> str:
    """
    Return the API base URL that the *browser* can actually reach.

    ``API_HOST`` may point at the docker-internal name (``http://api:8000``)
    which the browser cannot resolve. In that case fall back to the host the
    UI page is served from, on the same port.
    """
    import urllib.parse

    try:
        parsed = urllib.parse.urlparse(configured)
        host = parsed.hostname or ""
        if host in ("api", "localhost", "127.0.0.1", "0.0.0.0", ""):
            return f"http://localhost:{parsed.port or 8000}"
        return configured
    except Exception:
        return "http://localhost:8000"


def _build_html(api_base: str, theme: str = "light", initial_status: Optional[dict] = None) -> str:
    """Build the full self-contained HTML+JS dashboard.

    ``initial_status`` is embedded as ``window.__OKF_STATUS__`` and applied
    immediately, so the counters reflect the server-side status on every
    Streamlit rerun even if the browser cannot reach the API.
    """

    # Escape for embedding in a <script> string safely.
    api_base_js = _html.escape(api_base, quote=True)

    # Embed the server-side status as a raw JS object literal. HTML-entity
    # escaping would corrupt the JSON (quotes become &quot;), so we only guard
    # against breaking out of the <script> block via "</script>".
    status_json = _json.dumps(initial_status or {})
    status_js = status_json.replace("</", "<\\/")

    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', -apple-system, 'Segoe UI', Roboto, sans-serif; }

    :root {
        --accent: #4285f4;
        --accent-2: #1a73e8;
        --accent-3: #34a853;
        --success: #10b981;
        --warn: #f59e0b;
        --danger: #ef4444;
    }

    body[data-theme="dark"] {
        --text: #e2e8f0;
        --text-dim: #94a3b8;
        --glass-bg: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 255, 255, 0.12);
        --glass-shadow: rgba(0, 0, 0, 0.35);
        --axis-line: rgba(255,255,255,0.15);
        --axis-label: #64748b;
        --split-line: rgba(255,255,255,0.07);
        --bar-track: rgba(255,255,255,0.08);
        --donut-center: rgba(11,16,32,0.9);
        --donut-border: #0b1020;
        --badge-bg: rgba(255,255,255,0.06);
        --badge-border: rgba(255,255,255,0.14);
        --track-line: rgba(255,255,255,0.16);
        --step-ico: rgba(255,255,255,0.05);
        --body-bg:
            radial-gradient(900px 400px at 10% -10%, rgba(66, 133, 244, 0.28), transparent 60%),
            radial-gradient(700px 400px at 110% 0%, rgba(52, 168, 83, 0.14), transparent 55%),
            radial-gradient(600px 500px at 50% 120%, rgba(251, 188, 5, 0.12), transparent 60%),
            #0b1020;
    }

    body[data-theme="light"] {
        --text: #1f2937;
        --text-dim: #5f6368;
        --glass-bg: rgba(255, 255, 255, 0.78);
        --glass-border: rgba(15,23,42,0.10);
        --glass-shadow: rgba(60, 64, 67, 0.12);
        --axis-line: rgba(15,23,42,0.15);
        --axis-label: #9aa0a6;
        --split-line: rgba(15,23,42,0.07);
        --bar-track: rgba(15,23,42,0.08);
        --donut-center: rgba(255,255,255,0.95);
        --donut-border: #ffffff;
        --badge-bg: rgba(255,255,255,0.9);
        --badge-border: rgba(15,23,42,0.12);
        --track-line: rgba(66,133,244,0.25);
        --step-ico: rgba(66,133,244,0.08);
        --body-bg:
            radial-gradient(900px 400px at 10% -10%, rgba(66,133,244,0.12), transparent 60%),
            radial-gradient(700px 400px at 110% 0%, rgba(52,168,83,0.06), transparent 55%),
            radial-gradient(600px 500px at 50% 120%, rgba(251,188,5,0.07), transparent 60%),
            #f2f5fc;
    }

    body {
        min-height: 100%;
        padding: 12px;
        background: var(--body-bg);
        color: var(--text);
    }

    .glass {
        background: var(--glass-bg);
        backdrop-filter: blur(18px) saturate(140%);
        -webkit-backdrop-filter: blur(18px) saturate(140%);
        border: 1px solid var(--glass-border);
        border-radius: 20px;
        box-shadow: 0 8px 32px var(--glass-shadow);
    }

    .dash {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 18px;
    }

    .head h2 {
        font-size: 1.15rem;
        font-weight: 700;
        letter-spacing: 0.01em;
        background: linear-gradient(90deg, var(--text), var(--accent-2));
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        border: 1px solid var(--badge-border);
        background: var(--badge-bg);
        color: var(--text);
    }
    .badge .dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #64748b;
    }
    .badge.running .dot { background: var(--accent); animation: pulse 1.4s infinite; }
    .badge.completed .dot { background: var(--success); }
    .badge.failed .dot { background: var(--danger); }
    .badge.warn {
        color: var(--warn);
        border-color: rgba(245, 158, 11, 0.45);
        background: rgba(245, 158, 11, 0.12);
        animation: warnPulse 1.6s infinite;
    }
    .badge.warn .dot { background: var(--warn); }
    @keyframes warnPulse {
        0% { box-shadow: 0 0 0 0 rgba(245,158,11,0.45); }
        70% { box-shadow: 0 0 0 7px rgba(245,158,11,0); }
        100% { box-shadow: 0 0 0 0 rgba(245,158,11,0); }
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(66,133,244,0.7); }
        70% { box-shadow: 0 0 0 8px rgba(66,133,244,0); }
        100% { box-shadow: 0 0 0 0 rgba(66,133,244,0); }
    }

    /* ---- Process flow timeline ---- */
    .flow { padding: 14px 14px 10px; }
    .flow-head {
        display: flex; justify-content: space-between; align-items: baseline;
        margin-bottom: 10px; padding: 0 4px;
    }
    .flow-head .ttl {
        font-size: 0.85rem; font-weight: 700; color: var(--text);
    }
    .flow-head .live-note {
        font-size: 0.72rem; color: var(--accent); font-weight: 600;
        display: inline-flex; align-items: center; gap: 6px;
    }
    .flow-head .live-note .ldot {
        width: 7px; height: 7px; border-radius: 50%; background: var(--accent);
        animation: pulse 1.4s infinite;
    }
    .steps {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        position: relative;
        padding-top: 4px;
    }
    .steps::before {
        content: "";
        position: absolute;
        top: 22px; left: 7%; right: 7%;
        height: 2px;
        background: var(--split-line);
        z-index: 0;
    }
    .steps .track {
        position: absolute;
        top: 22px; left: 7%;
        height: 2px;
        width: 0%;
        background: linear-gradient(90deg, var(--accent), var(--accent-2));
        box-shadow: 0 0 8px rgba(66,133,244,0.6);
        z-index: 0;
        transition: width 0.45s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .step {
        flex: 1;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        position: relative;
        z-index: 1;
        text-align: center;
        min-width: 0;
    }
    .step .ico {
        width: 44px; height: 44px;
        border-radius: 50%;
        display: grid; place-items: center;
        font-size: 17px;
        background: var(--step-ico);
        border: 2px solid var(--split-line);
        color: var(--text-dim);
        transition: all 0.3s ease;
    }
    .step .lbl {
        font-size: 0.68rem;
        font-weight: 600;
        color: var(--text-dim);
        text-transform: uppercase;
        letter-spacing: 0.03em;
        white-space: nowrap;
        transition: color 0.3s ease;
    }
    .step .desc {
        font-size: 0.66rem;
        color: var(--text-dim);
        opacity: 0;
        max-height: 0;
        overflow: hidden;
        transition: opacity 0.3s ease, max-height 0.3s ease;
        line-height: 1.35;
        max-width: 110px;
    }
    .step.active .ico {
        border-color: var(--accent);
        background: var(--accent);
        color: #fff;
        box-shadow: 0 0 0 5px rgba(66,133,244,0.15), 0 0 18px rgba(66,133,244,0.5);
        animation: pulse 1.6s infinite;
        transform: scale(1.08);
    }
    .step.active .lbl { color: var(--accent); }
    .step.active .desc { opacity: 1; max-height: 3em; }
    .step.done .ico {
        background: var(--success);
        border-color: var(--success);
        color: #fff;
    }
    .step.done .lbl { color: var(--success); }
    .step.error .ico {
        background: var(--danger);
        border-color: var(--danger);
        color: #fff;
        animation: none;
    }
    .step.error .lbl { color: var(--danger); }

    @media (max-width: 760px) {
        .step .desc { display: none; }
        .step .lbl { font-size: 0.6rem; }
        .step .ico { width: 36px; height: 36px; font-size: 14px; }
        .steps::before, .steps .track { top: 18px; }
    }

    /* ---- Current activity strip ---- */
    .activity {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 10px 16px;
    }
    .activity .act-ico {
        width: 34px; height: 34px;
        border-radius: 10px;
        flex-shrink: 0;
        display: grid; place-items: center;
        font-size: 16px;
        background: rgba(66,133,244,0.14);
        color: var(--accent);
    }
    .activity .act-body { min-width: 0; }
    .activity .act-title {
        font-size: 0.9rem; font-weight: 650; color: var(--text);
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    .activity .act-sub {
        font-size: 0.74rem; color: var(--text-dim); margin-top: 2px;
        white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }

    /* ---- Stat cards ---- */
    .cards {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
    }
    @media (max-width: 900px) { .cards { grid-template-columns: repeat(2, 1fr); } }

    .stat {
        padding: 10px 12px;
        display: flex;
        flex-direction: column;
        gap: 4px;
        position: relative;
        overflow: hidden;
    }
    .stat::after {
        content: "";
        position: absolute;
        inset: 0;
        background: radial-gradient(120px 90px at 20% 0%, var(--c, var(--accent)), transparent 70%);
        opacity: 0.22;
        pointer-events: none;
    }
    .stat .ico {
        width: 26px; height: 26px;
        border-radius: 8px;
        display: grid; place-items: center;
        font-size: 13px;
        background: color-mix(in srgb, var(--c, var(--accent)) 18%, transparent);
        color: var(--c, var(--accent));
    }
    .stat .num {
        font-size: 1.4rem;
        font-weight: 750;
        font-variant-numeric: tabular-nums;
        line-height: 1;
        color: var(--text);
    }
    .stat .lbl {
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 0.09em;
        color: var(--text-dim);
    }

    .progress-card { padding: 12px 16px; }
    .progress-top {
        display: flex; justify-content: space-between; align-items: baseline;
        margin-bottom: 10px;
    }
    .progress-top .ttl {
        font-size: 0.85rem; font-weight: 600; color: var(--text-dim);
    }
    .progress-top .pct {
        font-size: 1.5rem; font-weight: 750; font-variant-numeric: tabular-nums;
        background: linear-gradient(90deg, var(--accent), var(--accent-2));
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .bar { height: 12px; border-radius: 999px; background: var(--bar-track); overflow: hidden; position: relative; }
    .bar .fill {
        height: 100%; width: 0%;
        border-radius: 999px;
        background: linear-gradient(90deg, var(--accent), var(--accent-2), var(--success));
        background-size: 200% 100%;
        animation: slide 2.5s linear infinite;
        transition: width 0.35s cubic-bezier(0.22, 1, 0.36, 1);
    }
    @keyframes slide { from { background-position: 0% 0; } to { background-position: 200% 0; } }
    .progress-sub { margin-top: 8px; font-size: 0.78rem; color: var(--text-dim); }

    .charts {
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 12px;
    }
    @media (max-width: 900px) { .charts { grid-template-columns: 1fr; } }
    .chart-card { padding: 10px 14px; }
    .chart-card h3 {
        font-size: 0.82rem; font-weight: 600; color: var(--text-dim);
        margin-bottom: 4px;
    }
    .chart-box { width: 100%; height: 150px; position: relative; }
    .chart-note {
        font-size: 0.75rem; color: var(--text-dim); padding: 8px;
        text-align: center;
    }

    .token-line {
        display: flex; gap: 14px; align-items: flex-end; height: 110px;
        padding: 8px 4px 0;
    }
    .token-line .col {
        flex: 1; display: flex; flex-direction: column; justify-content: flex-end;
        gap: 4px; text-align: center;
    }
    .token-line .col .v {
        font-size: 0.72rem; color: var(--text-dim);
        font-variant-numeric: tabular-nums;
    }
    .token-line .col .seg {
        border-radius: 6px 6px 2px 2px;
        transition: height 0.4s cubic-bezier(0.22, 1, 0.36, 1);
    }
    .token-line .col .seg.prompt { background: linear-gradient(180deg, var(--accent), var(--accent-2)); }
    .token-line .col .seg.completion { background: linear-gradient(180deg, #34a853, #1e8e3e); }
    .token-line .col .lbl {
        font-size: 0.65rem; color: var(--text-dim); text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .donut-wrap {
        display: flex; align-items: center; justify-content: center;
        flex-direction: column; gap: 6px; height: 110px;
    }
    .donut { width: 100px; height: 100px; border-radius: 50%; position: relative; }
    .donut .center {
        position: absolute; inset: 16px; border-radius: 50%;
        display: grid; place-items: center;
        font-size: 1.2rem; font-weight: 700;
        background: var(--donut-center);
        color: var(--text);
    }
    .legend { display: flex; gap: 14px; flex-wrap: wrap; font-size: 0.72rem; color: var(--text-dim); }
    .legend span { display: inline-flex; align-items: center; gap: 6px; }
    .legend i { width: 10px; height: 10px; border-radius: 3px; display: inline-block; }
</style>
</head>
<body data-theme="__THEME__">
<div class="dash">

    <div class="glass head">
        <h2>Ingestion Pipeline</h2>
        <div style="display:flex; align-items:center; gap:8px;">
            <span class="badge warn" id="rateLimitBadge" style="display:none;" title="Gemini's embedding API is rate-limiting this run; documents are being retried with backoff instead of dropped.">
                <span class="dot"></span>
                <span>Rate limited &times;<span id="rateLimitCount">0</span></span>
            </span>
            <span class="badge running" id="statusBadge">
                <span class="dot"></span>
                <span id="statusText">Connecting&hellip;</span>
            </span>
        </div>
    </div>

    <!-- Process flow timeline -->
    <div class="glass flow">
        <div class="flow-head">
            <span class="ttl">Process Flow</span>
            <span class="live-note" id="liveNote"><span class="ldot"></span><span id="liveNoteText">Live</span></span>
        </div>
        <div class="steps" id="steps">
            <div class="track" id="flowTrack"></div>
        </div>
    </div>

    <!-- Current activity -->
    <div class="glass activity">
        <div class="act-ico" id="actIco">&#9881;&#65039;</div>
        <div class="act-body">
            <div class="act-title" id="actTitle">Waiting for the pipeline&hellip;</div>
            <div class="act-sub" id="actSub">Select a source and trigger ingestion to begin.</div>
        </div>
    </div>

    <div class="cards" id="cards">
        <div class="stat glass" style="--c:#4285f4;">
            <div class="ico">&#128269;</div>
            <div class="num" id="discovered">0</div>
            <div class="lbl">Discovered</div>
        </div>
        <div class="stat glass" style="--c:#a78bfa;">
            <div class="ico">&#128229;</div>
            <div class="num" id="fetched">0</div>
            <div class="lbl">Fetched</div>
        </div>
        <div class="stat glass" style="--c:#10b981;">
            <div class="ico">&#9881;&#65039;</div>
            <div class="num" id="processed">0</div>
            <div class="lbl">Processed</div>
        </div>
        <div class="stat glass" style="--c:#f59e0b;">
            <div class="ico">&#128451;</div>
            <div class="num" id="indexed">0</div>
            <div class="lbl">Indexed</div>
        </div>
        <div class="stat glass" style="--c:#ef4444;">
            <div class="ico">&#9888;&#65039;</div>
            <div class="num" id="failed">0</div>
            <div class="lbl">Failed</div>
        </div>
    </div>

    <div class="glass progress-card">
        <div class="progress-top">
            <span class="ttl">Live Progress</span>
            <span class="pct" id="pct">0%</span>
        </div>
        <div class="bar"><div class="fill" id="barFill"></div></div>
        <div class="progress-sub" id="progressSub">Waiting for the pipeline&hellip;</div>
    </div>

    <div class="charts">
        <div class="glass chart-card">
            <h3>Token Consumption Estimate</h3>
            <div class="chart-box" id="tokenBox">
                <div class="chart-note">Loading charts&hellip;</div>
            </div>
        </div>
        <div class="glass chart-card">
            <h3>Pipeline Mix</h3>
            <div class="donut-wrap" id="mixBox">
                <div class="donut" id="donut"><div class="center" id="donutCenter">0%</div></div>
                <div class="legend" id="mixLegend"></div>
            </div>
        </div>
    </div>

</div>

<script src="https://cdn.jsdelivr.net/npm/echarts@5.5.0/dist/echarts.min.js"></script>
<script>
(function () {
    const API_BASE = "__API_BASE_JS__";
    const THEME = document.body.dataset.theme || "light";
    // Server-side status embedded on every Streamlit rerun. This is the primary
    // source of truth so the counters move even when the browser cannot reach
    // the API directly.
    const INITIAL = window.__OKF_STATUS__ || null;
    const EMBEDDED = !!(INITIAL && Object.keys(INITIAL).length);
    let echartsReady = false;

    // ---- process flow definition (mirrors the real architecture) ----
    const STEPS = [
        { key: "starting",    label: "Source",          icon: "🎯", desc: "Sources selected" },
        { key: "discovering", label: "Discover",        icon: "🧭", desc: "Scanning official docs" },
        { key: "downloading", label: "Download",        icon: "⬇️", desc: "Fetching pages from the web" },
        { key: "cached",      label: "Cache",           icon: "🗄️", desc: "Raw data stored in cache" },
        { key: "converting",  label: "Ingest \u2192 OKF", icon: "🔄", desc: "Ingestion pipeline running" },
        { key: "indexing",    label: "Index",           icon: "📊", desc: "Indexing into Qdrant" },
        { key: "completed",   label: "Done",            icon: "✅", desc: "Ingestion complete" },
    ];

    const STAGE_INDEX = {
        queued: 0, starting: 0, pending: 0,
        discovering: 1,
        downloading: 2,
        cached: 3,
        converting: 4, formatting: 4,
        indexing: 5,
        completed: 6, success: 6,
    };

    const STAGE_COPY = {
        starting:    ["⚙️", "Initializing the pipeline", "Preparing the ingestion pipeline"],
        discovering: ["🧭", "Discovering documentation", "Scanning official websites for pages"],
        downloading: ["⬇️", "Downloading from official website", "Fetching documentation pages into the cache folder"],
        cached:      ["🗄️", "Stored in cache", "Raw data cached \u2014 starting the ingestion pipeline from cache"],
        converting:  ["🔄", "Ingestion pipeline running", "Converting cached raw data into OKF knowledge files"],
        formatting:  ["🔄", "Formatting OKF knowledge", "Extracting metadata \u00B7 writing OKF knowledge files"],
        indexing:    ["📊", "Indexing knowledge", "Storing vectors into Qdrant"],
        completed:   ["✅", "Completed", "All documents indexed successfully"],
        success:     ["✅", "Completed", "All documents indexed successfully"],
        failed:      ["⛔", "Failed", "Check the sidebar for details"],
        cancelled:   ["⏹", "Cancelled", "Ingestion was stopped"],
        idle:        ["⚙️", "Waiting for the pipeline", "Select a source and trigger ingestion to begin"],
    };

    // ---- state (persist across iframe remounts so counts never reset) ----
    const KEY = "okf_live_dash_v2";
    let state = null;
    try {
        state = JSON.parse(sessionStorage.getItem(KEY) || "null");
    } catch (e) { state = null; }
    if (!state || !state.cur) {
        state = {
            cur: { discovered: 0, fetched: 0, processed: 0, indexed: 0, failed: 0, progress: 0 },
            tgt: { discovered: 0, fetched: 0, processed: 0, indexed: 0, failed: 0, progress: 0 },
            tokenHistory: [],
            running: true,
            total: 0,
            stage: "starting",
            currentSource: "",
            message: "",
            rateLimitHits: 0,
            lastStatus: null,
        };
    }
    if (!state.tokenHistory) state.tokenHistory = [];
    if (typeof state.rateLimitHits !== "number") state.rateLimitHits = 0;

    // ---- DOM refs ----
    const $ = (id) => document.getElementById(id);
    const numbers = ["discovered", "fetched", "processed", "indexed", "failed"];

    function save() {
        try { sessionStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {}
    }

    function fmt(n) {
        return Number(n || 0).toLocaleString("en-US");
    }

    // ---- process flow rendering ----
    function buildSteps() {
        const wrap = $("steps");
        wrap.innerHTML = '<div class="track" id="flowTrack"></div>';
        STEPS.forEach((s, i) => {
            const el = document.createElement("div");
            el.className = "step";
            el.id = "step-" + i;
            el.innerHTML =
                '<div class="ico">' + s.icon + '</div>' +
                '<div class="lbl">' + s.label + '</div>' +
                '<div class="desc">' + s.desc + '</div>';
            wrap.appendChild(el);
        });
    }

    function stageIndex(stage) {
        const s = (stage || "").toLowerCase();
        if (STAGE_INDEX[s] !== undefined) return STAGE_INDEX[s];
        return 0;
    }

    function deriveStage(s) {
        const st = (s.stage || "").toLowerCase();
        if (st && st !== "idle") return st;
        if (s.status === "completed" || s.status === "success") return "completed";
        if (s.status === "failed" || s.status === "cancelled" || s.status === "cancelling") return s.status;
        if (Number(s.fetched || 0) > 0) return "downloading";
        if (Number(s.discovered || 0) > 0) return "discovering";
        if (Number(s.processed || 0) > 0) return "converting";
        if (s.status === "queued" || s.status === "running") return "starting";
        return "idle";
    }

    function renderSteps() {
        const stage = deriveStage(state);
        const status = state.lastStatus;
        const isError = ["failed", "cancelled", "cancelling"].includes(status);
        const isDone = ["completed", "success"].includes(status);
        let idx = stageIndex(stage);
        if (isError) idx = Math.max(0, idx);
        const N = STEPS.length;

        for (let i = 0; i < N; i++) {
            const el = $("step-" + i);
            if (!el) continue;
            el.className = "step";
            if (i < idx && !isError) el.classList.add("done");
            else if (i === idx) {
                if (isError) el.classList.add("error");
                else el.classList.add("active");
            }
        }
        if (isError) {
            // mark the failing step red
            const el = $("step-" + idx);
            if (el) el.classList.add("error");
        }
        if (isDone && !isError) {
            for (let i = 0; i < N; i++) {
                const el = $("step-" + i);
                if (el) { el.className = "step done"; }
            }
        }

        // progress line fill
        let fraction;
        if (isError) fraction = Math.max(0.1, (idx + 0.5) / N);
        else if (isDone) fraction = 1;
        else fraction = Math.max(0.08, (idx + 0.5) / N);
        const track = $("flowTrack");
        if (track) track.style.width = (fraction * 86) + "%";

        // live note
        const note = $("liveNoteText");
        if (note) {
            if (isError) { $("liveNote").style.opacity = "0.6"; note.textContent = status.charAt(0).toUpperCase() + status.slice(1); }
            else if (isDone) note.textContent = "Done";
            else note.textContent = "Live";
        }
    }

    function renderActivity() {
        const stage = deriveStage(state);
        const copy = STAGE_COPY[stage] || STAGE_COPY.starting;
        const ico = $("actIco");
        const title = $("actTitle");
        const sub = $("actSub");
        if (ico) ico.textContent = state.currentStageIco || copy[0];
        const msg = state.stageMessage || state.message;
        if (title) title.textContent = msg || copy[1];
        let subText = copy[2];
        if (state.currentSource) subText = copy[2] + " \u2014 " + state.currentSource;
        if (state.lastStatus === "completed") subText = "Knowledge stored in OKF format and indexed into Qdrant";
        if (state.lastStatus === "failed") subText = state.message || "Check the sidebar for details";
        if (sub) sub.textContent = subText;
    }

    // ---- counters ----
    function renderNumbers() {
        for (const k of numbers) {
            const el = $(k);
            if (el) el.textContent = fmt(Math.round(state.cur[k] || 0));
        }
        const pct = Math.round(state.cur.progress || 0);
        const pctEl = $("pct");
        if (pctEl) pctEl.textContent = pct + "%";
        const fill = $("barFill");
        if (fill) fill.style.width = Math.min(100, Math.max(0, pct)) + "%";
        const sub = $("progressSub");
        if (sub) {
            const total = state.total || Math.max(1, state.tgt.processed || 1);
            sub.textContent = state.running
                ? Math.round(state.cur.processed) + " / " + fmt(total) + " documents processed"
                : (state.lastStatus === "completed"
                    ? "Completed \u2014 all documents indexed."
                    : state.lastStatus === "failed"
                    ? "Failed \u2014 check the sidebar for details."
                    : "Idle \u2014 no ingestion running.");
        }
    }

    function setBadge(status) {
        const badge = $("statusBadge");
        const text = $("statusText");
        if (!badge || !text) return;
        badge.className = "badge";
        if (status === "completed" || status === "success") {
            badge.classList.add("completed");
            text.textContent = "Completed";
        } else if (status === "failed" || status === "cancelled") {
            badge.classList.add("failed");
            text.textContent = status.charAt(0).toUpperCase() + status.slice(1);
        } else if (status === "running" || status === "queued" || status === "cancelling") {
            badge.classList.add("running");
            text.textContent = status.charAt(0).toUpperCase() + status.slice(1);
        } else {
            text.textContent = "Idle";
        }
    }

    // Persistent warning badge for Gemini embedding 429s during indexing.
    // Previously these were only ever visible in the container's stdout logs
    // ("Embedding rate limit (429) hit for '...'"); this makes it visible in
    // the UI itself, and - unlike the activity title (which gets overwritten
    // by the next progress message) - it stays up for the whole run so a
    // slow, rate-limited indexing phase doesn't look indistinguishable from
    // a stuck/broken one.
    function renderRateLimitBadge() {
        const badge = $("rateLimitBadge");
        const count = $("rateLimitCount");
        if (!badge || !count) return;
        const hits = state.rateLimitHits || 0;
        if (hits > 0) {
            count.textContent = fmt(hits);
            badge.style.display = "inline-flex";
        } else {
            badge.style.display = "none";
        }
    }

    // ---- smooth easing: step each counter one tick toward its target ----
    let easing = false;
    function step() {
        let dirty = false;
        for (const k of numbers.concat(["progress"])) {
            const c = state.cur[k] || 0;
            const t = state.tgt[k] || 0;
            if (c < t) { state.cur[k] = Math.min(t, c + 1); dirty = true; }
            else if (c > t) { state.cur[k] = Math.max(t, c - 1); dirty = true; }
        }
        renderNumbers();
        if (dirty) {
            requestAnimationFrame(step);
        } else {
            easing = false;
        }
    }

    function nudge() {
        if (!easing) {
            easing = true;
            requestAnimationFrame(step);
        }
    }

    // ---- charts ----
    let tokenChart = null, donut = null;

    const chartTheme = {
        dark: {
            axisLabel: "#64748b",
            axisLine: "rgba(255,255,255,0.15)",
            splitLine: "rgba(255,255,255,0.07)",
            donutBorder: "#0b1020",
            tooltipBg: "rgba(15,18,40,0.95)",
            tooltipBorder: "rgba(255,255,255,0.15)",
            tooltipText: "#e2e8f0",
        },
        light: {
            axisLabel: "#9aa0a6",
            axisLine: "rgba(15,23,42,0.15)",
            splitLine: "rgba(15,23,42,0.07)",
            donutBorder: "#ffffff",
            tooltipBg: "rgba(255,255,255,0.98)",
            tooltipBorder: "rgba(15,23,42,0.12)",
            tooltipText: "#1f2937",
        },
    };

    function initCharts() {
        if (typeof echarts === "undefined") return;
        const box = $("tokenBox");
        if (box) {
            box.innerHTML = "";
            tokenChart = echarts.init(box);
        }
        donut = echarts.init($("donut"));
        echartsReady = true;
        renderCharts();
    }

    function renderCharts() {
        if (!echartsReady) return;
        const T = chartTheme[THEME] || chartTheme.light;

        const hist = state.tokenHistory;
        if (tokenChart && hist.length) {
            const labels = hist.map((h) => h.label);
            tokenChart.setOption({
                animation: true,
                animationDurationUpdate: 400,
                tooltip: {
                    trigger: "axis",
                    backgroundColor: T.tooltipBg,
                    borderColor: T.tooltipBorder,
                    textStyle: { color: T.tooltipText },
                },
                grid: { left: 44, right: 12, top: 18, bottom: 24 },
                legend: { data: ["Prompt", "Completion"], textStyle: { color: T.axisLabel }, top: 0 },
                xAxis: {
                    type: "category",
                    data: labels,
                    axisLine: { lineStyle: { color: T.axisLine } },
                    axisLabel: { color: T.axisLabel, fontSize: 10 },
                },
                yAxis: {
                    type: "value",
                    splitLine: { lineStyle: { color: T.splitLine } },
                    axisLabel: { color: T.axisLabel, fontSize: 10 },
                },
                series: [
                    {
                        name: "Prompt",
                        type: "line",
                        smooth: true,
                        showSymbol: false,
                        lineStyle: { width: 3, color: "#4285f4" },
                        areaStyle: { color: "rgba(66,133,244,0.22)" },
                        data: hist.map((h) => h.prompt),
                    },
                    {
                        name: "Completion",
                        type: "line",
                        smooth: true,
                        showSymbol: false,
                        lineStyle: { width: 3, color: "#34a853" },
                        areaStyle: { color: "rgba(52,168,83,0.20)" },
                        data: hist.map((h) => h.completion),
                    },
                ],
            });
        }

        const mix = [
            { name: "Processed", value: state.tgt.processed || 0, itemStyle: { color: "#10b981" } },
            { name: "Indexed", value: state.tgt.indexed || 0, itemStyle: { color: "#4285f4" } },
            { name: "Failed", value: state.tgt.failed || 0, itemStyle: { color: "#ef4444" } },
        ];
        donut.setOption({
            animation: true,
            animationDurationUpdate: 400,
            tooltip: {
                trigger: "item",
                backgroundColor: T.tooltipBg,
                borderColor: T.tooltipBorder,
                textStyle: { color: T.tooltipText },
            },
            series: [{
                type: "pie",
                radius: ["62%", "88%"],
                avoidLabelOverlap: true,
                itemStyle: { borderColor: T.donutBorder, borderWidth: 3 },
                label: { show: false },
                emphasis: { label: { show: true, color: T.tooltipText } },
                data: mix.filter((d) => d.value > 0),
            }],
        });
        const total = mix.reduce((s, d) => s + d.value, 0);
        $("donutCenter").textContent = total > 0 ? (state.tgt.progress || 0) + "%" : "0%";
        $("mixLegend").innerHTML = mix.map((d) =>
            `<span><i style="background:${d.itemStyle.color}"></i>${d.name} ${d.value}</span>`
        ).join("");
    }

    // fallback: simple CSS bars when echarts CDN is unavailable
    function renderFallbackTokens() {
        const box = $("tokenBox");
        if (!box || echartsReady) return;
        const hist = state.tokenHistory.slice(-12);
        if (!hist.length) return;
        const max = Math.max(1, ...hist.map((h) => h.prompt + h.completion));
        box.innerHTML = "";
        const line = document.createElement("div");
        line.className = "token-line";
        hist.forEach((h) => {
            const col = document.createElement("div");
            col.className = "col";
            const ph = (h.prompt / max) * 100;
            const ch = (h.completion / max) * 100;
            col.innerHTML =
                `<div class="seg prompt" style="height:${Math.max(3, ph)}%"></div>` +
                `<div class="seg completion" style="height:${Math.max(3, ch)}%"></div>` +
                `<span class="lbl">${h.label}</span>`;
            line.appendChild(col);
        });
        box.appendChild(line);
    }

    // ---- apply a status payload to the shared state ----
    function applyStatus(s, opts) {
        const status = s.status || "idle";
        const isActive = ["running", "queued", "cancelling"].includes(status);
        const isDone = ["completed", "success"].includes(status);

        state.running = isActive || isDone;
        state.lastStatus = status;
        state.stage = s.stage || state.stage || "";
        state.currentSource = s.current_source || "";
        state.message = s.message || "";
        state.stageMessage = s.stage_message || "";
        const copy = STAGE_COPY[deriveStage(s)] || STAGE_COPY.starting;
        state.currentStageIco = copy[0];

        state.tgt.discovered = Number(s.discovered || 0);
        state.tgt.fetched = Number(s.fetched || 0);
        state.tgt.processed = Number(s.processed || 0);
        state.tgt.indexed = Number(s.indexed_documents ?? s.indexed ?? 0);
        state.tgt.failed = Number(s.failed || 0);
        state.tgt.progress = Number(s.progress_percent || (isDone ? 100 : 0));
        state.total = Number(s.total_documents || 0);
        // The backend resets rate_limit_hits to 0 at the start of every new
        // run (see app.ingestion.pipeline's initial update_status call), so
        // trusting it directly here is enough - no client-side reset logic
        // needed, and it stays correct across Streamlit reruns/remounts.
        state.rateLimitHits = Number(s.rate_limit_hits || 0);

        const prompt = Number(s.prompt_tokens_estimate || 0);
        const completion = Number(s.completion_tokens_estimate || 0);
        const label = new Date().toLocaleTimeString("en-US", { hour12: false });

        // Avoid duplicating an identical point when the iframe remounts on each
        // Streamlit rerun with the same embedded status.
        const key = label + "|" + prompt + "|" + completion;
        const last = state.tokenHistory.length
            ? state.tokenHistory[state.tokenHistory.length - 1]
            : null;
        const lastKey = last ? last.label + "|" + last.prompt + "|" + last.completion : null;
        if (key !== lastKey) {
            state.tokenHistory.push({ label, prompt, completion });
            if (state.tokenHistory.length > 30) state.tokenHistory.shift();
        }

        if (opts && opts.notify) {
            setBadge(status);
            renderRateLimitBadge();
            save();
            nudge();
            renderSteps();
            renderActivity();
            renderCharts();
            renderFallbackTokens();
        }
    }

    // ---- polling (enhancement only; embedded status is the source of truth) ----
    async function poll() {
        try {
            const res = await fetch(API_BASE + "/api/v1/ingest/status", { cache: "no-store" });
            if (!res.ok) throw new Error("status " + res.status);
            const s = await res.json();
            applyStatus(s, { notify: true });
        } catch (e) {
            // Browser cannot reach the API directly (e.g. preview domain + docker
            // host). The embedded status updated on the next Streamlit rerun.
            if (!EMBEDDED) {
                const badge = $("statusBadge");
                const text = $("statusText");
                if (badge) {
                    badge.className = "badge";
                    if (text) text.textContent = "API offline";
                }
            }
        }
    }

    buildSteps();
    if (typeof echarts !== "undefined") {
        initCharts();
    } else {
        window.addEventListener("echarts-loaded", initCharts);
        const t = setTimeout(renderFallbackTokens, 2500);
        window.addEventListener("echarts-loaded", () => clearTimeout(t));
    }

    renderNumbers();
    renderSteps();
    renderActivity();
    if (EMBEDDED) {
        applyStatus(INITIAL, { notify: true });
    }
    setBadge(state.lastStatus || "idle");
    renderRateLimitBadge();
    poll();
    window.setInterval(poll, 800);
    window.setInterval(save, 2000);
})();
</script>
</body>
</html>
""".replace("__API_BASE_JS__", api_base_js).replace(
        "__THEME__", _html.escape(theme, quote=True)
    ).replace(
        "window.__OKF_STATUS__ || null",
        "(%s) || null" % status_js,
    )


def render_live_dashboard(
    api_host: str,
    status: Optional[dict] = None,
    theme: str = "light",
    height: int = 620,
) -> None:
    """Render the live glassmorphism ingestion dashboard.

    ``status`` is the server-side status fetched by Streamlit and embedded into
    the component, so the counters reflect real backend progress even when the
    browser cannot reach the API directly. ``theme`` picks the light/dark palette.
    ``height`` controls the iframe's pixel height; kept compact (down from an
    original 760px) so the dialog's own footer (hint text + Close button) stays
    within the viewport without relying on the dialog's internal scroll to
    reach it - see the `max-height`/`overflow-y: auto` safety net on
    `[data-testid="stDialog"] [role="dialog"]` in app.py for the cases where a
    small screen still needs it.
    """
    base = browser_api_base(api_host)
    html = _build_html(base, theme=theme, initial_status=status)
    st.components.v1.html(html, height=height, scrolling=False)
