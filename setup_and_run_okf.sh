#!/usr/bin/env bash

set -Eeuo pipefail

readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m'

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

if [[ -f "${SCRIPT_DIR}/okf-poc/docker-compose.yml" ]]; then
    PROJECT_DIR="${SCRIPT_DIR}/okf-poc"
elif [[ -f "${SCRIPT_DIR}/docker-compose.yml" ]]; then
    PROJECT_DIR="${SCRIPT_DIR}"
else
    printf '%bError: could not find okf-poc/docker-compose.yml.%b\n' "$RED" "$NC" >&2
    exit 1
fi

cd "$PROJECT_DIR"

info() { printf '%b%s%b\n' "$BLUE" "$1" "$NC"; }
success() { printf '%b%s%b\n' "$GREEN" "$1" "$NC"; }
warn() { printf '%b%s%b\n' "$YELLOW" "$1" "$NC"; }
fail() { printf '%b%s%b\n' "$RED" "$1" "$NC" >&2; exit 1; }

get_env_value() {
    local key="$1"
    awk -F= -v key="$key" '$1 == key { sub(/^[^=]*=/, ""); print; exit }' .env
}

set_env_value() {
    local key="$1"
    local value="$2"
    local temp_file
    temp_file="$(mktemp)"

    awk -v key="$key" -v value="$value" '
        BEGIN { updated = 0 }
        index($0, key "=") == 1 {
            if (!updated) print key "=" value
            updated = 1
            next
        }
        { print }
        END { if (!updated) print key "=" value }
    ' .env > "$temp_file"
    mv "$temp_file" .env
}

is_placeholder() {
    local value="$1"
    [[ -z "$value" || "$value" == your_* || "$value" == \$\{*\} ]]
}

prompt_value() {
    local key="$1"
    local secret="${2:-false}"
    local value=""

    while [[ -z "$value" ]]; do
        if [[ "$secret" == true ]]; then
            read -r -s -p "Enter ${key}: " value
            printf '\n'
        else
            read -r -p "Enter ${key}: " value
        fi
        [[ -n "$value" ]] || warn "${key} cannot be empty."
    done

    set_env_value "$key" "$value"
    success "Updated ${key} in .env."
}

require_config() {
    local key="$1"
    local secret="${2:-false}"
    local value
    value="$(get_env_value "$key")"

    if is_placeholder "$value"; then
        warn "${key} is not configured."
        prompt_value "$key" "$secret"
    else
        success "${key} is configured."
    fi
}

wait_for_url() {
    local name="$1"
    local url="$2"
    local service="$3"
    local max_attempts="${4:-30}"
    local attempt

    info "Waiting for ${name}..."
    for ((attempt = 1; attempt <= max_attempts; attempt++)); do
        if curl --fail --silent --show-error --max-time 3 "$url" >/dev/null 2>&1; then
            success "${name} is ready."
            return 0
        fi
        sleep 2
    done

    printf '%b%s failed to become ready. Recent logs:%b\n' "$RED" "$name" "$NC" >&2
    docker compose logs --tail=100 "$service" >&2 || true
    return 1
}

printf '%b====================================================%b\n' "$BLUE" "$NC"
success "Starting OKF PoC Docker setup"
printf '%b====================================================%b\n' "$BLUE" "$NC"

info "Checking prerequisites..."
command -v docker >/dev/null 2>&1 || fail "Docker is not installed."
docker compose version >/dev/null 2>&1 || fail "Docker Compose v2 is not available."
command -v curl >/dev/null 2>&1 || fail "curl is not installed."
docker info >/dev/null 2>&1 || fail "The Docker daemon is not running or is not accessible."
success "Docker, Docker Compose, and curl are available."

info "Preparing environment configuration..."
[[ -f .env.example ]] || fail ".env.example was not found in ${PROJECT_DIR}."

if [[ ! -f .env ]]; then
    cp .env.example .env
    success "Created .env from .env.example."
else
    while IFS= read -r line || [[ -n "$line" ]]; do
        [[ "$line" =~ ^[[:space:]]*([A-Za-z_][A-Za-z0-9_]*)= ]] || continue
        key="${BASH_REMATCH[1]}"
        if ! grep -qE "^${key}=" .env; then
            printf '%s\n' "$line" >> .env
            warn "Added missing setting ${key} from .env.example."
        fi
    done < .env.example
fi

provider="$(get_env_value AI_PROVIDER)"
provider="${provider,,}"
if [[ "$provider" != gemini && "$provider" != vertex ]]; then
    warn "AI_PROVIDER must be either 'gemini' or 'vertex'."
    while [[ "$provider" != gemini && "$provider" != vertex ]]; do
        read -r -p "Choose AI provider (gemini/vertex): " provider
        provider="${provider,,}"
    done
    set_env_value AI_PROVIDER "$provider"
fi

if [[ "$provider" == gemini ]]; then
    info "Validating Gemini Developer API configuration..."
    require_config GEMINI_API_KEY true
else
    info "Validating Vertex AI configuration..."
    require_config VERTEX_AI_PROJECT_ID false
    require_config VERTEX_AI_LOCATION false
    require_config VERTEX_ACCESS_TOKEN true
    warn "VERTEX_ACCESS_TOKEN is short-lived and may need to be refreshed before a later run."
fi

success "Environment configuration is ready (${provider})."

info "Validating Docker Compose configuration..."
docker compose config --quiet
success "Docker Compose configuration is valid."

info "Building and starting api, ui, and qdrant..."
docker compose up --build --detach --remove-orphans

wait_for_url "Qdrant" "http://localhost:6333/collections" qdrant 30
wait_for_url "FastAPI" "http://localhost:8000/health" api 45
wait_for_url "Streamlit" "http://localhost:8501/_stcore/health" ui 45

printf '\n'
docker compose ps

printf '\n%b====================================================%b\n' "$GREEN" "$NC"
success "OKF PoC started successfully"
printf '%b====================================================%b\n' "$GREEN" "$NC"
printf 'Streamlit UI:     http://localhost:8501\n'
printf 'FastAPI docs:     http://localhost:8000/docs\n'
printf 'API health:       http://localhost:8000/health\n'
printf 'Qdrant dashboard: http://localhost:6333/dashboard\n'
printf '\nView logs with: cd %q && docker compose logs -f api ui qdrant\n' "$PROJECT_DIR"
