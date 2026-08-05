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
# Create / Validate .env
# -------------------------------------------------------

echo ""
echo "🔍 Checking .env..."

if [ ! -f ".env" ]; then

    if [ ! -f ".env.example" ]; then
        echo "❌ .env.example not found."
        exit 1
    fi

    cp .env.example .env
    echo "✅ .env created from .env.example"

fi

# -------------------------------------------------------
# Helper function
# -------------------------------------------------------

check_and_update() {

    VAR_NAME="$1"
    PLACEHOLDER="$2"
    SECRET="$3"

    CURRENT_VALUE=$(grep "^${VAR_NAME}=" .env | cut -d '=' -f2-)

    if [ -z "$CURRENT_VALUE" ] || [ "$CURRENT_VALUE" = "$PLACEHOLDER" ]; then

        echo ""

        if [ "$SECRET" = "true" ]; then
            read -s -p "Enter ${VAR_NAME}: " NEW_VALUE
            echo ""
        else
            read -p "Enter ${VAR_NAME}: " NEW_VALUE
        fi

        while [ -z "$NEW_VALUE" ]; do
            echo "❌ ${VAR_NAME} cannot be empty."

            if [ "$SECRET" = "true" ]; then
                read -s -p "Enter ${VAR_NAME}: " NEW_VALUE
                echo ""
            else
                read -p "Enter ${VAR_NAME}: " NEW_VALUE
            fi
        done

        if grep -q "^${VAR_NAME}=" .env; then
            sed -i "s|^${VAR_NAME}=.*|${VAR_NAME}=${NEW_VALUE}|" .env
        else
            echo "${VAR_NAME}=${NEW_VALUE}" >> .env
        fi

        echo "✅ ${VAR_NAME} updated."

    else
        echo "✔ ${VAR_NAME} already configured."
    fi
}

# -------------------------------------------------------
# Required Variables
# -------------------------------------------------------

check_and_update "GEMINI_API_KEY" "your_gemini_api_key_here" true

echo ""
echo "🎉 .env validation completed."

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