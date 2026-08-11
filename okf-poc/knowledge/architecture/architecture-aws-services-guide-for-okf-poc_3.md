---
id: architecture-aws-services-guide-for-okf-poc
type: concept
title: AWS Services Guide for OKF PoC
<<<<<<< HEAD
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
=======
description: This document provides a practical AWS reference guide for deploying
  a Dockerized FastAPI, Streamlit, Qdrant, and Gemini-based OKF/RAG application. It
  details how various AWS infrastructure services like ECS, S3, ECR, IAM, and ALB
  can support the application without replacing its core AI and databas
category: architecture
tags:
- AWS
- Docker
- ECS Fargate
- RAG
- Cloud Infrastructure
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: Architecture
trust_level: High
>>>>>>> 279b5f57 (updated the Evaluation)
source_file: aws_services_project_guide.pdf
---

AWS Services Guide — OKF PoC
<<<<<<< HEAD
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
=======
Page 1
 AWS Services Guide
Practical AWS reference for a Dockerized FastAPI + Streamlit + Qdrant + Gemini OKF/RAG application
Scope: What each major AWS service does, why it is useful, and how it can fit this project.
Your current application uses FastAPI, Streamlit, Docker, Qdrant, Gemini, an OKF Markdown knowledge repository,
document ingestion, metadata extraction, and retrieval. AWS can provide the cloud infrastructure around these
components without requiring you to replace Gemini or Qdrant.
Core recommendation: use ECS/Fargate for containers, S3 for durable documents and OKF artifacts, ECR for images,
IAM and Secrets Manager for security, ALB/VPC for networking, and CloudWatch for operations.
>>>>>>> 279b5f57 (updated the Evaluation)
