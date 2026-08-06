#!/bin/bash
set -euo pipefail

ROOT_DIR="okf-poc"
mkdir -p "$ROOT_DIR"
cd "$ROOT_DIR"

# Create directories
mkdir -p app/api/routers app/core app/ingestion app/okf app/retrieval app/ui/components \
         config data/raw docs evaluation/results knowledge/source_1 notebooks requirements tests

# Create empty init and gitkeep files
touch app/__init__.py app/api/__init__.py app/api/routers/__init__.py app/core/__init__.py \
      app/ingestion/__init__.py app/okf/__init__.py app/retrieval/__init__.py app/ui/__init__.py \
      app/ui/components/__init__.py tests/__init__.py data/raw/.gitkeep knowledge/.gitkeep \
      knowledge/source_1/.gitkeep

# Create Python scaffold files
touch app/api/main.py app/api/routers/ingest.py app/api/routers/query.py app/core/config.py \
      app/ingestion/loaders.py app/ingestion/metadata_extractor.py app/ingestion/pipeline.py \
      app/okf/parser.py app/okf/formatter.py app/retrieval/hybrid_search.py app/retrieval/query_engine.py \
      app/ui/app.py evaluation/evaluate_ragas.py tests/test_ingestion.py tests/test_retrieval.py

# Create config and docs files
touch config/prompts.yaml config/settings.yaml docs/architecture.md docs/comparative_study.md \
      evaluation/dataset.json notebooks/01_explore_qdrant.ipynb

# Sync text files function
sync_text_file() {
    local FILE="$1"

    touch "$FILE"

    while IFS= read -r line; do

        [ -z "$line" ] && {
            echo >> "$FILE"
            continue
        }

        [[ "$line" =~ ^# ]] && {
            grep -Fxq "$line" "$FILE" || echo "$line" >> "$FILE"
            continue
        }

        grep -Fxq "$line" "$FILE" || echo "$line" >> "$FILE"

    done
}

# Write .gitignore
cat <<'EOF' | sync_text_file .gitignore
# Python
__pycache__/
*.py[cod]
*.class
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

# Write requirements/base.txt
cat <<'EOF' | sync_text_file requirements/base.txt
python-dotenv

pydantic>=2.0.0
pydantic-settings

pyyaml
EOF

# Write requirements/api.txt
cat <<'EOF' | sync_text_file requirements/api.txt
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
# HTML parsing / cleaning / conversion / crawling
beautifulsoup4
lxml
markdownify
httpx
fastembed
llama-index-readers-file
EOF

# Write requirements/ui.txt
cat <<'EOF' | sync_text_file requirements/ui.txt
-r base.txt

streamlit==1.61.1
starlette<1.4.0
requests
EOF

# Write requirements/eval.txt
cat <<'EOF' | sync_text_file requirements/eval.txt
-r api.txt
 
ragas==0.1.9
langchain==0.2.17
langchain-core==0.3.29
langchain-community==0.2.19
langchain-openai==0.2.14
EOF

# Write requirements/dev.txt
cat <<'EOF' | sync_text_file requirements/dev.txt
-r api.txt
-r ui.txt

pytest
pytest-cov

black

ruff

mypy

pre-commit
EOF

#Structured files Fuction
write_if_missing_or_confirm() {
    local FILE="$1"

    if [ -f "$FILE" ]; then
        read -rp "$FILE already exists. Replace it? (y/N): " ans

        [[ "$ans" =~ ^[Yy]$ ]] || return
    fi

    cat > "$FILE"
}

# Write Dockerfile.api
write_if_missing_or_confirm Dockerfile.api <<'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY requirements ./requirements

RUN pip install --no-cache-dir     -r requirements/api.txt

COPY . .

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

# Write Dockerfile.ui
write_if_missing_or_confirm Dockerfile.ui <<'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY requirements ./requirements

RUN pip install --no-cache-dir     -r requirements/ui.txt

COPY . .

CMD ["streamlit", "run", "app/ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
EOF

# Write docker-compose.yml
write_if_missing_or_confirm docker-compose.yml <<'EOF'
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

# Copy env template to active env
cp .env.example .env

echo "OKF scaffold completed successfully in ./${ROOT_DIR}"
echo "Next steps:"
echo "  cd ${ROOT_DIR}"
echo "  docker compose up --build"