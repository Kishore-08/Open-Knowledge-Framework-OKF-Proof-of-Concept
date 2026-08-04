#!/bin/bash

set -e

echo "===================================================="
echo "🚀 Starting OKF PoC Docker Setup"
echo "===================================================="

PROJECT_DIR="okf-poc"

# -------------------------------------------------------
# Check Required Tools
# -------------------------------------------------------

echo ""
echo "🔍 Checking prerequisites..."

if ! command -v docker >/dev/null 2>&1; then
    echo "❌ Docker is not installed."
    echo "Please install Docker Desktop or Docker Engine."
    exit 1
fi

echo "✅ Docker found"

if ! docker compose version >/dev/null 2>&1; then
    echo "❌ Docker Compose is not installed."
    exit 1
fi

echo "✅ Docker Compose found"

if ! command -v curl >/dev/null 2>&1; then
    echo "❌ curl is required but not installed."
    exit 1
fi

echo "✅ curl found"

# -------------------------------------------------------
# Move into Project
# -------------------------------------------------------

if [ ! -d "$PROJECT_DIR" ]; then
    echo ""
    echo "❌ Project directory '$PROJECT_DIR' not found."
    echo "Run the project scaffold script first."
    exit 1
fi

cd "$PROJECT_DIR"

echo "✅ Project directory found"

# -------------------------------------------------------
# Create .env
# -------------------------------------------------------

if [ ! -f ".env" ]; then

    echo ""
    echo "📝 Creating .env file..."

    if [ ! -f ".env.example" ]; then
    echo "❌ .env.example not found."
    exit 1
    fi

    cp .env.example .env

    while [ -z "$GEMINI_API_KEY" ]; do
        read -s -p "Enter your Gemini API Key: " GEMINI_API_KEY
        echo ""

        if [ -z "$GEMINI_API_KEY" ]; then
            echo "❌ Gemini API Key cannot be empty."
        fi
    done

    sed -i "s|your_gemini_api_key_here|$GEMINI_API_KEY|g" .env

    echo ""
    echo "✅ .env created successfully."

else

    echo ""
    echo "ℹ️ .env already exists. Skipping."

fi

# -------------------------------------------------------
# Build & Start Containers
# -------------------------------------------------------

echo ""
echo "🐳 Building Docker images..."

docker compose build

echo ""
echo "🚀 Starting containers..."

docker compose up -d

# -------------------------------------------------------
# Wait for Qdrant
# -------------------------------------------------------

echo ""
echo "⏳ Waiting for Qdrant..."

ATTEMPTS=0
MAX_ATTEMPTS=30

until curl -fs http://localhost:6333/collections >/dev/null 2>&1
do
    ATTEMPTS=$((ATTEMPTS + 1))

    if [ "$ATTEMPTS" -ge "$MAX_ATTEMPTS" ]; then
        echo ""
        echo "❌ Qdrant failed to start."
        echo ""
        docker compose logs qdrant
        exit 1
    fi

    sleep 2
done

echo "✅ Qdrant is ready."

# -------------------------------------------------------
# Show Running Containers
# -------------------------------------------------------

echo ""
echo "📦 Running Containers"
echo "----------------------------------------------------"

docker compose ps

echo "----------------------------------------------------"

# -------------------------------------------------------
# Show URLs
# -------------------------------------------------------

echo ""
echo "===================================================="
echo "🎉 OKF PoC Started Successfully"
echo "===================================================="

echo ""
echo "🌐 Streamlit UI"
echo "http://localhost:8501"

echo ""
echo "📘 FastAPI Docs"
echo "http://localhost:8000/docs"

echo ""
echo "🧠 Qdrant Dashboard"
echo "http://localhost:6333/dashboard"

echo ""
echo "🔍 Qdrant API"
echo "http://localhost:6333"

echo ""
echo "===================================================="
echo "✅ Setup Complete"
echo "===================================================="