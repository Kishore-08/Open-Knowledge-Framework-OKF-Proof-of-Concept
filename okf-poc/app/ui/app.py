import streamlit as st
import requests
import os
import time

# Page configuration MUST be the first Streamlit command
st.set_page_config(
    page_title="OKF Knowledge Assistant",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# This CSS provides a highly polished, modern 2026 aesthetic with animations and glassmorphism
st.markdown("""
<style>
    /* Global Typography and Background */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* Modern Chat Bubble Styling */
    .stChatMessage {
        border-radius: 1rem;
        padding: 1rem;
        margin-bottom: 1rem;
        animation: fadeIn 0.5s ease-out forwards;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }
    
    /* User Message Bubble */
    [data-testid="chatAvatarIcon-user"] {
        background-color: #3b82f6 !important;
    }
    
    /* Assistant Message Bubble */
    [data-testid="chatAvatarIcon-assistant"] {
        background-color: #10b981 !important;
    }

    /* Citation Cards (Glassmorphism & Hover Effects) */
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
        border-left: 4px solid #3b82f6;
    }
    
    .citation-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-color: rgba(59, 130, 246, 0.5);
    }
    
    .citation-title {
        font-weight: 600;
        font-size: 0.95rem;
        color: #60a5fa;
        margin-bottom: 0.25rem;
        display: flex;
        justify-content: space-between;
    }
    
    .citation-score {
        font-size: 0.75rem;
        background: #1e3a8a;
        color: #bfdbfe;
        padding: 0.1rem 0.5rem;
        border-radius: 9999px;
    }
    
    .citation-content {
        font-size: 0.85rem;
        color: #d1d5db;
        line-height: 1.5;
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.5); }
        70% { box-shadow: 0 0 0 10px rgba(59, 130, 246, 0); }
        100% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
    }
    
    /* Primary Button Styling */
    .stButton > button {
        border-radius: 0.5rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    .stButton > button:hover {
        animation: pulse-glow 1.5s infinite;
        border-color: #3b82f6 !important;
        color: #3b82f6 !important;
    }
</style>
""", unsafe_allow_html=True)

# Determine API Host (Docker sets this to http://api:8000, local dev defaults to localhost)
API_HOST = os.getenv("API_HOST", "http://localhost:8000")

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Enterprise OKF Knowledge Assistant. How can I help you today?", "citations": []}
    ]

if "ingestion_running" not in st.session_state:
    st.session_state.ingestion_running = False

if "ingestion_message" not in st.session_state:
    st.session_state.ingestion_message = ""

def check_api_health():
    """Pings the FastAPI health endpoint and returns its parsed checks (or None)."""
    try:
        res = requests.get(f"{API_HOST}/health", timeout=2)
        if res.status_code != 200:
            return None
        return res.json()
    except requests.exceptions.RequestException:
        return None

def trigger_ingestion():
    """Starts ingestion and displays live backend progress."""
    try:
        # No hardcoded paths here: let the API fall back to its own settings
        # (CACHE_DIR / KNOWLEDGE_DIR) so the UI never disagrees with the
        # backend about where the disposable cache or the knowledge source of
        # truth live.
        payload = {}

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

