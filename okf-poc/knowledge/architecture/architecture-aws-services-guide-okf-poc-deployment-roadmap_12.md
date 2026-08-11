---
id: architecture-aws-services-guide-okf-poc-deployment-roadmap
type: concept
title: AWS Services Guide — OKF PoC Deployment Roadmap
description: This document outlines a five-phase AWS deployment roadmap for an OKF
  Proof of Concept, detailing the transition from a minimum cloud deployment to production
  networking, data reliability, DevOps, and a potential Kubernetes path. It emphasizes
  securing and scaling infrastructure around a knowledge r
category: architecture
tags:
- AWS
- Cloud Architecture
- DevOps
- Kubernetes
- Infrastructure Roadmap
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
Page 11
10. Recommended AWS Roadmap
Phase 1 — Minimum cloud deployment
 ECR for Docker images.
 ECS/Fargate for API and UI.
 S3 for uploads and generated knowledge artifacts.
 Secrets Manager for Gemini credentials.
 CloudWatch for logs.
 IAM least-privilege roles.
Phase 2 — Production networking
 VPC with public/private subnet separation.
 Application Load Balancer.
 ACM for HTTPS certificates.
 Route 53 for DNS.
 Restricted security groups.
Phase 3 — Data reliability
 RDS PostgreSQL if structured metadata is needed.
 Persistent Qdrant storage or a managed vector option.
 S3 versioning and lifecycle policies.
 Backups and disaster recovery.
Phase 4 — DevOps and security
 CI/CD using GitHub Actions or CodeBuild/CodePipeline.
 ECR image scanning and immutable tags.
 CloudTrail audit logging.
 WAF for public endpoints.
 CloudWatch dashboards and alarms.
Phase 5 — Kubernetes path
 Use EKS if Kubernetes is a deployment requirement.
 Deploy with Helm and Kubernetes Services/Ingress.
 Add autoscaling and centralized observability.
Key principle: keep the OKF knowledge repository as the source of truth, Qdrant as the retrieval index, and Gemini as the
answer-generation layer. AWS should provide secure, durable, observable infrastructure around these components.
