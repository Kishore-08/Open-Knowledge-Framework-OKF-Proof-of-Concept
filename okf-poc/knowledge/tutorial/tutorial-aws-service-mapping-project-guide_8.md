---
id: tutorial-aws-service-mapping-project-guide
type: concept
title: AWS Service Mapping Project Guide
description: This document outlines the AWS service mappings required for a Proof
  of Concept project. It pairs specific technical requirements, such as running FastAPI,
  Streamlit, and Qdrant, with their corresponding AWS solutions including ECS, S3,
  RDS, and EC2.
category: tutorial
tags:
- AWS
- Cloud Architecture
- Containerization
- Infrastructure
- DevOps
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
Page 9
8. Service Mapping for Your Project
Requirement
AWS service
Use
Run FastAPI
ECS + Fargate
Managed Docker runtime
Run Streamlit
ECS + Fargate
Managed UI container
Store uploads
S3
Durable source documents
Store OKF Markdown
S3
Durable knowledge artifacts
Run Qdrant
EC2 + EBS / managed option
Persistent vector search
Structured metadata
RDS PostgreSQL
Relational records
HTTPS entry
ALB + ACM
TLS and routing
DNS
Route 53
Application domain
Secrets
Secrets Manager
API keys/credentials
Docker registry
ECR
Private images
Logs/metrics
CloudWatch
Observability
Audit
CloudTrail
AWS activity
CI/CD
CodeBuild + CodePipeline
Build/deploy
Network
VPC
Isolation and routing
Web protection
WAF
HTTP filtering
