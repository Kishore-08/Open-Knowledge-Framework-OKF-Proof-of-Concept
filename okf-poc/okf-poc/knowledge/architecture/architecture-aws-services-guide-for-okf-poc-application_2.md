---
id: architecture-aws-services-guide-for-okf-poc-application
type: concept
title: AWS Services Guide for OKF PoC Application
description: This document provides a practical reference for hosting a Dockerized
  FastAPI, Streamlit, Qdrant, and Gemini-based RAG application on AWS. It outlines
  the role of major AWS services like ECS/Fargate, S3, and ECR, explaining how they
  integrate with the application without replacing core AI components
category: architecture
tags:
- AWS
- Docker
- RAG
- FastAPI
- ECS Fargate
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Architecture
trust_level: High
source_file: aws_services_project_guide.pdf
---

AWS Services Guide — OKF PoC
Page 1
 AWS Services Guide
Practical AWS reference for a Dockerized FastAPI + Streamlit + Qdrant + Gemini OKF/RAG application
Scope: What each major AWS service does, why it is useful, and how it can fit this project.
Your current application uses FastAPI, Streamlit, Docker, Qdrant, Gemini, an OKF Markdown knowledge repository,
document ingestion, metadata extraction, and retrieval. AWS can provide the cloud infrastructure around these
components without requiring you to replace Gemini or Qdrant.
Core recommendation: use ECS/Fargate for containers, S3 for durable documents and OKF artifacts, ECR for images,
IAM and Secrets Manager for security, ALB/VPC for networking, and CloudWatch for operations.
