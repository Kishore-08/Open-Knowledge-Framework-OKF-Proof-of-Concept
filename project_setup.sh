#!/bin/bash

# OKF PoC Project Scaffold Script
# Usage: ./scaffold.sh [--force]

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuration
ROOT_DIR="okf-poc"
FORCE=false

if [[ "${1:-}" == "--force" ]]; then
    FORCE=true
    echo -e "${YELLOW}Running in FORCE mode. Files will be backed up before overwrite.${NC}"
fi

echo -e "${BLUE}Starting OKF PoC Project Scaffold...${NC}"

mkdir -p "$ROOT_DIR"
cd "$ROOT_DIR"

# Create or update files safely
create_or_update_file() {
    local target_file="$1"
    local tmp_file

    tmp_file=$(mktemp)
    cat > "$tmp_file"

    mkdir -p "$(dirname "$target_file")"

    if [[ ! -f "$target_file" ]]; then
        mv "$tmp_file" "$target_file"
        echo -e "${GREEN}Created:${NC} $target_file"
    else
        if cmp -s "$tmp_file" "$target_file"; then
            echo -e "${BLUE}Up to date:${NC} $target_file"
            rm "$tmp_file"
        else
            if [[ "$FORCE" == true ]]; then
                cp "$target_file" "${target_file}.bak"
                mv "$tmp_file" "$target_file"
                echo -e "${YELLOW}Updated:${NC} $target_file (backup created)"
            else
                echo -e "${YELLOW}Skipped:${NC} $target_file (manual changes detected)"
                rm "$tmp_file"
            fi
        fi
    fi
}

# Create empty files
create_empty_file() {
    local target_file="$1"

    mkdir -p "$(dirname "$target_file")"

    if [[ ! -f "$target_file" ]]; then
        touch "$target_file"
        echo -e "${GREEN}Created:${NC} $target_file"
    else
        echo -e "${BLUE}Exists:${NC} $target_file"
    fi
}

# Directories
DIRECTORIES=(
    "app/api/routers"
    "app/core"
    "app/ingestion"
    "app/okf"
    "app/retrieval"
    "app/ui/components"
    "config"
    "data/raw"
    "docs"
    "evaluation/results"
    "knowledge/source_1"
    "notebooks"
    "requirements"
    "tests"
)

echo -e "\n${BLUE}Creating directories...${NC}"

for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$dir"
done

# Python files
PYTHON_FILES=(
    "app/__init__.py"
    "app/api/__init__.py"
    "app/api/main.py"
    "app/api/routers/__init__.py"
    "app/api/routers/ingest.py"
    "app/api/routers/query.py"
    "app/core/__init__.py"
    "app/core/config.py"
    "app/ingestion/__init__.py"
    "app/ingestion/loaders.py"
    "app/ingestion/metadata_extractor.py"
    "app/ingestion/pipeline.py"
    "app/okf/__init__.py"
    "app/okf/formatter.py"
    "app/okf/parser.py"
    "app/retrieval/__init__.py"
    "app/retrieval/hybrid_search.py"
    "app/retrieval/query_engine.py"
    "app/ui/__init__.py"
    "app/ui/app.py"
    "app/ui/components/__init__.py"
    "evaluation/evaluate_ragas.py"
    "tests/__init__.py"
    "tests/test_ingestion.py"
    "tests/test_retrieval.py"
)

echo -e "\n${BLUE}Creating Python files...${NC}"

for file in "${PYTHON_FILES[@]}"; do
    create_empty_file "$file"
done

# Empty files
EMPTY_FILES=(
    "config/prompts.yaml"
    "config/settings.yaml"
    "data/raw/.gitkeep"
    "docs/architecture.md"
    "docs/comparative_study.md"
    "evaluation/dataset.json"
    "knowledge/.gitkeep"
    "knowledge/source_1/.gitkeep"
    "notebooks/01_explore_qdrant.ipynb"
)

echo -e "\n${BLUE}Creating config and documentation files...${NC}"

for file in "${EMPTY_FILES[@]}"; do
    create_empty_file "$file"
done

# Root files

create_or_update_file ".gitignore" <<'EOF'
__pycache__/
*.py[cod]
*.env
.venv/
venv/
ENV/
.pytest_cache/
.ruff_cache/
.mypy_cache/

data/raw/*
!data/raw/.gitkeep

knowledge/*
!knowledge/.gitkeep
!knowledge/source_1/.gitkeep

.vscode/
.idea/
EOF


create_or_update_file ".env.example" <<'EOF'
GEMINI_API_KEY=your_gemini_api_key_here

QDRANT_URL=http://qdrant:6333
QDRANT_COLLECTION=okf_knowledge

API_HOST=http://api:8000
API_PORT=8000

LLM_MODEL=gemini-2.5-flash
EMBEDDING_MODEL=models/text-embedding-004

TOP_K=5
SPARSE_TOP_K=5
ALPHA=0.5
CHUNK_SIZE=512
CHUNK_OVERLAP=100

TEMPERATURE=0.1

RAW_DATA_DIR=data/raw
OKF_DATA_DIR=knowledge/source_1

ENV=development
LOG_LEVEL=INFO
EOF


create_or_update_file "requirements/base.txt" <<'EOF'
python-dotenv
pydantic>=2.0.0
pydantic-settings
pyyaml
EOF


create_or_update_file "requirements/api.txt" <<'EOF'
-r base.txt

fastapi>=0.100.0
uvicorn>=0.23.0

llama-index>=0.10.0
llama-index-readers-file
llama-index-vector-stores-qdrant
llama-index-llms-gemini
llama-index-embeddings-gemini

google-generativeai
qdrant-client>=1.16.0,<1.19.0
PyMuPDF>=1.23.0
python-docx
openpyxl
fastembed
EOF


create_or_update_file "requirements/ui.txt" <<'EOF'
-r base.txt

streamlit>=1.49.1
requests
EOF


create_or_update_file "requirements/eval.txt" <<'EOF'
-r api.txt

ragas==0.1.9
langchain==0.2.17
langchain-core==0.3.29
langchain-community==0.2.19
langchain-openai==0.2.14
EOF


create_or_update_file "requirements/dev.txt" <<'EOF'
-r api.txt
-r ui.txt

pytest
pytest-cov
black
ruff
mypy
pre-commit
EOF


create_or_update_file "Dockerfile.api" <<'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY requirements ./requirements

RUN pip install --no-cache-dir -r requirements/api.txt

COPY . .

CMD ["uvicorn","app.api.main:app","--host","0.0.0.0","--port","8000"]
EOF


create_or_update_file "Dockerfile.ui" <<'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY requirements ./requirements

RUN pip install --no-cache-dir -r requirements/ui.txt

COPY . .

CMD ["streamlit","run","app/ui/app.py","--server.port=8501","--server.address=0.0.0.0"]
EOF


create_or_update_file "docker-compose.yml" <<'EOF'
version: "3.8"

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


echo -e "\n${GREEN}OKF PoC scaffold completed.${NC}"

echo -e "\n${BLUE}Next steps:${NC}"
echo "cd $ROOT_DIR"
echo "cp .env.example .env"
echo "docker compose up --build"