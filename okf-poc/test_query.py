#!/usr/bin/env python3
"""Quick test to check if knowledge base is working"""

import requests

API_HOST = "http://localhost:8000"

# Test 1: Check how many concepts are available
print("=" * 60)
print("Test 1: Checking available concepts")
print("=" * 60)

try:
    response = requests.get(f"{API_HOST}/api/v1/knowledge/categories")
    if response.status_code == 200:
        categories = response.json()
        print(f"✅ Found {len(categories)} categories:")
        for cat in categories:
            print(f"   - {cat}")
    else:
        print(f"❌ Failed to get categories: {response.status_code}")
        print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")

print()

# Test 2: List Kubernetes concepts
print("=" * 60)
print("Test 2: Listing Kubernetes concepts")
print("=" * 60)

try:
    response = requests.get(f"{API_HOST}/api/v1/knowledge/concepts?category=kubernetes")
    if response.status_code == 200:
        concepts = response.json()
        print(f"✅ Found {len(concepts)} Kubernetes concepts")
        if concepts:
            print("\nFirst 5 concepts:")
            for concept in concepts[:5]:
                print(f"   - {concept['title']} (id: {concept['id']})")
    else:
        print(f"❌ Failed to list concepts: {response.status_code}")
        print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")

print()

# Test 3: Ask "What is Kubernetes?"
print("=" * 60)
print("Test 3: Asking 'What is Kubernetes?'")
print("=" * 60)

try:
    response = requests.post(
        f"{API_HOST}/api/v1/ask/",
        json={"question": "What is Kubernetes?"},
        timeout=30
    )
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Got answer!")
        print(f"\nAnswer: {result['answer'][:500]}...")
        print(f"\n📚 Sources: {len(result['sources'])} documents")
        if result['sources']:
            print("\nTop sources:")
            for src in result['sources'][:3]:
                print(f"   - {src['title']}")
                print(f"     URL: {src['source_url']}")
    else:
        print(f"❌ Failed to get answer: {response.status_code}")
        print(f"Response: {response.text}")
except Exception as e:
    print(f"❌ Error: {e}")

print()
print("=" * 60)
