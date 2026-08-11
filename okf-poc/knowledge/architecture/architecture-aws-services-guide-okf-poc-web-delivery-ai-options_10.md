---
id: architecture-aws-services-guide-okf-poc-web-delivery-ai-options
type: concept
title: 'AWS Services Guide — OKF PoC: Web Delivery & AI Options'
description: This document outlines various AWS services evaluated for an OKF Proof
  of Concept, specifically focusing on web delivery, security, and AI integrations.
  It details the purpose, usage, and project fit for Amazon CloudFront, AWS WAF, Amazon
  Bedrock, and AWS Lambda, helping architects determine which c
category: architecture
tags:
- AWS
- Cloud Security
- Content Delivery Network
- Serverless Compute
- Artificial Intelligence
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
Page 8
7. Web Delivery & AI Options
Amazon CloudFront
What it is: Content delivery network.
Why it is used: Improves edge delivery and can provide an HTTPS edge entry point.
How it is used: Put CloudFront in front of S3 or an HTTP origin such as an ALB and configure caching.
Project fit: Optional for the PoC; useful for public multi-region users.
AWS WAF
What it is: Web application firewall.
Why it is used: Filters malicious or unwanted HTTP traffic and can use AWS managed rules.
How it is used: Attach WAF to CloudFront or ALB and configure rules and rate limits.
Project fit: Recommended once the AI assistant is publicly exposed.
Amazon Bedrock
What it is: Managed AWS platform for foundation-model access.
Why it is used: Provides an AWS-native alternative if you later want to use supported foundation models instead of or
alongside Gemini.
How it is used: Call supported models through Bedrock APIs using IAM permissions.
Project fit: Optional; it is an LLM platform alternative, not a requirement.
AWS Lambda
What it is: Event-driven serverless compute.
Why it is used: Useful for lightweight processing triggered by events such as an S3 upload.
How it is used: Create an event trigger and execute a short function.
Project fit: Optional; your heavier ingestion pipeline may be better suited to ECS workers.
