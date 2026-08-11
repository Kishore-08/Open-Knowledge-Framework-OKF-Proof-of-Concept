---
id: architecture-aws-services-guide-for-okf-poc-networking-and-security
type: concept
title: AWS Services Guide for OKF PoC - Networking and Security
description: This document outlines the core AWS networking and security services
  required for the OKF Proof of Concept deployment. It details the utilization of
  Amazon VPC, Application Load Balancers, Route 53, IAM, and AWS Secrets Manager to
  ensure a secure, production-style infrastructure.
category: architecture
tags:
- AWS
- Cloud Security
- Networking
- Identity and Access Management
- Secrets Management
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
Page 5
4. Networking & Security
Amazon VPC
What it is: Private networking boundary for AWS resources.
Why it is used: Keeps internal workloads and databases away from direct public exposure.
How it is used: Use public subnets for internet-facing entry points and private subnets for internal services; control traffic
with security groups.
Project fit: Foundation for a production-style deployment.
Application Load Balancer
What it is: HTTP/HTTPS Layer-7 load balancer.
Why it is used: Provides a stable endpoint and routes requests to healthy containers.
How it is used: Create listeners, target groups, health checks, and routing rules.
Project fit: Front FastAPI and optionally Streamlit.
Amazon Route 53
What it is: Managed DNS.
Why it is used: Provides a friendly domain instead of an ALB hostname.
How it is used: Create DNS records and alias them to ALB or CloudFront.
Project fit: Use for a public application domain.
AWS IAM
What it is: Identity and access management.
Why it is used: Controls which users and workloads can access S3, ECR, Secrets Manager, CloudWatch, and other
resources.
How it is used: Use least-privilege roles for ECS tasks, CI/CD, and administrators.
Project fit: Critical: do not put AWS access keys in source code or images.
AWS Secrets Manager
What it is: Managed secret storage.
Why it is used: Prevents Gemini keys and database credentials from being committed to Git or baked into images.
How it is used: Store secrets and allow only the required ECS task role to retrieve them.
Project fit: Use for GEMINI_API_KEY and future credentials.
