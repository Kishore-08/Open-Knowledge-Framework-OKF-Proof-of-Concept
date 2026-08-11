---
id: architecture-aws-services-guide-okf-poc-architecture
type: concept
title: AWS Services Guide — OKF PoC Architecture
description: This document outlines the recommended AWS cloud architecture for the
  OKF Proof of Concept, utilizing ECS/Fargate to host Streamlit and FastAPI. It defines
  a clear separation of concerns with Amazon S3 for durable storage, Qdrant for vector
  retrieval, and the Gemini API for LLM generation.
category: architecture
tags:
- AWS ECS Fargate
- Vector Search Qdrant
- Generative AI Gemini API
- Cloud Architecture
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: aws_services_project_guide.pdf
---

AWS Services Guide — OKF PoC
Page 2
1. Recommended AWS Architecture
User
↓
Route 53 / HTTPS
↓
Application Load Balancer
↓
ECS/Fargate: Streamlit + FastAPI
↓
S3: raw uploads + OKF knowledge artifacts
↓
Qdrant: vector search
↓
Gemini API: LLM / embeddings
Supporting services: ECR, IAM, Secrets Manager, VPC, CloudWatch, CloudTrail
For a first cloud deployment, ECS/Fargate is simpler than operating Kubernetes yourself. If Kubernetes is specifically a
learning or deployment requirement, EKS is the advanced alternative.
Keep the architectural boundaries clear: S3/knowledge is the durable document layer, Qdrant is the retrieval index, and
Gemini is the generation layer.
