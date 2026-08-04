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

   ```bash
   cp .env.example .env
   ```

2. Add your Gemini API key to `.env` (get one at https://aistudio.google.com/apikey):
   ```bash
   GEMINI_API_KEY=AIza...
   ```

3. Build and start the services:

   ```bash
   docker compose up --build
   ```

## Access

- Streamlit UI: http://localhost:8501
- FastAPI Docs: http://localhost:8000/docs
