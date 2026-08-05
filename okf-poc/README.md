# Open Knowledge Framework (OKF) Enterprise PoC

This repository contains a complete **Proof of Concept (PoC)** demonstrating how the **Open Knowledge Framework (OKF)** can be utilized alongside **LlamaIndex, Qdrant, FastAPI, and Streamlit** to build a highly accurate, hallucination-resistant **Enterprise AI Knowledge Assistant**.

---

# 🚀 Features

- **Multi-Source Ingestion**
  - Supports parsing PDFs, Markdown, JSON, and raw text.

- **OKF Standardization**
  - Automatically uses an LLM to extract metadata and formats raw data into strict OKF physical files (Markdown + YAML Frontmatter).

- **Hybrid Search**
  - Uses Qdrant to perform simultaneous:
    - Semantic (Dense Vector) Search
    - Keyword (Sparse BM25) Search

- **Strict Citations**
  - Forces the LLM to cite original OKF documents using YAML metadata and renders citation cards in the UI.

- **Automated Evaluation**
  - Includes a complete Ragas evaluation suite to measure:
    - Accuracy
    - Faithfulness
    - Hallucination Rate
    - Context Precision
    - Context Recall

---

# 📁 Project Structure

```text
okf-poc/
├── app/
│   ├── api/                     # FastAPI backend and routers
│   ├── core/                    # Configuration & settings
│   ├── ingestion/               # Document loaders & indexing pipeline
│   ├── okf/                     # OKF Formatter & Parser
│   ├── retrieval/               # Hybrid Search & Query Engine
│   └── ui/                      # Streamlit UI
│
├── config/                      # Prompt templates & system settings
├── data/
│   └── raw/                     # Place raw PDFs, JSON, Markdown here
│
├── docs/                        # Architecture diagrams & reports
├── evaluation/                  # Ragas evaluation scripts
├── knowledge/                   # Generated OKF Markdown files
├── tests/                       # Unit tests
│
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🛠️ Setup & Installation

## Prerequisites

Before starting, ensure the following are installed:

- Docker
- Docker Compose
- Python 3.11+ (only for local evaluation)
- Gemini API Key or OpenAI API Key

---

## 1. Clone the Repository

```bash
git clone https://github.com/your-org/okf-poc.git

cd okf-poc
```

---

## 2. Configure Environment Variables

Copy the example environment file.

```bash
cp .env.example .env
```

Example `.env`

```env
# LLM Provider
LLM_PROVIDER=gemini

# Gemini
GEMINI_API_KEY=your_api_key

# OpenAI (Optional)
OPENAI_API_KEY=

# Models
LLM_MODEL=gemini-2.5-flash
EMBEDDING_MODEL=text-embedding-004

# Qdrant
QDRANT_HOST=qdrant
QDRANT_PORT=6333

# API
API_HOST=0.0.0.0
API_PORT=8000
```

---

## 3. Add Raw Documents

Copy your source documents into:

```text
data/raw/
```

Supported file types:

- PDF
- Markdown
- JSON
- TXT

Example datasets:

- Kubernetes Documentation
- Apache Documentation
- Linux Documentation
- LangChain Documentation

---

## 4. Build & Start Containers

```bash
docker-compose up --build -d
```

This starts:

- FastAPI
- Streamlit
- Qdrant

Verify running containers:

```bash
docker ps
```

---

# 🎮 Usage

## Streamlit UI

Once all containers are running, open:

```
http://localhost:8501
```

### Steps

1. Open the sidebar.
2. Click **Trigger Ingestion Pipeline**.
3. The system will:
   - Read files from `data/raw/`
   - Convert them into OKF Markdown files
   - Save them in `knowledge/`
   - Generate embeddings
   - Store vectors inside Qdrant
4. Ask questions using the chat interface.
5. Observe generated citation cards below every answer.

---

## FastAPI Backend

Swagger Documentation

```
http://localhost:8000/docs
```

### Available Endpoints

#### Trigger Ingestion

```http
POST /api/v1/ingest
```

Converts and indexes documents.

---

#### Query Documents

```http
POST /api/v1/query
```

Example request

```json
{
  "query": "What is a Kubernetes Pod?"
}
```

Example response

```json
{
  "answer": "...",
  "citations": [
    {
      "title": "Pods",
      "source": "kubernetes/docs/concepts/pods.md"
    }
  ]
}
```

---

## Qdrant Dashboard

Inspect vectors and metadata.

```
http://localhost:6333/dashboard
```

You can view:

- Collections
- Vector Payloads
- Metadata
- Stored Documents

---

# 🔄 Ingestion Pipeline

The ingestion workflow follows the pipeline below:

```text
Raw Documents
      │
      ▼
Document Loader
      │
      ▼
Content Extraction
      │
      ▼
Metadata Generation (LLM)
      │
      ▼
OKF Formatter
      │
      ▼
Markdown + YAML
      │
      ▼
Embedding Generation
      │
      ▼
Qdrant Indexing
```

---

# 🔍 Query Pipeline

```text
User Question
      │
      ▼
Embedding Generation
      │
      ▼
Hybrid Retrieval
(Dense + BM25)
      │
      ▼
Relevant OKF Files
      │
      ▼
LLM
      │
      ▼
Answer
      │
      ▼
Citation Mapping
      │
      ▼
Response to User
```

---

# 📊 Running the Evaluation Suite

The project includes a complete **Ragas Evaluation** suite.

It evaluates:

- Faithfulness
- Context Precision
- Context Recall
- Answer Correctness
- Hallucination Rate

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Ensure Services are Running

Make sure:

- Qdrant is running
- FastAPI is running
- Documents have already been ingested

---

## Execute Evaluation

```bash
python evaluation/evaluate_ragas.py
```

---

## Output

Results are generated in:

```text
evaluation/results/
```

Generated files include:

```text
results.csv

results.json

summary.txt
```

---

# 🧪 Running Unit Tests

Execute all unit tests.

```bash
pytest tests/
```

---

# 📂 Generated Knowledge Base

After ingestion, every source document becomes an OKF Markdown file.

Example:

```text
knowledge/

├── kubernetes-pods.md

├── deployments.md

├── services.md
```

Each document contains YAML Frontmatter.

Example:

```yaml
---
title: Kubernetes Pods
category: Kubernetes
source: kubernetes.io
author: CNCF
last_updated: 2025-01-20
tags:
  - kubernetes
  - pods
---
```

---

# 🏗️ Tech Stack

| Layer | Technology |
|---------|------------|
| Backend | FastAPI |
| Frontend | Streamlit |
| Framework | LlamaIndex |
| Vector Database | Qdrant |
| Embeddings | Gemini / OpenAI |
| LLM | Gemini / OpenAI |
| Evaluation | Ragas |
| Containerization | Docker |
| API Docs | Swagger |
| Configuration | Pydantic |

---

# 📈 Future Improvements

- Multi-user Authentication
- Role-Based Access Control (RBAC)
- Incremental Document Ingestion
- Scheduled Re-indexing
- Multi-Tenant Knowledge Bases
- Feedback Collection
- Analytics Dashboard
- Source Ranking
- Metadata Validation
- Redis Caching
- Kubernetes Deployment
- CI/CD Pipeline
- Monitoring with Prometheus & Grafana

---

# 📄 License

This project is intended as an Enterprise Proof of Concept for demonstrating the capabilities of the Open Knowledge Framework (OKF), Retrieval-Augmented Generation (RAG), and Hybrid Search architectures.

---

# 👨‍💻 Author

**Kishore Kumar K**

Enterprise AI | DevOps | Cloud | Kubernetes | LLM Engineering

---