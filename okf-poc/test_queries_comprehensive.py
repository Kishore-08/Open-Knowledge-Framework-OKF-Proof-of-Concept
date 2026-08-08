#!/usr/bin/env python3
"""Comprehensive test suite for query answering"""

import requests

API_URL = "http://localhost:8000/api/v1"

test_cases = [
    {
        "query": "What is Kubernetes?",
        "expected_keywords": ["kubernetes", "platform", "container"],
        "expected_category": "kubernetes",
    },
    {
        "query": "What is a Kubernetes Deployment?",
        "expected_keywords": ["deployment", "replica", "pod"],
        "expected_category": "kubernetes",
    },
    {
        "query": "What are Kubernetes namespaces?",
        "expected_keywords": ["namespace", "isolation", "cluster"],
        "expected_category": "kubernetes",
    },
    {
        "query": "What is Docker?",
        "expected_keywords": ["docker", "container"],
        "expected_category": "reference",
    },
    {
        "query": "What is CI/CD?",
        "expected_keywords": ["continuous", "integration", "deployment"],
        "expected_category": "reference",
    },
]

def test_query(query_text, expected_keywords, expected_category):
    """Test a single query"""
    print(f"\n{'='*70}")
    print(f"Query: {query_text}")
    print('='*70)
    
    try:
        response = requests.post(f"{API_URL}/ask/", json={"question": query_text}, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        answer = result.get("answer", "")
        sources = result.get("sources", [])
        
        # Check if answer contains expected keywords
        answer_lower = answer.lower()
        matched_keywords = [kw for kw in expected_keywords if kw.lower() in answer_lower]
        
        # Check if sources are from correct category
        source_categories = [s.get("category") for s in sources[:3]]
        has_correct_category = expected_category in source_categories
        
        # Check if answer says "cannot answer"
        is_refusal = "cannot answer" in answer_lower or "unable to answer" in answer_lower
        
        print(f"✅ Got answer ({len(answer)} chars)")
        print(f"   Answer preview: {answer[:200]}...")
        print(f"\n📚 Top {len(sources[:3])} sources:")
        for idx, src in enumerate(sources[:3], 1):
            print(f"   {idx}. {src.get('title')} (category={src.get('category')})")
            print(f"      URL: {src.get('source_url', 'N/A')}")
        
        print(f"\n🔍 Verification:")
        print(f"   Matched keywords: {matched_keywords}/{len(expected_keywords)}")
        print(f"   Has {expected_category} sources: {'✅' if has_correct_category else '❌'}")
        print(f"   Provides answer: {'❌ REFUSED' if is_refusal else '✅'}")
        
        if is_refusal:
            print(f"\n⚠️  ISSUE: AI refused to answer despite having sources!")
            return False
        elif not has_correct_category:
            print(f"\n⚠️  ISSUE: Sources are from wrong category!")
            return False
        elif len(matched_keywords) == 0:
            print(f"\n⚠️  WARNING: Answer doesn't contain expected keywords")
            return False
        else:
            print(f"\n✅ TEST PASSED")
            return True
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("\n" + "="*70)
    print("COMPREHENSIVE QUERY TESTING")
    print("="*70)
    
    results = []
    for test_case in test_cases:
        passed = test_query(
            test_case["query"],
            test_case["expected_keywords"],
            test_case["expected_category"]
        )
        results.append((test_case["query"], passed))
    
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    for query, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status}: {query}")
    
    print(f"\nTotal: {passed_count}/{total_count} tests passed")
    
    if passed_count == total_count:
        print("\n🎉 All tests passed!")
    else:
        print(f"\n⚠️  {total_count - passed_count} test(s) failed")

if __name__ == "__main__":
    main()
