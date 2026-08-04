Open Knowledge Framework (OKF) Enterprise PoC

This repository contains a complete Proof of Concept (PoC) demonstrating how the Open Knowledge Framework (OKF) can be utilized alongside LlamaIndex, Qdrant, FastAPI, and Streamlit to build a highly accurate, hallucination-resistant Enterprise AI Knowledge Assistant.

🚀 Features

Multi-Source Ingestion: Supports parsing PDFs, Markdown, JSON, and raw text.

OKF Standardization: Automatically uses an LLM to extract metadata and formats raw data into strict OKF physical files (Markdown + YAML frontmatter).

Hybrid Search: Leverages Qdrant to perform simultaneous Semantic (Dense Vector) and Keyword (Sparse BM25) searches for maximum retrieval accuracy.

Strict Citations: Enforces the LLM to cite its sources using the OKF YAML metadata, rendering beautiful citation cards in the UI.

Automated Evaluation: Includes a full Ragas evaluation suite to measure hallucination rates and accuracy against a 20-question ground-truth dataset.

📁 Project Structure

okf-poc/
├── app/
│   ├── api/          # FastAPI backend and routers
│   ├── core/         # Pydantic configuration
│   ├── ingestion/    # Document loaders and LlamaIndex orchestration
│   ├── okf/          # OKF Formatter and Parser logic
│   ├── retrieval/    # Hybrid search and Query Engine
│   └── ui/           # Streamlit conversational interface
├── config/           # Prompts and system settings
├── data/raw/         # Drop raw PDFs/files here for ingestion
├── docs/             # PoC reports and architecture diagrams
├── evaluation/       # 20-question dataset and Ragas scoring script
├── knowledge/        # The destination folder for generated OKF .md files
├── tests/            # Unit tests for core logic
└── docker-compose.yml


🛠️ Setup and Installation

Prerequisites

Docker & Docker Compose

An OpenAI API Key (or Gemini API Key, configurable in app/core/config.py)

1. Configure Environment

Clone the repository and set up your environment variables.

git clone https://github.com/your-org/okf-poc.git
cd okf-poc
cp .env.example .env


Open the .env file and insert your OPENAI_API_KEY.

2. Add Raw Data

Place your sample documents (PDFs, JSON, text files) into the data/raw/ directory. (A subset of Kubernetes documentation is recommended for testing).

3. Spin up the Containers

Run the following command to build the FastAPI, Streamlit, and Qdrant containers.

docker-compose up --build -d


🎮 Usage

The Streamlit UI

Once the containers are running, access the conversational interface at:
👉 http://localhost:8501

Open the left sidebar in the UI.

Click "Trigger Ingestion Pipeline". This will read your files in data/raw/, convert them to OKF format in knowledge/, and index them into Qdrant.

Once complete, use the chat interface to ask questions about your documents. Observe the generated OKF Citation cards beneath the answers.

The FastAPI Backend

The API documentation (Swagger UI) is available at:
👉 http://localhost:8000/docs

POST /api/v1/ingest/: Triggers the OKF conversion and indexing pipeline.

POST /api/v1/query/: Accepts a JSON payload {"query": "your question"} and returns the LLM answer with mapped citations.

The Qdrant Dashboard

You can visually inspect your generated vectors and OKF metadata payloads at:
👉 http://localhost:6333/dashboard

📊 Running the Evaluation Suite

To prove the system meets the 80% accuracy requirement, you can run the automated Ragas evaluation script.

Note: You must have Python installed locally to run this script outside of Docker.

Install the required dependencies locally:

pip install -r requirements.txt


Ensure your Docker containers (specifically Qdrant) are running and that you have ingested the documents via the UI.

Execute the evaluation script:

python evaluation/evaluate_ragas.py


The script will query the system 20 times, score the results, and output a CSV and JSON summary into the evaluation/results/ folder.

🧪 Running Unit Tests

To run the unit tests (which mock the LLM and Database calls to ensure pure logic verification):

pytest tests/
