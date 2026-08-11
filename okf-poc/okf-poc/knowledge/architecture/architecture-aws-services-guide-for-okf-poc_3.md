---
id: architecture-aws-services-guide-for-okf-poc
type: concept
title: AWS Services Guide for OKF PoC
description: This document outlines the recommended AWS cloud architecture for an
  OKF Proof of Concept (PoC) deployment. It details a multi-layered stack utilizing
  ECS/Fargate for application hosting, S3 for storage, Qdrant for vector search, and
  the Gemini API for LLM generation.
category: architecture
tags:
- AWS
- ECS Fargate
- Vector Search
- LLM Integration
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
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
