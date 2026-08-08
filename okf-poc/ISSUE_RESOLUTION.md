# Issue Resolution: "What is Kubernetes?" Query Fix

## Original Problem

**User Report:**
> "if i ask what is kubernetes, the ai assistant is telling 'I cannot answer this based on the OKF knowledge base', but it should ans as we have data in knowledge folder"

**Symptoms:**
- AI assistant returned "I cannot answer this based on the OKF knowledge base"
- Knowledge repository contained 645 Kubernetes concepts
- Query API returned 5 source documents
- Top sources were Docker and CI/CD documents (wrong category)
- Answer generator refused to respond despite having sources

## Investigation Process

### Step 1: Verified Knowledge Repository
```bash
# Confirmed 645 Kubernetes concepts exist
$ python3 test_query.py
✅ Found 6 categories: apache, kubernetes, langchain, linux, reference, tutorial
✅ Found 645 Kubernetes concepts
```

### Step 2: Traced Query Execution Path
Added debug logging to trace:
1. Query reception: `/api/v1/ask/` → `app/query/engine.py`
2. Retrieval: `app/query/search.py` → `app/okf/repository.py`
3. Context building: Retrieved docs → LLM prompt
4. Answer generation: `app/core/gemini_llm.py`

### Step 3: Identified Root Causes

**Root Cause #1: Incomplete Qdrant Vector Index**
- Only 79/874 documents indexed before hitting Gemini API rate limits (429 errors)
- Semantic search returned Docker/CI-CD docs instead of Kubernetes docs
- Evidence from logs:
  ```
  Retrieved (before fix):
    1. 'Docker Basics for DevOps' (category=reference, score=0.7521)
    2. 'Docker Basics for DevOps' (category=reference, score=0.7521)
    3. 'CI/CD Pipeline Guide' (category=reference, score=0.721)
    5. 'What's next' (category=kubernetes, score=27.0)  # Only 1 K8s doc!
  ```

**Root Cause #2: Wrong Search Result Merging Strategy**
- In "auto" mode, search.py was preferring semantic results over keyword results
- Since semantic index was incomplete, wrong documents ranked first
- Code in `app/query/search.py`:
  ```python
  # WRONG: Prefer incomplete semantic results
  merged = list(semantic_results)
  for r in keyword_results:
      if r["id"] not in seen:
          merged.append(r)  # Keyword as fallback only
  ```

**Root Cause #3: Poor Keyword Search Ranking**
- "What is Kubernetes?" query didn't prioritize overview/definition documents
- File `kubernetes-overview-eceb9608.md` (contains "Kubernetes is a portable...") wasn't ranking high
- Retrieved documents ("What's next", "Workload Management") didn't contain the definition
- LLM correctly refused to answer based on incomplete context

## Solutions Implemented

### Fix 1: Prioritize Keyword Search Over Incomplete Semantic Search
**File:** `app/query/search.py` (Lines 45-59)

**Change:**
```python
# NEW: Start with accurate keyword results
merged = list(keyword_results[:top_k])
seen = {r["id"] for r in merged}

# Add only high-confidence semantic results
for r in semantic_results:
    if r["id"] not in seen and r.get("score", 0) > 0.8:
        merged.append(r)
        if len(merged) >= top_k:
            break
```

**Rationale:** Keyword search is always accurate (filesystem-based), while semantic search is degraded due to incomplete index.

### Fix 2: Boost Overview Documents for "What is X?" Queries
**File:** `app/okf/repository.py` (Lines 225-285)

**Change:**
```python
# Detect "What is X?" pattern
is_definition_query = query.lower().startswith(("what is", "what are", "define"))
overview_keywords = ["overview", "introduction", "intro", "basics", "getting started"]

# Apply 5x boost for overview titles
if is_definition_query and matched_fields:
    title_lower = meta.title.lower()
    if any(kw in title_lower for kw in overview_keywords):
        score *= 5.0
    
    # 3x boost for "X is a/an" definitions
    desc_lower = (meta.description or "").lower()
    if any(desc_lower.startswith(t + " is a") for t in tokens):
        score *= 3.0
```

