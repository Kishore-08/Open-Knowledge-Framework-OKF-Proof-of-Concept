---
id: tutorial-aws-services-project-guide-example-deployment-flow
type: concept
title: 'AWS Services Project Guide: Example Deployment Flow'
description: This document outlines an example deployment flow for an AWS-based Proof
  of Concept project. It details the step-by-step process from code push and Docker
  image building to ECS/Fargate deployment, S3 storage, vector indexing with Qdrant,
  and LLM integration via Gemini.
category: tutorial
tags:
- AWS
- Deployment Flow
- ECS/Fargate
- Docker
- CI/CD
source:
  name: Ingested document
  url: ''
created_at: '2026-08-08'
updated_at: '2026-08-08'
aliases: []
related: []
document_type: Tutorial
trust_level: Medium
source_file: aws_services_project_guide.pdf
---

AWS Services Guide — OKF PoC
Page 10
9. Example Deployment Flow
1. Developer pushes code to Git.
2. CI runs tests and builds Docker images.
3. Images are pushed to ECR.
4. ECS/Fargate deploys API and UI.
5. ALB exposes HTTPS endpoints.
6. User uploads a document.
7. Backend stores the source in S3.
8. Ingestion processes the document.
9. OKF Markdown is written to durable knowledge storage.
10. Concepts are embedded and indexed into Qdrant.
11. User asks a question in Streamlit.
12. FastAPI performs retrieval.
13. Retrieved OKF context is passed to Gemini.
14. Answer and source attribution are returned.
15. CloudWatch records logs and metrics.
For the current PoC, migrate incrementally. First move containers to ECS/Fargate and images to ECR. Then move
durable documents to S3. Add Secrets Manager and CloudWatch. Add ALB/HTTPS and DNS when the application is
ready for public access.
