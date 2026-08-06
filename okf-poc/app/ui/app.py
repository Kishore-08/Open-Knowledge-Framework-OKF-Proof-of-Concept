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
    """Calls the FastAPI ingestion endpoint."""
    try:
        with st.spinner("Processing documents, extracting OKF metadata, and generating embeddings..."):
            payload = {"raw_dir": "data/raw", "okf_dir": "knowledge/source_1"}
            res = requests.post(f"{API_HOST}/api/v1/ingest/", json=payload, timeout=600)
            
            if res.status_code == 200:
                data = res.json()
                st.sidebar.success(f"✅ Success! Indexed {data.get('indexed_documents')} documents.")
            else:
                st.sidebar.error(f"❌ Error: {res.text}")
    except Exception as e:
        st.sidebar.error(f"Connection Error: {e}")

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
    st.markdown("Drop files into `data/raw`, then click below to convert them to OKF Standard and push to Qdrant.")
    st.caption("Supported formats: PDF (.pdf), Markdown (.md), plain text (.txt), JSON (.json). "
               "Keep files small and well-structured so ingestion stays fast.")
    if st.button("🚀 Trigger Ingestion Pipeline", disabled=not is_healthy, use_container_width=True):
        trigger_ingestion()

    st.divider()
    st.caption("Powered by Google OKF, LlamaIndex, and Qdrant.")

if page == "📚 Knowledge Base":
    render_knowledge_base(is_healthy)
    st.stop()

st.title("🧠 OKF Knowledge Retrieval")
st.markdown("Ask questions against your enterprise knowledge base. Answers are generated using Hybrid Search and strict OKF citations.")

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