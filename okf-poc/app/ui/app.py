import streamlit as st
import requests
import os
import time
import json
import sys
from pathlib import Path

# Make the repo root importable so `app.ui.components.dashboard` resolves both
# when running locally and inside the UI container. Streamlit puts the script's
# directory first in sys.path, and since the script is named `app.py` it would
# shadow the `app` package — always inserting the repo root at index 0 fixes this.
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_REPO_ROOT) in sys.path:
    sys.path.remove(str(_REPO_ROOT))
sys.path.insert(0, str(_REPO_ROOT))

from app.ui.components.dashboard import render_live_dashboard

# Page configuration MUST be the first Streamlit command
st.set_page_config(
    page_title="OKF Knowledge Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------------------------
# Global glassmorphism theme (dual-mode: dark / light)
# ---------------------------------------------------------------------------

STYLE_DIR = Path(__file__).resolve().parent / "styles"


def load_css_file(name: str) -> str:
    """Load a stylesheet stored alongside the Streamlit UI."""
    return (STYLE_DIR / name).read_text(encoding="utf-8")


def load_theme_css(theme: str) -> str:
    """Combine shared styles with the selected light or dark palette."""
    theme_file = "light.css" if theme == "light" else "dark.css"
    return f"""
<style>
{load_css_file('base.css')}

{load_css_file(theme_file)}
</style>
"""


# Theme state. Dark is the default — it mirrors the original OKF dark design
# exactly. The sidebar toggle flips between dark and light at runtime.
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

st.markdown(load_theme_css(st.session_state.theme), unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------
API_HOST = os.getenv("API_HOST", "http://localhost:8000")

def check_api_health():
    """Pings the FastAPI health endpoint and returns its parsed checks (or None)."""
    try:
        res = requests.get(f"{API_HOST}/health", timeout=2)
        if res.status_code != 200:
            return None
        return res.json()
    except requests.exceptions.RequestException:
        return None

def get_available_sources():
    """Fetch documentation sources from the backend (from sources.yaml)."""
    try:
        res = requests.get(f"{API_HOST}/api/v1/ingest/sources", timeout=5)
        if res.status_code == 200:
            return res.json().get("sources", [])
    except requests.exceptions.RequestException:
        pass
    return []

def trigger_ingestion(sources=None):
    """Starts ingestion and stores the exact job ID."""
    try:
        payload = {
            "sources": sources or []
        }

        res = requests.post(
            f"{API_HOST}/api/v1/ingest/",
            json=payload,
            timeout=10,
        )

        if res.status_code != 200:
            st.sidebar.error(f"❌ Error: {res.text}")
            return False

        data = res.json()

        job_id = data.get("job_id")

        if not job_id:
            st.sidebar.error(
                "Ingestion started but API did not return a job ID."
            )
            return False

        st.session_state.ingestion_job_id = job_id
        st.session_state.ingestion_running = True
        st.session_state.ingestion_overlay_open = True

        st.session_state.ingestion_message = data.get(
            "message",
            "Ingestion started.",
        )

        return True

    except requests.exceptions.RequestException as e:
        st.sidebar.error(f"Connection Error: {e}")
        return False

def get_ingestion_status():
    """Gets the current ingestion status from FastAPI."""
    try:
        res = requests.get(
            f"{API_HOST}/api/v1/ingest/status",
            timeout=5,
        )
        if res.status_code == 200:
            return res.json()
        return None
    except requests.exceptions.RequestException:
        return None

def get_job_status(job_id):
    """Fetch status for one exact ingestion job."""
    if not job_id:
        return None

    try:
        res = requests.get(
            f"{API_HOST}/api/v1/jobs/{job_id}",
            timeout=5,
        )

        if res.status_code == 200:
            return res.json()

        return None

    except requests.exceptions.RequestException:
        return None
    
def upload_files(files, sources=None):
    """Upload files to the backend and start processing for selected sources.

    Uploads run in upload-only mode server-side: ONLY the uploaded files are
    converted + indexed, and the documentation crawl is skipped entirely, so an
    uploaded document is never mixed with cached crawl pages.
    """
    files_data = []
    for f in files:
        f.seek(0)
        files_data.append(('files', (f.name, f.getvalue(), f.type or "application/octet-stream")))
    data = {"sources": ""}  # upload-only: sources ignored / no crawl
    response = requests.post(
        f"{API_HOST}/api/v1/ingest/upload",
        files=files_data,
        data=data,
        timeout=30,
    )
    return response

def simulated_typing_effect(text):
    """Simulates a typewriter effect for better UX."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Enterprise OKF Knowledge Assistant. How can I help you today?", "citations": [], "retrieval_mode": ""}
    ]

if "ingestion_running" not in st.session_state:
    st.session_state.ingestion_running = False
    
if "ingestion_job_id" not in st.session_state:
    st.session_state.ingestion_job_id = None

if "ingestion_overlay_open" not in st.session_state:
    st.session_state.ingestion_overlay_open = False

if "ingestion_message" not in st.session_state:
    st.session_state.ingestion_message = ""

if "upload_success_message" not in st.session_state:
    st.session_state.upload_success_message = ""

if "last_uploaded" not in st.session_state:
    st.session_state.last_uploaded = []

# ---------------------------------------------------------------------------
# Knowledge base browser
# ---------------------------------------------------------------------------
def render_knowledge_base(is_healthy: bool):
    """Knowledge Base browser: categories, concept list, metadata, and full content."""
    st.markdown('<div class="hero-title"><span class="hero-emoji">📚</span> <span class="hero-text">OKF Knowledge Base</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">Browse the curated OKF knowledge repository. Each concept is a Markdown file with YAML metadata and links back to its official source.</div>', unsafe_allow_html=True)

    if not is_healthy:
        st.warning("Backend offline: showing any locally cached repository data is unavailable. Start the API to browse the knowledge base.")
        return

    try:
        stats_res = requests.get(f"{API_HOST}/api/v1/knowledge/stats", timeout=5)
        if stats_res.status_code == 200:
            stats = stats_res.json()
            cats = stats.get("categories", {})
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Concepts", stats.get("total_concepts", 0))
            col2.metric("Categories", len(cats))
            col3.metric("Total Tags", stats.get("total_tags", 0))
            col4.metric("Sources", len(stats.get("sources", [])))
    except requests.exceptions.RequestException:
        st.error("Could not reach the knowledge base API.")

    st.divider()

    search_query = st.text_input("🔎 Search concepts", placeholder="e.g. deployment rollout, chmod permissions...")
    search_results = []
    if search_query.strip():
        try:
            res = requests.get(f"{API_HOST}/api/v1/knowledge/search", params={"q": search_query}, timeout=5)
            if res.status_code == 200:
                search_results = res.json().get("results", [])
        except requests.exceptions.RequestException:
            pass
        st.markdown(f"**Search results ({len(search_results)}):**")
        if search_results:
            for hit in search_results:
                with st.expander(f"{hit.get('title', hit.get('id'))} — {hit.get('category')}"):
                    st.markdown(hit.get("description") or "*no description*")
                    st.markdown(f"Tags: {', '.join(hit.get('tags', []))}")
                    if hit.get("snippet"):
                        st.caption(hit.get("snippet"))
                    if hit.get("source_url"):
                        st.markdown(f"[Official source]({hit.get('source_url')})")
        else:
            st.info("No matches. Try different keywords.")

    try:
        cat_res = requests.get(f"{API_HOST}/api/v1/knowledge/categories", timeout=5)
        categories = cat_res.json() if cat_res.status_code == 200 else []
    except requests.exceptions.RequestException:
        categories = []

    st.divider()
    st.markdown("### Browse by category")
    selected_category = st.selectbox("Category", ["All"] + categories) if categories else "All"

    try:
        params = {"category": selected_category} if selected_category != "All" else {}
        concepts_res = requests.get(f"{API_HOST}/api/v1/knowledge/concepts", params=params, timeout=5)
        concepts = concepts_res.json() if concepts_res.status_code == 200 else []
    except requests.exceptions.RequestException:
        concepts = []

    if concepts:
        for idx, concept in enumerate(concepts):
            with st.expander(f"{concept.get('title')} — {concept.get('category')}"):
                st.markdown(concept.get("description") or "*no description*")
                st.markdown(f"**Tags:** {', '.join(concept.get('tags', []))}  ")
                st.markdown(f"**Type:** {concept.get('type')}")
                if concept.get("source_url"):
                    st.markdown(f"**Source:** [Official documentation]({concept.get('source_url')})")
                if st.button("📖 View full concept", key=f"view_{idx}_{concept.get('id')}"):
                    try:
                        detail = requests.get(
                            f"{API_HOST}/api/v1/knowledge/concepts/{concept.get('id')}", timeout=5
                        ).json()
                        st.markdown("---")
                        st.markdown(detail.get("content", ""))
                    except requests.exceptions.RequestException:
                        st.error("Could not load concept detail.")
    else:
        st.info("No concepts in this category yet. Run the crawl + convert + build_index pipeline to populate the knowledge base.")

    st.divider()
    st.markdown("### Vector index status")
    st.caption(
        "Concepts are indexed into Qdrant (`okf_concepts`) with hybrid search. "
        "Run `python -m scripts.build_index` to rebuild the index after adding concepts."
    )

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.title("⚙️ OKF Control Panel")
    st.markdown("Manage your Open Knowledge Framework pipeline.")

    # Dual-mode theme toggle
    dark_mode = st.toggle(
        "🌙 Dark mode",
        value=st.session_state.theme == "dark",
        help="Switch between the dark and light glassmorphism themes.",
    )
    new_theme = "dark" if dark_mode else "light"
    if new_theme != st.session_state.theme:
        st.session_state.theme = new_theme
        st.rerun()

    st.divider()

    # System status
    st.subheader("System Status")
    health = check_api_health()
    is_healthy = health is not None
    if health:
        checks = health.get("checks", {})
        qdrant_ok = checks.get("qdrant", {}).get("ok", False)
        llm_ok = checks.get("llm", {}).get("ok", False)
        api_state = "online" if health.get("status") == "healthy" else "degraded"
        st.markdown(
            f'<div class="health-pill {"ok" if api_state == "online" else "warn"}">'
            f'<span class="dot"></span>FastAPI Backend · {api_state}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="health-pill {"ok" if qdrant_ok else "bad"}">'
            f'<span class="dot"></span>Qdrant Vector DB · {"Connected" if qdrant_ok else "Disconnected"}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="health-pill {"ok" if llm_ok else "warn"}">'
            f'<span class="dot"></span>LLM · {"Ready" if llm_ok else "Key missing"}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="health-pill bad"><span class="dot"></span>FastAPI Backend · Offline</div>',
            unsafe_allow_html=True,
        )
        st.error("Cannot connect to API. Please ensure Docker containers are running.")

    st.divider()

    # Navigation
    st.subheader("Navigation")
    page = st.radio("View", ["💬 Chat Assistant", "📚 Knowledge Base"], index=0)

    st.divider()

    # ------------------------------------------------------------------
    # Ingestion controls
    # ------------------------------------------------------------------
    st.subheader("Knowledge Ingestion")

    # Source selection
    available_sources = get_available_sources()
    enabled_sources = [s["name"] for s in available_sources if s.get("enabled")]
    source_options = [s["name"] for s in available_sources]

    st.markdown("**Documentation Sources**")
    st.caption("Pick which docs to crawl. Leave empty to process only uploaded files.")
    selected_sources = st.multiselect(
        "Sources to ingest",
        options=source_options,
        default=enabled_sources,
        help="Select documentation sources from config/sources.yaml to crawl during ingestion.",
        label_visibility="collapsed",
    )

    if selected_sources:
        chips = "".join(
            f'<span class="src-chip"><b>{s}</b></span>' for s in selected_sources
        )
        st.markdown(
            f'<div style="margin: 4px 0 8px;">{chips}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.caption("⚠️ No sources selected — ingestion will only process uploaded/cached files.")

    # Upload dropzone
    uploaded_files = st.file_uploader(
        "Choose files to upload",
        type=['pdf', 'md', 'txt', 'json'],
        accept_multiple_files=True,
        help="Supported formats: PDF, Markdown, Text, JSON",
        label_visibility="collapsed",
    )

    # Selected files summary
    if uploaded_files:
        total_bytes = sum(len(f.getvalue()) for f in uploaded_files)
        size_str = f"{total_bytes / (1024*1024):.2f} MB" if total_bytes >= 1024 * 1024 else f"{total_bytes / 1024:.1f} KB"
        st.markdown(
            f'<div class="glass-card" style="padding: 0.7rem 0.9rem; margin: 0.4rem 0;">'
            f'📁 <b>{len(uploaded_files)}</b> file(s) · {size_str}</div>',
            unsafe_allow_html=True,
        )

    # Process button (redesigned)
    can_run = is_healthy and not st.session_state.ingestion_running
    if uploaded_files:
        process_label = "✨ Process & Index Documents"
    else:
        process_label = "🚀 Trigger Ingestion"

    if st.button(
        process_label,
        use_container_width=True,
        disabled=not can_run,
        type="primary",
    ):
        if uploaded_files:
            with st.spinner("📤 Uploading files..."):
                try:
                    response = upload_files(uploaded_files, selected_sources)
                    if response.status_code == 200:
                        result = response.json()

                        job_id = result.get("job_id")

                        if not job_id:
                            st.error("Upload succeeded but no ingestion job ID was returned.")
                        else:
                            st.session_state.ingestion_job_id = job_id
                            st.session_state.ingestion_running = True
                            st.session_state.ingestion_overlay_open = True
                            st.session_state.upload_success_message = result.get(
                                "message",
                                "Upload successful",
                            )

                            st.rerun()
                    else:
                        st.error(f"Upload failed: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Connection error: {e}")
        else:
            started = trigger_ingestion(selected_sources)

            if started:
                st.rerun()

    if not can_run and st.session_state.ingestion_running:
        running_status = get_ingestion_status()
        if running_status:
            status_value = running_status.get("status", "").lower()

            if status_value in {
                "completed",
                "success",
                "failed",
                "cancelled",
            }:
                st.session_state.ingestion_running = False
                st.session_state.ingestion_overlay_open = False
        stage = (running_status or {}).get("stage", "")
        stage_labels = {
            "starting": "Starting pipeline…",
            "discovering": "Discovering documentation…",
            "downloading": "Downloading from official websites…",
            "cached": "Raw data stored in cache…",
            "converting": "Running ingestion pipeline (→ OKF)…",
            "formatting": "Writing OKF knowledge files…",
            "indexing": "Indexing into Qdrant…",
        }
        stage_label = stage_labels.get(stage, "Ingestion is running…")
        if running_status:
            pct = running_status.get("progress_percent", 0)
            pct_clamped = min(100, max(0, pct))
            pct_color = "#1a73e8" if st.session_state.theme == "light" else "#a5b4fc"
            track_color = "rgba(15,23,42,0.10)" if st.session_state.theme == "light" else "rgba(255,255,255,0.10)"
            st.markdown(
                f'<div class="glass-card" style="padding: 0.7rem 0.9rem; margin: 0.4rem 0;">'
                f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">'
                f'<b style="font-size:0.85rem;">⚙️ {stage_label}</b>'
                f'<span style="font-size:0.85rem;font-weight:700;color:{pct_color};">{pct}%</span>'
                f'</div>'
                f'<div style="height:8px;border-radius:999px;background:{track_color};overflow:hidden;">'
                f'<div style="height:100%;width:{pct_clamped}%;border-radius:999px;'
                f'background:linear-gradient(90deg,#4285f4,#1a73e8);transition:width 0.4s ease;"></div>'
                f'</div></div>',
                unsafe_allow_html=True,
            )
        if st.button("⏹ Stop Ingestion", use_container_width=True, key="stop_ingestion_btn"):
            job_id = st.session_state.get("ingestion_job_id")
            if job_id:
                try:
                    requests.post(
                        f"{API_HOST}/api/v1/jobs/{job_id}/cancel",
                        timeout=5,
                    )
                    st.success("Cancellation requested. The pipeline will stop at the next stage.")
                except requests.exceptions.RequestException as e:
                    st.error(f"Could not reach the API: {e}")
            else:
                st.session_state.ingestion_running = False
            st.rerun()

    st.divider()
    st.caption("Powered by Google OKF, LlamaIndex, and Qdrant.")

# ---------------------------------------------------------------------------
# Main content
# ---------------------------------------------------------------------------
if page == "📚 Knowledge Base":
    render_knowledge_base(is_healthy)
    st.stop()

# Hero header
st.markdown('<div class="hero-title"><span class="hero-emoji">🧠</span> <span class="hero-text">OKF Knowledge Retrieval</span></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Ask questions against your enterprise knowledge base. '
    'Answers are generated using Hybrid Search and strict OKF citations.</div>',
    unsafe_allow_html=True,
)

# Live ingestion progress — rendered as a popup/overlay on the main page with
# curved edges (st.dialog). The dashboard component embeds the server-side
# status on every rerun so the counters move even if the browser cannot reach
# the API directly.
def _dismiss_ingestion_overlay() -> None:
    """
    Close only the popup.
    The ingestion job continues running in the background.
    """
    st.session_state.ingestion_running = False


@st.dialog(
    "Live Ingestion Pipeline",
    width="large",
    dismissible=True,
    on_dismiss=_dismiss_ingestion_overlay,
)
def ingestion_overlay() -> None:

    job_id = st.session_state.get("ingestion_job_id")

    if not job_id:
        st.warning("No ingestion job is currently being tracked.")
        return

    initial_status = get_job_status(job_id)

    st.markdown(
        '<div class="dialog-hint">'
        'Watching the pipeline in real time: '
        'Download from official website → store raw data in cache → '
        'run the ingestion pipeline → OKF knowledge files → '
        'indexed into Qdrant.'
        '</div>',
        unsafe_allow_html=True,
    )

    render_live_dashboard(
        API_HOST,
        status=initial_status,
        theme=st.session_state.theme,
        job_id=job_id,
    )

    col_hint, col_btn = st.columns([3, 1])

    col_hint.caption(
        "The ingestion job continues running on the backend. "
        "The dashboard above updates automatically."
    )

    if col_btn.button(
        "Close",
        key="close_ingestion_overlay",
        use_container_width=True,
    ):
        _dismiss_ingestion_overlay()
        st.rerun()


if (
    st.session_state.ingestion_running
    and st.session_state.ingestion_overlay_open
):
    ingestion_overlay()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("citations"):
            mode = message.get("retrieval_mode") or "retrieved"
            st.markdown(f"📚 **Knowledge-base results ({mode} search):**")
            for citation in message["citations"]:
                title = citation.get("title", "Unknown OKF Source")
                score = citation.get("score", 0.0)
                with st.expander(f"📄 {title} · relevance {score:.3f}"):
                    st.markdown(citation.get("content", "No preview available."))

if prompt := st.chat_input("Ask a question about your documents...", disabled=not is_healthy):

    st.session_state.messages.append({"role": "user", "content": prompt, "citations": [], "retrieval_mode": ""})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        try:
            with st.spinner("Performing Hybrid Search and reasoning over OKF documents..."):
                response = requests.post(
                    f"{API_HOST}/api/v1/query/",
                    json={"query": prompt},
                    timeout=120,
                )

            if response.status_code == 200:
                data = response.json()
                answer = data.get("answer", "No answer generated.")
                citations = data.get("citations", [])
                retrieval_mode = data.get("retrieval_mode", "")

                message_placeholder.write_stream(simulated_typing_effect(answer))

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "citations": citations,
                    "retrieval_mode": retrieval_mode,
                })
                st.rerun()
            else:
                st.error(f"API Error {response.status_code}: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the FastAPI backend. Is the server running?")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