def simulated_typing_effect(text):
    """Simulates a typewriter effect for better UX."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)


def render_knowledge_base(is_healthy: bool):
    """Knowledge Base browser: categories, concept list, metadata, and full content."""
    st.title("📚 OKF Knowledge Base")
    st.markdown("Browse the curated OKF knowledge repository. Each concept is a Markdown file with YAML metadata and links back to its official source.")

    if not is_healthy:
        st.warning("Backend offline: showing any locally cached repository data is unavailable. Start the API to browse the knowledge base.")
        return

    # Stats
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
            if cats:
                st.markdown("**Per-category distribution:**")
                st.json(cats)
    except requests.exceptions.RequestException:
        st.error("Could not reach the knowledge base API.")

    st.divider()

    # Search
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

    # Browse by category
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

    # Index stats
    st.divider()
    st.markdown("### Vector index status")
    st.caption(
        "Concepts are indexed into Qdrant (`okf_concepts`) with hybrid search. "
        "Run `python -m scripts.build_index` to rebuild the index after adding concepts."
    )

with st.sidebar:
    st.title("⚙️ OKF Control Panel")
    st.markdown("Manage your Open Knowledge Framework pipeline.")
    
    st.divider()
    
    # System Status
    st.subheader("System Status")
    health = check_api_health()
    is_healthy = health is not None
    if health:
        checks = health.get("checks", {})
        qdrant_ok = checks.get("qdrant", {}).get("ok", False)
        llm_ok = checks.get("llm", {}).get("ok", False)
        st.markdown(f"**FastAPI Backend:** {'Online' if health.get('status') == 'healthy' else 'Degraded'}")
        st.markdown(f"**Qdrant Vector DB:** {'Connected' if qdrant_ok else 'Disconnected'}")
        if not qdrant_ok:
            st.error("Qdrant is not reachable. Start the qdrant container (`docker compose up -d qdrant`).")
        if not llm_ok:
            st.warning("GEMINI_API_KEY is not set. Answers will list sources but skip AI generation.")
    else:
        st.markdown("**FastAPI Backend:** Offline")
        st.error("Cannot connect to API. Please ensure Docker containers are running.")
        
    st.divider()
    
    # Navigation
    st.subheader("Navigation")
    page = st.radio("View", ["💬 Chat Assistant", "📚 Knowledge Base"], index=0)
    
    st.divider()
    
    # Ingestion Controls
    st.subheader("Knowledge Ingestion")
    
    # Initialize upload state
    if "uploaded_files_list" not in st.session_state:
        st.session_state.uploaded_files_list = []
    if "upload_success_message" not in st.session_state:
        st.session_state.upload_success_message = ""
    
    st.markdown("""
    <style>
    /* Upload Area Glassmorphism */
    .upload-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 2px dashed rgba(96, 165, 250, 0.3);
        border-radius: 1.25rem;
        padding: 2.5rem 2rem;
        text-align: center;
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    
    .upload-container:hover {
        border-color: rgba(96, 165, 250, 0.6);
        background: rgba(255, 255, 255, 0.05);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.1);
    }
    
    .upload-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.7;
    }
    
    .upload-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #bfdbfe;
        margin-bottom: 0.5rem;
    }
    
    .upload-subtitle {
        font-size: 0.95rem;
        color: #9ca3af;
        margin-bottom: 1rem;
    }
    
    .upload-formats {
        font-size: 0.85rem;
        color: #6b7280;
        font-family: 'Courier New', monospace;
    }
    
    /* File List Card */
    .file-card {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(96, 165, 250, 0.2);
        border-radius: 0.75rem;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: all 0.2s ease;
    }
    
    .file-card:hover {
        border-color: rgba(96, 165, 250, 0.4);
        transform: translateX(4px);
    }
    
    .file-info {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .file-icon {
        font-size: 1.5rem;
    }
    
    .file-name {
        font-weight: 500;
        color: #d1d5db;
    }
    
    .file-size {
        font-size: 0.8rem;
        color: #9ca3af;
        margin-left: 0.5rem;
    }
    
    /* Success Message */
    .success-card {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(5, 150, 105, 0.05));
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 0.75rem;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .success-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #34d399;
        margin-bottom: 0.5rem;
    }
    
    .success-details {
        font-size: 0.9rem;
        color: #d1d5db;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # File uploader with custom styling
    uploaded_files = st.file_uploader(
        "Choose files to upload",
        type=['pdf', 'md', 'txt', 'json'],
        accept_multiple_files=True,
        help="Supported formats: PDF, Markdown, Text, JSON (max 50MB per file)",
        label_visibility="collapsed"
    )
    
    # Display upload area with glassmorphism
    if not uploaded_files:
        st.markdown("""
        <div class="upload-container">
            <div class="upload-icon">☁️</div>
            <div class="upload-title">Upload Knowledge Documents</div>
            <div class="upload-subtitle">Drag & drop files or click Browse above</div>
            <div class="upload-formats">PDF · MD · TXT · JSON</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Display selected files
    if uploaded_files:
        st.markdown("<div style='margin-top: 1rem;'><strong>📁 Selected Documents</strong></div>", unsafe_allow_html=True)
        
        for file in uploaded_files:
            file_size_mb = len(file.getvalue()) / (1024 * 1024)
            file_size_str = f"{file_size_mb:.2f} MB" if file_size_mb >= 1 else f"{len(file.getvalue()) / 1024:.2f} KB"
            
            # Determine file icon
            ext = Path(file.name).suffix.lower()
            icon_map = {'.pdf': '📄', '.md': '📝', '.txt': '📃', '.json': '📊'}
            icon = icon_map.get(ext, '📄')
            
            st.markdown(f"""
            <div class="file-card">
                <div class="file-info">
                    <span class="file-icon">{icon}</span>
                    <span class="file-name">{file.name}</span>
                    <span class="file-size">{file_size_str}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Process button
        col1, col2 = st.columns([3, 1])
        with col2:
            process_button = st.button(
                "✨ Process Documents",
                use_container_width=True,
                disabled=not is_healthy or st.session_state.ingestion_running,
                type="primary"
            )
        
        if process_button:
            # Upload files via API
            try:
                with st.spinner("🔄 Uploading files..."):
                    files_data = []
                    for file in uploaded_files:
                        file.seek(0)  # Reset file pointer
                        files_data.append(
                            ('files', (file.name, file.getvalue(), file.type))
                        )
                    
                    response = requests.post(
                        f"{API_HOST}/api/v1/ingest/upload",
                        files=files_data,
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.session_state.ingestion_running = True
                        st.session_state.upload_success_message = result.get('message', 'Upload successful')
                        
                        # Show success message
                        st.markdown(f"""
                        <div class="success-card">
                            <div class="success-title">✅ Upload Successful</div>
                            <div class="success-details">
                                {result.get('uploaded_files', 0)} file(s) uploaded<br/>
                                Processing started in background...
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error(f"Upload failed: {response.text}")
            
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    
    # Show success message if exists
    if st.session_state.upload_success_message and not st.session_state.ingestion_running:
        st.success(st.session_state.upload_success_message)
        if st.button("Clear"):
            st.session_state.upload_success_message = ""
            st.rerun()
    
    # Legacy ingestion trigger (for files already in cache)
    st.divider()
    st.caption("Or process files already in cache directory:")
    if st.button(
        "🚀 Trigger Pipeline (Cache Files)",
        disabled=not is_healthy or st.session_state.ingestion_running,
        use_container_width=True,
    ):
        trigger_ingestion()
        st.rerun()

    if st.session_state.ingestion_running:
        status = get_ingestion_status()

        if status:
            current_status = status.get("status", "running")

            # Dedicated side-panel placement for the live ingestion telemetry.
            st.markdown(
                """
                <style>
                .okf-top-telemetry {
                    margin-top: 0.9rem;
                    border-radius: 0.80rem;
                    border: 1px solid rgba(96, 165, 250, 0.35);
                    padding: 0.75rem;
                    background: linear-gradient(180deg, rgba(15, 23, 42, 0.95), rgba(30, 41, 59, 0.90));
                }
                .okf-top-telemetry .subheader {
                    font-weight: 700;
                    font-size: 0.88rem;
                    margin-bottom: 0.25rem;
                }
                </style>
                """,
                unsafe_allow_html=True,
            )

            with st.container():
                st.markdown("### 📊 Ingestion Progress")

                if current_status in ("completed", "success"):
                    st.success("✅ Ingestion completed")
                    st.session_state.ingestion_running = False

                elif current_status == "failed":
                    st.error(
                        f"❌ Ingestion failed: "
                        f"{status.get('error', 'Unknown error')}"
                    )
                    st.session_state.ingestion_running = False

                else:
                    st.info("🔄 Ingestion in progress...")

                col1, col2, col3, col4 = st.columns(4)

                col1.metric(
                    "Discovered",
                    status.get("discovered", 0),
                )

                col2.metric(
                    "Fetched",
                    status.get("fetched", 0),
                )

                col3.metric(
                    "Processed",
                    status.get("processed", 0),
                )

                col4.metric(
                    "Failed",
                    status.get("failed", 0),
                )

                if status.get("indexed_documents") is not None:
                    st.metric(
                        "Indexed",
                        status.get("indexed_documents", 0),
                    )

                total_docs = status.get("total_documents") or 0
                processed_docs = status.get("processed") or 0
                if total_docs:
                    progress_value = min(100, max(0, int(round((processed_docs / total_docs) * 100))))
                elif status.get("status") in {"completed", "success"}:
                    progress_value = 100
                else:
                    progress_value = status.get("progress_percent", 0) or 0

                st.subheader("📈 Live Progress")
                st.progress(progress_value / 100.0, text=f"{progress_value}% complete")

                token_bar = {
                    "Prompt": status.get("prompt_tokens_estimate", 0) or 0,
                    "Completion": status.get("completion_tokens_estimate", 0) or 0,
                }
                st.markdown("### Token Consumption Estimate")
                st.bar_chart(token_bar)
                st.caption(
                    f"Estimated token usage: {status.get('total_tokens_estimate', 0) or 0} / "
                    f"{max(total_docs, 1)} document(s)"
                )

                if st.session_state.ingestion_running:
                    time.sleep(2)
                    st.rerun()

    st.divider()
    st.caption("Powered by Google OKF, LlamaIndex, and Qdrant.")

if page == "📚 Knowledge Base":
    render_knowledge_base(is_healthy)
    st.stop()

st.title("🧠 OKF Knowledge Retrieval")
st.markdown("Ask questions against your enterprise knowledge base. Answers are generated using Hybrid Search and strict OKF citations.")

# Top-right telemetry overlay for the current ingestion cycle. Streamlit does not
# expose a true absolute top-right layout element, so this is the nearest stable
# contract: a right-hand, compact, progress-only panel that appears in the main
# page area whenever a background ingestion is visible to the API.
if st.session_state.ingestion_running:
    status = get_ingestion_status() or {}
    progress_value = status.get("progress_percent") or 0
    if not progress_value and status.get("total_documents"):
        processed_docs = status.get("processed") or 0
        total_docs = status.get("total_documents") or 1
        progress_value = min(100, int(round((processed_docs / total_docs) * 100)))

    st.markdown(
        """
        <style>
        .okf-right-telemetry {
            position: fixed;
            z-index: 10;
            top: 6rem;
            right: 1rem;
            width: min(26rem, 36vw);
            border-radius: 0.9rem;
            padding: 0.85rem 1.0rem;
            background: rgba(15, 23, 42, 0.96);
            border: 1px solid rgba(125, 211, 252, 0.55);
            box-shadow: 0 8px 18px rgba(0,0,0,0.16);
        }
        .okf-right-telemetry .label {
            font-size: 0.70rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: #93c5fd;
        }
        .okf-right-telemetry .big {
            font-size: 1.2rem;
            font-weight: 700;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown(
            f"""
            <div class="okf-right-telemetry">
                <div class="label">Ingestion Telemetry</div>
                <div class="big">{status.get('status', 'running').title()}</div>
                <div style="margin-top: 0.4rem;">
                    <div class="label">Progress</div>
                    <div style="margin-top: 0.2rem;">{status.get('processed', 0)} / {status.get('total_documents') or max(status.get('processed', 0), 1)} processed</div>
                </div>
                <div style="margin-top: 0.4rem;">
                    <div class="label">Token Estimate</div>
                    <div style="margin-top: 0.2rem;">Prompt {status.get('prompt_tokens_estimate', 0) or 0} &middot; Completion {status.get('completion_tokens_estimate', 0) or 0}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Render Citations if they exist
        if message.get("citations"):
            st.markdown("<div style='margin-top: 10px; font-weight: 600; font-size: 0.9rem;'>📚 Sources Cited:</div>", unsafe_allow_html=True)
            for citation in message["citations"]:
                # Custom HTML for beautiful citation cards
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
    
    # Add user message to state and UI
    st.session_state.messages.append({"role": "user", "content": prompt, "citations": []})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call FastAPI Backend
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Show a temporary thinking state
            with st.spinner("Performing Hybrid Search and reasoning over OKF documents..."):
                response = requests.post(
                    f"{API_HOST}/api/v1/query/", 
                    json={"query": prompt},
                    timeout=120
                )
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get("answer", "No answer generated.")
                citations = data.get("citations", [])
                
                # Stream the text output for better UX
                message_placeholder.write_stream(simulated_typing_effect(answer))
                
                # Save to session state
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer,
                    "citations": citations
                })
                
                # Force a rerun to render the beautiful custom HTML citation cards
                st.rerun()
                
            else:
                st.error(f"API Error {response.status_code}: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the FastAPI backend. Is the server running?")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")