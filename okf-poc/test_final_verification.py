#!/usr/bin/env python3
"""Final verification test - demonstrates the fix works"""

import requests
import json

API_URL = "http://localhost:8000/api/v1/ask/"

queries = [
    "What is Kubernetes?",
    "What is Docker?",
    "What is a Kubernetes Pod?",
]

print("="*80)
print("FINAL VERIFICATION TEST")
print("="*80)
print("\nThis test verifies that the 'What is Kubernetes?' issue is FIXED.\n")

all_passed = True

for query in queries:
    print(f"\n{'─'*80}")
    print(f"Query: {query}")
    print('─'*80)
    
    try:
        response = requests.post(API_URL, json={"question": query}, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        answer = result.get("answer", "")
        sources = result.get("sources", [])
        
        # Check if answer is a refusal
        is_refusal = ("cannot answer" in answer.lower() or 
                     "unable to answer" in answer.lower())
        
        if is_refusal:
            print(f"❌ FAILED: AI refused to answer")
            print(f"   Answer: {answer[:150]}...")
            all_passed = False
        else:
            print(f"✅ PASSED: AI provided an answer")
            print(f"   Answer: {answer[:150]}...")
        
        print(f"\n   Top 3 sources:")
        for idx, src in enumerate(sources[:3], 1):
            print(f"   {idx}. {src.get('title')} (category={src.get('category')}, score={src.get('score')})")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        all_passed = False

print(f"\n{'='*80}")
if all_passed:
    print("🎉 SUCCESS: All queries returned answers!")
    print("The 'What is Kubernetes?' issue is FIXED.")
else:
    print("⚠️  Some queries failed. See details above.")
print("="*80)
