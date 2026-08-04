Open Knowledge Framework (OKF) - System Architecture

This document details the architecture, components, and data flows of the OKF Enterprise Proof of Concept.

1. High-Level System Architecture

The system is designed as a containerized, microservice-based architecture to ensure scalability and separation of concerns.

graph TB
    subgraph "Docker Compose Environment"
        
        subgraph "Frontend Layer"
            UI["Streamlit UI (Port: 8501)"]
        end

        subgraph "Backend API Layer"
            API["FastAPI Backend (Port: 8000)"]
            Router["API Routers (/ingest, /query)"]
        end
        
        subgraph "Knowledge Processing Engine"
            Orchestrator["LlamaIndex Orchestrator"]
            OKF_Core["OKF Converter Engine"]
        end

        subgraph "Storage Layer"
            Qdrant[("Qdrant Vector DB<br/>(Port: 6333)")]
            LocalVol[("Local File System<br/>(Physical OKF .md files)")]
        end

    end

    ExternalLLM(("External LLM API<br/>(OpenAI / Gemini)"))
    RawData[/"Raw Data Sources<br/>(PDF, JSON, MD)"/]
    User(("End User"))

    %% Connections
    User <-->|HTTP Chat| UI
    UI <-->|REST API| API
    API --> Router
    Router --> Orchestrator
    Router --> OKF_Core
    RawData -->|Upload| API
    
    Orchestrator <-->|Embeddings/Completion| ExternalLLM
    OKF_Core <-->|Metadata Extraction| ExternalLLM
    
    Orchestrator <-->|Hybrid Search| Qdrant
    OKF_Core -->|Save standardized files| LocalVol
    Orchestrator -->|Read chunk context| LocalVol


2. Component Breakdown

Component

Technology

Purpose

Frontend UI

Streamlit

Provides an interactive chat interface. Parses backend responses to render AI answers and interactive "Citation Cards" showing OKF sources.

Backend API

FastAPI

High-performance async REST API. Exposes endpoints for UI consumption and handles data validation via Pydantic.

Data Orchestration

LlamaIndex

Handles document chunking (SentenceSplitter), prompt construction, and LLM communication.

OKF Engine

Custom Python

Extracts metadata via LLM, formats text into OKF standard (Markdown + YAML), and writes physical files to disk to prevent vendor lock-in.

Vector Database

Qdrant

Stores dense vector embeddings and sparse BM25 vectors. Crucially, it stores the OKF YAML data as JSON payloads to enable rapid metadata filtering.

3. Data Workflows

3.1 Knowledge Ingestion Workflow

This process describes how raw, unstructured data becomes searchable OKF knowledge.

sequenceDiagram
    autonumber
    participant Raw as Raw Document
    participant Load as Loaders (PyMuPDF)
    participant OKF as OKF Engine
    participant LLM as External LLM
    participant Disk as Local Storage
    participant Llama as LlamaIndex
    participant Qdrant as Vector DB

    Raw->>Load: Read raw text
    Load->>OKF: Pass unformatted text
    OKF->>LLM: Prompt: Extract Title, Topics, Type
    LLM-->>OKF: Return JSON Metadata
    OKF->>OKF: Assemble Markdown + YAML Frontmatter
    OKF->>Disk: Save physical 'document.md'
    Llama->>Disk: Read 'document.md'
    Llama->>Llama: Chunk text (512 tokens)
    Llama->>Llama: Attach YAML metadata to every chunk
    Llama->>Qdrant: Upsert Vectors + OKF Metadata Payload


3.2 Retrieval & Reasoning Workflow (RAG)

This process describes how a user query is resolved using Hybrid Search and strict anti-hallucination prompting.

flowchart TD
    A([User Query]) --> B(FastAPI /query)
    B --> C[LlamaIndex Query Engine]
    
    C --> D[(Qdrant DB)]
    
    subgraph "Hybrid Search"
        D -->|Dense Match| E[Semantic Results]
        D -->|Sparse Match| F[Keyword Results]
        E & F --> G{Reciprocal Rank Fusion}
    end
    
    G -->|Top-K OKF Chunks| H[Prompt Builder]
    H -->|Inject Context & Enforce Citations| I((LLM))
    
    I --> J[Generated Answer]
    I --> K[Extracted Citations]
    
    J & K --> L(FastAPI Response)
    L --> M([Streamlit UI])


4. Key Design Decisions

Physical File Storage: By saving OKF documents as .md files to the disk before indexing, we ensure the enterprise retains human-readable, framework-agnostic copies of all knowledge.

Hybrid Search Integration: Relying solely on vector similarity fails for enterprise acronyms and specific IDs. Qdrant's BM25 sparse vectors solve this.

Strict Prompts: The LLM is explicitly instructed to cite the YAML title field and state "I cannot answer this" if the OKF context lacks the answer. This is verified by the Ragas Evaluation suite.