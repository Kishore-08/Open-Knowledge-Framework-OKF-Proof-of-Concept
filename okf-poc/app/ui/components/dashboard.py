"""
Self-contained live ingestion dashboard.

Rendered as a Streamlit HTML component so the counters, progress bar and
token graphs animate smoothly in the browser instead of re-rendering on every
Streamlit rerun. The component eases every number toward its target one step at
a time (+1 increments), which is what makes the "live progress" feel smooth.

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
from typing import Dict, Optional

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


def _build_html(api_base: str, theme: str = "dark", initial_status: Optional[dict] = None) -> str:
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
        --accent: #6366f1;
        --accent-2: #8b5cf6;
        --accent-3: #ec4899;
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
        --body-bg:
            radial-gradient(900px 400px at 10% -10%, rgba(99, 102, 241, 0.28), transparent 60%),
            radial-gradient(700px 400px at 110% 0%, rgba(236, 72, 153, 0.18), transparent 55%),
            radial-gradient(600px 500px at 50% 120%, rgba(139, 92, 246, 0.16), transparent 60%),
            #0b1020;
    }

    body[data-theme="light"] {
        --text: #1e293b;
        --text-dim: #64748b;
        --glass-bg: rgba(255, 255, 255, 0.72);
        --glass-border: rgba(15,23,42,0.10);
        --glass-shadow: rgba(15, 23, 42, 0.10);
        --axis-line: rgba(15,23,42,0.15);
        --axis-label: #94a3b8;
        --split-line: rgba(15,23,42,0.07);
        --bar-track: rgba(15,23,42,0.08);
        --donut-center: rgba(255,255,255,0.92);
        --donut-border: #ffffff;
        --badge-bg: rgba(255,255,255,0.85);
        --badge-border: rgba(15,23,42,0.12);
        --body-bg:
            radial-gradient(900px 400px at 10% -10%, rgba(99,102,241,0.14), transparent 60%),
            radial-gradient(700px 400px at 110% 0%, rgba(236,72,153,0.08), transparent 55%),
            radial-gradient(600px 500px at 50% 120%, rgba(139,92,246,0.10), transparent 60%),
            #f2f5fc;
    }

    body {
        min-height: 100%;
        padding: 18px;
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
        gap: 16px;
    }

    .head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 20px;
    }

    .head h2 {
        font-size: 1.15rem;
        font-weight: 650;
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

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(99,102,241,0.7); }
        70% { box-shadow: 0 0 0 8px rgba(99,102,241,0); }
        100% { box-shadow: 0 0 0 0 rgba(99,102,241,0); }
    }

    .cards {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
    }
    @media (max-width: 900px) { .cards { grid-template-columns: repeat(2, 1fr); } }

    .stat {
        padding: 14px 16px;
        display: flex;
        flex-direction: column;
        gap: 6px;
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
        width: 30px; height: 30px;
        border-radius: 9px;
        display: grid; place-items: center;
        font-size: 15px;
        background: color-mix(in srgb, var(--c, var(--accent)) 18%, transparent);
        color: var(--c, var(--accent));
    }
    .stat .num {
        font-size: 1.7rem;
        font-weight: 750;
        font-variant-numeric: tabular-nums;
        line-height: 1;
        color: var(--text);
    }
    .stat .lbl {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: var(--text-dim);
    }

    .progress-card { padding: 18px 20px; }
    .progress-top {
        display: flex; justify-content: space-between; align-items: baseline;
        margin-bottom: 10px;
    }
    .progress-top .ttl {
        font-size: 0.85rem; font-weight: 600; color: var(--text-dim);
    }
    .progress-top .pct {
        font-size: 1.5rem; font-weight: 750; font-variant-numeric: tabular-nums;
        background: linear-gradient(90deg, var(--accent), var(--accent-3));
        -webkit-background-clip: text; background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .bar { height: 12px; border-radius: 999px; background: var(--bar-track); overflow: hidden; position: relative; }
    .bar .fill {
        height: 100%; width: 0%;
        border-radius: 999px;
        background: linear-gradient(90deg, var(--accent), var(--accent-2), var(--accent-3));
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
    .chart-card { padding: 14px 16px; }
    .chart-card h3 {
        font-size: 0.85rem; font-weight: 600; color: var(--text-dim);
        margin-bottom: 6px;
    }
    .chart-box { width: 100%; height: 210px; position: relative; }
    .chart-note {
        font-size: 0.75rem; color: var(--text-dim); padding: 8px;
        text-align: center;
    }

    .token-line {
        display: flex; gap: 14px; align-items: flex-end; height: 170px;
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
    .token-line .col .seg.completion { background: linear-gradient(180deg, var(--accent-3), #f472b6); }
    .token-line .col .lbl {
        font-size: 0.65rem; color: var(--text-dim); text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    .donut-wrap {
        display: flex; align-items: center; justify-content: center;
        flex-direction: column; gap: 8px; height: 170px;
    }
    .donut { width: 140px; height: 140px; border-radius: 50%; position: relative; }
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
        <h2>&#9203; Ingestion Progress</h2>
        <span class="badge running" id="statusBadge">
            <span class="dot"></span>
            <span id="statusText">Connecting&hellip;</span>
        </span>
    </div>

    <div class="cards" id="cards">
        <div class="stat glass" style="--c:#60a5fa;">
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
    const THEME = document.body.dataset.theme || "dark";
    // Server-side status embedded on every Streamlit rerun. This is the primary
    // source of truth so the counters move even when the browser cannot reach
    // the API directly.
    const INITIAL = window.__OKF_STATUS__ || null;
    const EMBEDDED = !!(INITIAL && Object.keys(INITIAL).length);
    let echartsReady = false;

    // ---- state (persist across iframe remounts so counts never reset) ----
    const KEY = "okf_live_dash_v1";
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
        };
    }
    if (!state.tokenHistory) state.tokenHistory = [];

    // ---- DOM refs ----
    const $ = (id) => document.getElementById(id);
    const numbers = ["discovered", "fetched", "processed", "indexed", "failed"];

    function save() {
        try { sessionStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {}
    }

    function fmt(n) {
        return Number(n || 0).toLocaleString("en-US");
    }

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
            axisLabel: "#94a3b8",
            axisLine: "rgba(15,23,42,0.15)",
            splitLine: "rgba(15,23,42,0.07)",
            donutBorder: "#ffffff",
            tooltipBg: "rgba(255,255,255,0.98)",
            tooltipBorder: "rgba(15,23,42,0.12)",
            tooltipText: "#1e293b",
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
        const T = chartTheme[THEME] || chartTheme.dark;

        // Token history area chart
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
                        lineStyle: { width: 3, color: "#6366f1" },
                        areaStyle: { color: "rgba(99,102,241,0.25)" },
                        data: hist.map((h) => h.prompt),
                    },
                    {
                        name: "Completion",
                        type: "line",
                        smooth: true,
                        showSymbol: false,
                        lineStyle: { width: 3, color: "#ec4899" },
                        areaStyle: { color: "rgba(236,72,153,0.22)" },
                        data: hist.map((h) => h.completion),
                    },
                ],
            });
        }

        // Pipeline mix donut
        const mix = [
            { name: "Processed", value: state.tgt.processed || 0, itemStyle: { color: "#10b981" } },
            { name: "Indexed", value: state.tgt.indexed || 0, itemStyle: { color: "#6366f1" } },
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

        state.tgt.discovered = Number(s.discovered || 0);
        state.tgt.fetched = Number(s.fetched || 0);
        state.tgt.processed = Number(s.processed || 0);
        state.tgt.indexed = Number(s.indexed_documents ?? s.indexed ?? 0);
        state.tgt.failed = Number(s.failed || 0);
        state.tgt.progress = Number(s.progress_percent || (isDone ? 100 : 0));
        state.total = Number(s.total_documents || 0);

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
            save();
            nudge();
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

    if (typeof echarts !== "undefined") {
        initCharts();
    } else {
        window.addEventListener("echarts-loaded", initCharts);
        const t = setTimeout(renderFallbackTokens, 2500);
        window.addEventListener("echarts-loaded", () => clearTimeout(t));
    }

    renderNumbers();
    if (EMBEDDED) {
        applyStatus(INITIAL, { notify: true });
    }
    setBadge(state.lastStatus || "idle");
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
    theme: str = "dark",
) -> None:
    """Render the live glassmorphism ingestion dashboard.

    ``status`` is the server-side status fetched by Streamlit and embedded into
    the component, so the counters reflect real backend progress even when the
    browser cannot reach the API directly. ``theme`` picks the light/dark palette.
    """
    base = browser_api_base(api_host)
    html = _build_html(base, theme=theme, initial_status=status)
    st.components.v1.html(html, height=560, scrolling=False)
