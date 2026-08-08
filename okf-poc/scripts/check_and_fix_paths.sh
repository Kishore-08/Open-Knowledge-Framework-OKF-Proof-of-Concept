#!/bin/bash

echo "=========================================="
echo "OKF Path Check and Fix Script"
echo "=========================================="
echo ""

# Check current state
echo "📊 Current State:"
echo "----------------"
echo "Files in knowledge/ (NEW location): $(find knowledge -name '*.md' -type f 2>/dev/null | wc -l)"
echo "Files in data/knowledge/ (OLD location): $(find data/knowledge -name '*.md' -type f 2>/dev/null | wc -l)"
echo "Files in data/raw/ (OLD cache): $(find data/raw -type f 2>/dev/null | wc -l)"
echo "Files in cache/ (NEW cache): $(find cache -type f 2>/dev/null | wc -l)"
echo ""

# Check .env
echo "🔧 Configuration Check:"
echo "----------------------"
if grep -q "KNOWLEDGE_DIR=knowledge" .env; then
    echo "✅ .env has KNOWLEDGE_DIR=knowledge"
else
    echo "❌ .env needs update"
    grep "KNOWLEDGE_DIR" .env || echo "  (KNOWLEDGE_DIR not found)"
fi

if grep -q "CACHE_DIR=cache" .env; then
    echo "✅ .env has CACHE_DIR=cache"
else
    echo "❌ .env needs update"
    grep "CACHE_DIR" .env || echo "  (CACHE_DIR not found)"
fi
echo ""

# Check Docker
echo "🐳 Docker Status:"
echo "----------------"
if docker ps | grep -q okf-poc; then
    echo "⚠️  Docker containers are running"
    echo "   You need to restart them after fixes:"
    echo "   docker-compose down && docker-compose up -d"
else
    echo "✅ Docker containers not running"
fi
echo ""

# Recommendation
echo "📋 Recommendation:"
echo "-----------------"

DATA_KNOWLEDGE_COUNT=$(find data/knowledge -name '*.md' -type f 2>/dev/null | wc -l)
KNOWLEDGE_COUNT=$(find knowledge -name '*.md' -type f 2>/dev/null | wc -l)

if [ "$DATA_KNOWLEDGE_COUNT" -gt "$KNOWLEDGE_COUNT" ]; then
    echo "⚠️  You have MORE data in data/knowledge/ than knowledge/"
    echo ""
    echo "Option 1: Use migration script (RECOMMENDED)"
    echo "  python scripts/migrate_data_structure.py"
    echo ""
    echo "Option 2: Manual merge"
    echo "  rsync -av data/knowledge/ knowledge/"
    echo ""
    echo "Option 3: Use data/knowledge temporarily"
    echo "  Update .env: KNOWLEDGE_DIR=data/knowledge"
    echo "  (Not recommended - defeats refactoring purpose)"
else
    echo "✅ knowledge/ has more or equal data"
    echo "   Run: docker-compose down && docker-compose up -d"
fi
echo ""
echo "=========================================="
