---
id: architecture-aws-service-mapping-guide-for-okf-poc
type: concept
title: AWS Service Mapping Guide for OKF PoC
description: 'This document outlines the AWS service architecture and mapping required
  for an OKF Proof of Concept (PoC) project. It details how various AWS services,
  such as ECS, S3, RDS, and Route 53, are mapped to specific application requirements
  like running FastAPI, storing Markdown artifacts, and managing '
category: architecture
tags:
- AWS
- Cloud Architecture
- Infrastructure Mapping
- Container Deployment
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: Architecture
trust_level: High
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
