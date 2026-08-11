---
id: architecture-aws-services-guide-for-okf-poc-architecture
type: concept
title: AWS Services Guide for OKF PoC Architecture
description: This document outlines the recommended AWS architecture for the OKF Proof
  of Concept, detailing a serverless deployment using ECS/Fargate, S3, Qdrant, and
  the Gemini API. It highlights service roles such as storage, vector search, and
  generation, while comparing Fargate's simplicity to Kubernetes.
category: architecture
tags:
- AWS Architecture
- ECS/Fargate
- Vector Search
- Gemini API
- Cloud Deployment
source:
  name: Ingested document
  url: ''
created_at: '2026-08-08'
updated_at: '2026-08-08'
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
