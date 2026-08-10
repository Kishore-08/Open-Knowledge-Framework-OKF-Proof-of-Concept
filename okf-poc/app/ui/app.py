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
# Global glassmorphism theme
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    /* Dark aurora backdrop */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    .stApp {
        background:
            radial-gradient(1000px 500px at 15% -10%, rgba(99, 102, 241, 0.22), transparent 60%),
            radial-gradient(800px 500px at 110% 10%, rgba(236, 72, 153, 0.16), transparent 55%),
            radial-gradient(700px 600px at 50% 120%, rgba(139, 92, 246, 0.14), transparent 60%),
            #0b1020;
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit chrome */
    #MainMenu, footer { visibility: hidden; }
    .block-container { padding-top: 1.5rem; max-width: 1200px; }
    [data-testid="stHeader"] { background: transparent; }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.15); border-radius: 999px; }

    /* ---- Glassmorphism shared card ---- */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(18px) saturate(140%);
        -webkit-backdrop-filter: blur(18px) saturate(140%);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
        padding: 1.1rem 1.3rem;
        margin-bottom: 0.75rem;
    }

    /* ---- Sidebar ---- */
    [data-testid="stSidebar"] {
        background: rgba(15, 18, 40, 0.55);
        backdrop-filter: blur(24px) saturate(140%);
        -webkit-backdrop-filter: blur(24px) saturate(140%);
        border-right: 1px solid rgba(255, 255, 255, 0.10);
    }
    [data-testid="stSidebar"] * { color: #e2e8f0; }
    [data-testid="stSidebar"] .stTitle h1 { font-size: 1.35rem; font-weight: 700; }
    [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.12); }

    /* ---- Headers ---- */
    h1, h2, h3 {
        color: #f1f5f9 !important;
        font-weight: 650 !important;
        letter-spacing: -0.01em;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 750;
        background: linear-gradient(90deg, #fff 0%, #c7d2fe 45%, #f0abfc 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
    }
    .hero-sub { color: #94a3b8; font-size: 0.98rem; margin-top: 0.2rem; }

    /* ---- Buttons ---- */
    .stButton > button, .stDownloadButton > button {
        border-radius: 14px !important;
        font-weight: 600 !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        background: rgba(255,255,255,0.06) !important;
        color: #e2e8f0 !important;
        backdrop-filter: blur(10px);
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        border-color: rgba(99, 102, 241, 0.6) !important;
        background: rgba(99, 102, 241, 0.18) !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.25);
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: #fff !important;
        border: none !important;
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.35);
    }
    .stButton > button[kind="primary"]:hover {
        filter: brightness(1.1);
        box-shadow: 0 8px 28px rgba(99, 102, 241, 0.5);
    }

    /* ---- Upload dropzone ---- */
    [data-testid="stFileUploaderDropzone"] {
        background: rgba(255,255,255,0.03) !important;
        border: 2px dashed rgba(96, 165, 250, 0.35) !important;
        border-radius: 18px !important;
        backdrop-filter: blur(12px);
        transition: all 0.25s ease;
    }
    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: rgba(96, 165, 250, 0.7) !important;
        background: rgba(96, 165, 250, 0.06) !important;
    }
    [data-testid="stFileUploaderDropzone"] small, 
    [data-testid="stFileUploaderDropzone"] div { color: #94a3b8 !important; }

    /* ---- Inputs ---- */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] > div {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        border-radius: 12px !important;
        color: #e2e8f0 !important;
    }
    .stTextInput input::placeholder, .stTextArea textarea::placeholder { color: #64748b !important; }

    /* ---- Chat ---- */
    [data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.045);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 18px;
        padding: 0.9rem 1rem;
        margin-bottom: 0.6rem;
    }
    [data-testid="stChatInput"] textarea {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        border-radius: 16px !important;
        color: #e2e8f0 !important;
    }

    /* ---- Multiselect chips ---- */
    [data-baseweb="tag"] {
        background: rgba(99, 102, 241, 0.22) !important;
        border-radius: 999px !important;
        color: #c7d2fe !important;
    }

    /* ---- Metrics ---- */
    [data-testid="stMetric"] {
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.10);
        border-radius: 16px;
        padding: 0.8rem 1rem;
    }
    [data-testid="stMetric"] label { color: #94a3b8 !important; }
    [data-testid="stMetricValue"] { color: #f1f5f9 !important; }

    /* ---- Info/warning/error boxes ---- */
    .stAlert {
        border-radius: 16px !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        background: rgba(255,255,255,0.05) !important;
        backdrop-filter: blur(12px);
    }

    /* ---- Status pill for sidebar ---- */
    .health-pill {
        display: inline-flex; align-items: center; gap: 8px;
        padding: 6px 14px; border-radius: 999px;
        font-size: 0.78rem; font-weight: 600;
        border: 1px solid rgba(255,255,255,0.14);
        background: rgba(255,255,255,0.06);
        margin: 2px 0;
    }
    .health-pill .dot { width: 8px; height: 8px; border-radius: 50%; }
    .ok .dot { background: #10b981; box-shadow: 0 0 8px #10b981; }
    .bad .dot { background: #ef4444; box-shadow: 0 0 8px #ef4444; }
    .warn .dot { background: #f59e0b; box-shadow: 0 0 8px #f59e0b; }

    /* Source chip row */
    .src-chip {
        display: inline-flex; align-items: center; gap: 6px;
        padding: 4px 12px; margin: 2px 4px 2px 0;
        border-radius: 999px; font-size: 0.78rem;
        border: 1px solid rgba(255,255,255,0.14);
        background: rgba(255,255,255,0.06);
        color: #cbd5e1;
    }
    .src-chip b { color: #f1f5f9; }

    /* Citation cards (used by the chat) */
    .citation-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 0.75rem;
        padding: 1rem;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
        border-left: 4px solid #6366f1;
    }
    .citation-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-color: rgba(99, 102, 241, 0.6);
    }
    .citation-title {
        font-weight: 600;
        font-size: 0.95rem;
        color: #a5b4fc;
        margin-bottom: 0.25rem;
        display: flex;
        justify-content: space-between;
    }
    .citation-score {
        font-size: 0.75rem;
        background: rgba(99, 102, 241, 0.25);
        color: #c7d2fe;
        padding: 0.1rem 0.5rem;
        border-radius: 9999px;
    }
    .citation-content {
        font-size: 0.85rem;
        color: #cbd5e1;
        line-height: 1.5;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

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
    """Starts ingestion for the selected documentation sources."""
    try:
        payload = {"sources": sources or []}
        res = requests.post(
            f"{API_HOST}/api/v1/ingest/",
            json=payload,
            timeout=10,
        )

        if res.status_code != 200:
            st.sidebar.error(f"❌ Error: {res.text}")
            return

        data = res.json()
        st.session_state.ingestion_running = True
        st.session_state.ingestion_message = data.get(
            "message",
            "Ingestion started."
        )
    except requests.exceptions.RequestException as e:
        st.sidebar.error(f"Connection Error: {e}")

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

def upload_files(files, sources=None):
    """Upload files to the backend and start processing for selected sources."""
    files_data = []
    for f in files:
        f.seek(0)
        files_data.append(('files', (f.name, f.getvalue(), f.type or "application/octet-stream")))
    data = {"sources": ",".join(sources or [])}
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
        {"role": "assistant", "content": "Hello! I am your Enterprise OKF Knowledge Assistant. How can I help you today?", "citations": []}
    ]

if "ingestion_running" not in st.session_state:
    st.session_state.ingestion_running = False

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
    st.markdown('<div class="hero-title">📚 OKF Knowledge Base</div>', unsafe_allow_html=True)
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
                        st.session_state.ingestion_running = True
                        st.session_state.upload_success_message = result.get('message', 'Upload successful')
                        st.rerun()
                    else:
                        st.error(f"Upload failed: {response.text}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Connection error: {e}")
        else:
            trigger_ingestion(selected_sources)
            st.rerun()

    if not can_run and st.session_state.ingestion_running:
        st.caption("🔄 Ingestion is already running…")

    st.divider()
    st.caption("Powered by Google OKF, LlamaIndex, and Qdrant.")

# ---------------------------------------------------------------------------
# Main content
# ---------------------------------------------------------------------------
if page == "📚 Knowledge Base":
    render_knowledge_base(is_healthy)
    st.stop()

# Hero header
st.markdown('<div class="hero-title">🧠 OKF Knowledge Retrieval</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Ask questions against your enterprise knowledge base. '
    'Answers are generated using Hybrid Search and strict OKF citations.</div>',
    unsafe_allow_html=True,
)

# Live ingestion dashboard — a self-contained HTML component that polls the API
# itself so counters and charts animate smoothly in the browser.
if st.session_state.ingestion_running:
    render_live_dashboard(API_HOST)

    status = get_ingestion_status()
    if status:
        current_status = status.get("status", "running")
        if current_status in ("completed", "success", "failed", "cancelled"):
            st.session_state.ingestion_running = False
            st.rerun()
    else:
        # Backend unreachable while we think we're running: keep trying briefly
        time.sleep(2)
        st.rerun()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("citations"):
            st.markdown("<div style='margin-top: 10px; font-weight: 600; font-size: 0.9rem;'>📚 Sources Cited:</div>", unsafe_allow_html=True)
            for citation in message["citations"]:
                st.markdown(f"""
                <div class="citation-card" title="Click to read full context">
                    <div class="citation-title">
                        <span>📄 {citation.get('title', 'Unknown OKF Source')}</span>
                        <span class="citation-score">Relevance: {citation.get('score', 0.0)}</span>
                    </div>
                    <div class="citation-content">
                        {citation.get('content', '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)

if prompt := st.chat_input("Ask a question about your documents...", disabled=not is_healthy):

    st.session_state.messages.append({"role": "user", "content": prompt, "citations": []})
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

                message_placeholder.write_stream(simulated_typing_effect(answer))

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "citations": citations,
                })
                st.rerun()
            else:
                st.error(f"API Error {response.status_code}: {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the FastAPI backend. Is the server running?")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
