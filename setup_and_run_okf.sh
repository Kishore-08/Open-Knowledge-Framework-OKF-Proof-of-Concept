#!/bin/bash

# Exit immediately on errors, undefined variables, and pipe failures
set -euo pipefail

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}====================================================${NC}"
echo -e "${GREEN}🚀 Starting OKF PoC Docker Setup${NC}"
echo -e "${BLUE}====================================================${NC}"

PROJECT_DIR="okf-poc"

# -------------------------------------------------------
# Check Required Tools
# -------------------------------------------------------
echo -e "\n${BLUE}🔍 Checking prerequisites...${NC}"

if ! command -v docker >/dev/null 2>&1; then
    echo -e "${RED}❌ Docker is not installed.${NC}"
    echo "Please install Docker Desktop or Docker Engine."
    exit 1
fi
echo -e "${GREEN}✅ Docker found${NC}"

if ! docker compose version >/dev/null 2>&1; then
    echo -e "${RED}❌ Docker Compose is not installed.${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Docker Compose found${NC}"

if ! command -v curl >/dev/null 2>&1; then
    echo -e "${RED}❌ curl is required but not installed.${NC}"
    exit 1
fi
echo -e "${GREEN}✅ curl found${NC}"

# -------------------------------------------------------
# Move into Project
# -------------------------------------------------------
if [ ! -d "$PROJECT_DIR" ]; then
    echo -e "\n${RED}❌ Project directory '${PROJECT_DIR}' not found.${NC}"
    echo "Run the project scaffold script first."
    exit 1
fi

cd "$PROJECT_DIR"
echo -e "${GREEN}✅ Project directory found${NC}"

# -------------------------------------------------------
# Create / Sync / Validate .env
# -------------------------------------------------------
echo -e "\n${BLUE}🔍 Syncing and Validating .env file...${NC}"

if [ ! -f ".env.example" ]; then
    echo -e "${RED}❌ .env.example not found. Cannot validate configurations.${NC}"
    exit 1
fi

if [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✅ .env created from .env.example${NC}"
else
    # Check for missing keys in .env that exist in .env.example
    grep -v '^#' .env.example | grep -v '^[[:space:]]*$' | while IFS='=' read -r key value; do
        if [ -n "$key" ]; then
            # If key does not exist in .env, append it
            if ! grep -q "^${key}=" .env; then
                echo "${key}=${value}" >> .env
                echo -e "${YELLOW}➕ Added missing config to .env: ${key}${NC}"
            fi
        fi
    done
    echo -e "${GREEN}✅ .env structure is up to date.${NC}"
fi

# -------------------------------------------------------
# Helper functions
# -------------------------------------------------------

update_env_file() {
    local key=$1
    local val=$2
    local temp_file
    temp_file=$(mktemp)
    
    # awk safely updates values even if they contain special chars like / or &
    awk -v k="$key" -v v="$val" '
    BEGIN { FS=OFS="=" }
    $1 == k { $2=v; found=1 }
    { print }
    END { if (!found) print k "=" v }
    ' .env > "$temp_file" && mv "$temp_file" .env
}

prompt_for_value() {
    local VAR_NAME="$1"
    local SECRET="$2"
    local NEW_VALUE=""

    while [ -z "$NEW_VALUE" ]; do
        if [ "$SECRET" = "true" ]; then
            read -s -p "Enter new value for ${VAR_NAME}: " NEW_VALUE
            echo ""
        else
            read -p "Enter new value for ${VAR_NAME}: " NEW_VALUE
        fi

        if [ -z "$NEW_VALUE" ]; then
            echo -e "${RED}❌ ${VAR_NAME} cannot be empty.${NC}"
        fi
    done

    update_env_file "$VAR_NAME" "$NEW_VALUE"
    echo -e "${GREEN}✅ ${VAR_NAME} updated successfully in .env${NC}"
}

check_and_update() {
    local VAR_NAME="$1"
    local PLACEHOLDER="$2"
    local SECRET="$3"

    # Grab current value (|| true prevents set -e from killing the script if grep fails)
    local CURRENT_VALUE
    CURRENT_VALUE=$(grep "^${VAR_NAME}=" .env | cut -d '=' -f2- || true)

    if [ -z "$CURRENT_VALUE" ] || [ "$CURRENT_VALUE" = "$PLACEHOLDER" ]; then
        echo -e "\n${YELLOW}⚠️  ${VAR_NAME} is missing or using the default placeholder.${NC}"
        prompt_for_value "$VAR_NAME" "$SECRET"
    else
        # Mask the existing value for display
        local MASKED_VAL
        if [ "${#CURRENT_VALUE}" -gt 8 ]; then
            MASKED_VAL="${CURRENT_VALUE:0:4}****${CURRENT_VALUE: -4}"
        else
            MASKED_VAL="********"
        fi

        echo -e "\n${BLUE}✔ ${VAR_NAME} is currently set (${MASKED_VAL}).${NC}"
        read -p "Do you want to update it? (y/N): " UPDATE_CHOICE
        if [[ "$UPDATE_CHOICE" =~ ^[Yy]$ ]]; then
            prompt_for_value "$VAR_NAME" "$SECRET"
        else
            echo -e "${GREEN}✅ Kept existing ${VAR_NAME}.${NC}"
        fi
    fi
}

# -------------------------------------------------------
# Required Variables to Check Interactively
# -------------------------------------------------------
check_and_update "GEMINI_API_KEY" "your_gemini_api_key_here" true

echo -e "\n${GREEN}🎉 .env validation completed.${NC}"

# -------------------------------------------------------
# Build & Start Containers
# -------------------------------------------------------
echo -e "\n${BLUE}🐳 Building Docker images...${NC}"
docker compose build

echo -e "\n${BLUE}🚀 Starting containers...${NC}"
docker compose up -d

# -------------------------------------------------------
# Wait for Qdrant
# -------------------------------------------------------
echo -e "\n${YELLOW}⏳ Waiting for Qdrant to be ready...${NC}"

ATTEMPTS=0
MAX_ATTEMPTS=30

until curl -fs http://localhost:6333/collections >/dev/null 2>&1
do
    ATTEMPTS=$((ATTEMPTS + 1))
    
    if [ "$ATTEMPTS" -ge "$MAX_ATTEMPTS" ]; then
        echo -e "\n${RED}❌ Qdrant failed to start.${NC}\n"
        docker compose logs qdrant
        exit 1
    fi
    sleep 2
done

echo -e "${GREEN}✅ Qdrant is ready.${NC}"

# -------------------------------------------------------
# Show Running Containers
# -------------------------------------------------------
echo -e "\n${BLUE}📦 Running Containers${NC}"
echo "----------------------------------------------------"
docker compose ps
echo "----------------------------------------------------"

# -------------------------------------------------------
# Show URLs
# -------------------------------------------------------
echo -e "\n${GREEN}====================================================${NC}"
echo -e "${GREEN}🎉 OKF PoC Started Successfully${NC}"
echo -e "${GREEN}====================================================${NC}"

echo -e "\n🌐 ${YELLOW}Streamlit UI${NC}"
echo "http://localhost:8501"

echo -e "\n📘 ${YELLOW}FastAPI Docs${NC}"
echo "http://localhost:8000/docs"

echo -e "\n🧠 ${YELLOW}Qdrant Dashboard${NC}"
echo "http://localhost:6333/dashboard"

echo -e "\n🔍 ${YELLOW}Qdrant API${NC}"
echo "http://localhost:6333"

echo -e "\n${BLUE}====================================================${NC}"
echo -e "${BLUE}✅ Setup Complete${NC}"
echo -e "${BLUE}====================================================${NC}"