**Rationale:** "What is X?" queries should prioritize documents that define X, not documents that mention X in passing.

## Results

### Before Fix
```json
{
  "query": "What is Kubernetes?",
  "top_results": [
    {"title": "Docker Basics for DevOps", "category": "reference", "score": 0.7521},
    {"title": "CI/CD Pipeline Guide", "category": "reference", "score": 0.721},
    {"title": "What's next", "category": "kubernetes", "score": 27.0}
  ],
  "answer": "I cannot answer this based on the OKF knowledge base."
}
```

### After Fix
```json
{
  "query": "What is Kubernetes?",
  "top_results": [
    {"title": "Overview", "category": "kubernetes", "score": 135.0},
    {"title": "What is Ingress?", "category": "kubernetes", "score": 45.0},
    {"title": "What is a Pod?", "category": "kubernetes", "score": 40.0}
  ],
  "answer": "Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services [Overview]."
}
```

### Test Results
```bash
$ python3 test_query.py
✅ Found 645 Kubernetes concepts
✅ Got answer!
   Answer: Kubernetes is a portable, extensible, open source platform...
📚 Sources:
   - Overview (https://kubernetes.io/docs/concepts/overview/)
   - What is Ingress? (https://kubernetes.io/docs/concepts/services-networking/ingress/)
   - What is a Pod? (https://kubernetes.io/docs/concepts/workloads/pods/)
```

## Verification

All files modified and working correctly in Docker environment:

1. **app/query/search.py** - Search result merging strategy fixed ✅
2. **app/okf/repository.py** - Overview document boosting added ✅
3. **app/query/engine.py** - Debug logging removed (production-ready) ✅

Verified via:
```bash
# Test via API
$ curl -X POST http://localhost:8000/api/v1/ask/ \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Kubernetes?"}'

# Returns correct answer with kubernetes.io sources ✅
```

## Known Limitations

1. **Qdrant Index Incomplete** - Only 79/874 docs indexed
   - Semantic search degraded but compensated by keyword search
   - Recommendation: Complete indexing with rate limit handling

2. **Some Queries Still Fail** - e.g., "What are Kubernetes namespaces?"
   - No dedicated namespace overview document exists in knowledge base
   - LLM correctly says it cannot answer (working as designed)
   - Recommendation: Generate missing overview pages

3. **Category Inconsistencies** - Some docs have wrong category assignments
   - e.g., CI/CD docs in "tutorial" instead of "reference"
   - Doesn't affect retrieval but affects filtering
   - Recommendation: Normalize during ingestion

## Recommendations

### Immediate (Done ✅)
- ✅ Fix search ranking for "What is X?" queries
- ✅ Prioritize keyword over incomplete semantic search
- ✅ Remove debug logging

### Short-term (Not Done)
- ⏸️ Complete Qdrant indexing with rate limit handling
- ⏸️ Generate missing overview documents for common queries
- ⏸️ Add batch API endpoint for testing multiple queries

### Long-term (Not Done)
- ⏸️ Implement query rewriting and expansion
- ⏸️ Add relevance feedback mechanism
- ⏸️ Build comprehensive test suite with expected answers

## Conclusion

**Status: ✅ RESOLVED**

The issue "What is Kubernetes?" returning "I cannot answer" has been **completely fixed**. The system now:

1. ✅ Retrieves correct Kubernetes documents for Kubernetes questions
2. ✅ Prioritizes overview/definition documents for "What is X?" queries  
3. ✅ Generates accurate answers from retrieved context
4. ✅ Cites correct source documents with URLs
5. ✅ Works reliably in Docker deployment

The root cause was an incomplete vector index combined with poor search ranking. By prioritizing keyword search and boosting overview documents, the system now functions correctly for definition queries.

**Test it yourself:**
```bash
cd okf-poc
docker compose up -d
python3 test_query.py
```

Expected output:
```
✅ Got answer!
Answer: Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services (Overview)....
```
