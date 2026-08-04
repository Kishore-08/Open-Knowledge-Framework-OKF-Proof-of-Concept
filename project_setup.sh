#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "🚀 Starting OKF PoC Project Scaffold..."

# Define the root directory
ROOT_DIR="okf-poc"

# Create root directory and navigate into it
mkdir -p "$ROOT_DIR"
cd "$ROOT_DIR"

# ----------------------------------------------------
# 1. Create Directories
# ----------------------------------------------------
echo "📁 Creating directories..."

mkdir -p \
    app/api/routers \
    app/ui/components \
    app/okf \
    app/ingestion \
    app/retrieval \
    app/core \
    knowledge/source_1 \
    data/raw \
    evaluation/results \
    notebooks \
    config \
    docs \
    requirements \
    tests

# ----------------------------------------------------
# 2. Create Python Files
# ----------------------------------------------------
echo "📄 Creating Python files..."

touch \
    app/__init__.py \
    app/api/__init__.py \
    app/api/main.py \
    app/api/routers/__init__.py \
    app/api/routers/ingest.py \
    app/api/routers/query.py \
    app/ui/__init__.py \
    app/ui/app.py \
    app/ui/components/__init__.py \
    app/okf/__init__.py \
    app/okf/formatter.py \
    app/okf/parser.py \
    app/ingestion/__init__.py \
    app/ingestion/loaders.py \
    app/ingestion/metadata_extractor.py \
    app/ingestion/pipeline.py \
    app/retrieval/__init__.py \
    app/retrieval/hybrid_search.py \
    app/retrieval/query_engine.py \
    app/core/__init__.py \
    app/core/config.py \
    evaluation/evaluate_ragas.py \
    tests/__init__.py \
    tests/test_ingestion.py \
    tests/test_retrieval.py

# ----------------------------------------------------
# 3. Create Config, Data and Docs Files
# ----------------------------------------------------
echo "📝 Creating config and documentation files..."

touch \
    evaluation/dataset.json \
    config/prompts.yaml \
    config/settings.yaml \
    docs/architecture.md \
    docs/comparative_study.md \
    notebooks/01_explore_qdrant.ipynb

# ----------------------------------------------------
# 4. Create Root-Level Files
# ----------------------------------------------------
echo "⚙️ Creating root configuration files..."

# .gitignore
cat <<EOF > .gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.env
.venv/
venv/
ENV/

# Data & Knowledge
data/raw/*
!data/raw/.gitkeep
knowledge/*
!knowledge/.gitkeep

# IDEs
.vscode/
.idea/
EOF

# Preserve empty folders
touch data/raw/.gitkeep
touch knowledge/.gitkeep

# .env.example
cat <<EOF > .env.example
# Gemini
# Get a free API key at https://aistudio.google.com/apikey
# The llama-index Gemini integration also reads GOOGLE_API_KEY, so either one works,
# but GEMINI_API_KEY is preferred for this project.
GEMINI_API_KEY=your_gemini_api_key_here

# Qdrant
QDRANT_URL=http://qdrant:6333
QDRANT_COLLECTION=okf_knowledge

# FastAPI
API_HOST=http://api:8000
API_PORT=8000

# Models
LLM_MODEL=gemini-2.5-flash
EMBEDDING_MODEL=models/text-embedding-004

# RAG Configuration
TOP_K=5
SPARSE_TOP_K=5
ALPHA=0.5
CHUNK_SIZE=512
CHUNK_OVERLAP=100

# Generation
TEMPERATURE=0.1

# Storage
RAW_DATA_DIR=data/raw
OKF_DATA_DIR=knowledge/source_1

# Environment
ENV=development
LOG_LEVEL=INFO
EOF

# requirements/base.txt
cat <<EOF > requirements/base.txt
python-dotenv

pydantic>=2.0.0
pydantic-settings

pyyaml
EOF

#requirements/api.txt
cat <<EOF > requirements/api.txt
-r base.txt

fastapi>=0.100.0
uvicorn>=0.23.0

llama-index>=0.10.0
llama-index-vector-stores-qdrant
llama-index-llms-gemini
llama-index-embeddings-gemini
google-generativeai
qdrant-client>=1.16.0,<1.19.0

PyMuPDF>=1.23.0
pymupdf

python-docx
openpyxl

fastembed
EOF

#requirements/ui.txt
cat <<EOF > requirements/ui.txt
-r base.txt

streamlit>=1.25.0
requests
EOF

#requirements/eval.txt
cat <<EOF > requirements/eval.txt
-r api.txt
 
ragas==0.1.9
langchain==0.2.17
langchain-core==0.3.29
langchain-community==0.2.19
langchain-openai==0.2.14
EOF

# requirements/dev.txt
cat <<EOF > requirements/dev.txt
-r api.txt
-r ui.txt

pytest
pytest-cov

black

ruff

mypy

pre-commit
EOF

# Dockerfile.api
cat <<EOF > Dockerfile.api
FROM python:3.11-slim

WORKDIR /app

COPY requirements ./requirements

RUN pip install --no-cache-dir \
    -r requirements/api.txt

COPY . .

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

# Dockerfile.ui
cat <<EOF > Dockerfile.ui
FROM python:3.11-slim

WORKDIR /app

COPY requirements ./requirements

RUN pip install --no-cache-dir \
    -r requirements/ui.txt

COPY . .

CMD ["streamlit", "run", "app/ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
EOF

# docker-compose.yml
cat <<EOF > docker-compose.yml
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile.api
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app/app
      - ./knowledge:/app/knowledge
      - ./data:/app/data
      - ./config:/app/config
    env_file:
      - .env
    depends_on:
      - qdrant

  ui:
    build:
      context: .
      dockerfile: Dockerfile.ui
    ports:
      - "8501:8501"
    volumes:
      - ./app:/app/app
    env_file:
      - .env
    depends_on:
      - api

  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  qdrant_data:
EOF

# README.md
cat <<EOF > README.md
# Open Knowledge Framework (OKF) PoC

## Overview

Enterprise knowledge retrieval system utilizing:

- OKF specifications
- LlamaIndex
- Qdrant (Hybrid Search)
- FastAPI
- Streamlit

## Setup

1. Copy the environment file:

   \`\`\`bash
   cp .env.example .env
   \`\`\`

2. Add your Gemini API key to \`.env\` (get one at https://aistudio.google.com/apikey):
   \`\`\`bash
   GEMINI_API_KEY=AIza...
   \`\`\`

3. Build and start the services:

   \`\`\`bash
   docker compose up --build
   \`\`\`

## Access

- Streamlit UI: http://localhost:8501
- FastAPI Docs: http://localhost:8000/docs
EOF

echo ""
echo "✅ Setup complete! Project structure generated in ./$ROOT_DIR"
echo ""
echo "👉 Next steps:"
echo "   cd $ROOT_DIR"
echo "   cp .env.example .env"
echo "   docker compose up --build"