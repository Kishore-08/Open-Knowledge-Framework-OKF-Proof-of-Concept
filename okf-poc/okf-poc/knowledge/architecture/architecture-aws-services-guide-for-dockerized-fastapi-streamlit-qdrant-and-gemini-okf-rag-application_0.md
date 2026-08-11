---
id: architecture-aws-services-guide-for-dockerized-fastapi-streamlit-qdrant-and-gemini-okf-rag-application
type: concept
title: AWS Services Guide for Dockerized FastAPI, Streamlit, Qdrant, and Gemini OKF/RAG
  Application
description: This document provides a practical AWS reference guide for deploying
  a containerized RAG application built with FastAPI, Streamlit, Qdrant, and Gemini.
  It outlines the scope of major AWS services, their use cases, and core architectural
  recommendations including ECS/Fargate, S3, ECR, and IAM.
category: architecture
tags:
- AWS
- Containerization
- RAG
- Cloud Architecture
- FastAPI
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
Page 1
 AWS Services Guide
Practical AWS reference for a Dockerized FastAPI + Streamlit + Qdrant + Gemini OKF/RAG application
Scope: What each major AWS service does, why it is useful, and how it can fit this project.
Your current application uses FastAPI, Streamlit, Docker, Qdrant, Gemini, an OKF Markdown knowledge repository,
document ingestion, metadata extraction, and retrieval. AWS can provide the cloud infrastructure around these
components without requiring you to replace Gemini or Qdrant.
Core recommendation: use ECS/Fargate for containers, S3 for durable documents and OKF artifacts, ECR for images,
IAM and Secrets Manager for security, ALB/VPC for networking, and CloudWatch for operations.
