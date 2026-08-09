---
id: tutorial-aws-services-guide-for-web-delivery-and-ai-options
type: concept
title: AWS Services Guide for Web Delivery and AI Options
description: This document outlines various AWS services, including Amazon CloudFront,
  AWS WAF, Amazon Bedrock, and AWS Lambda, detailing their purpose, usage, and fit
  for the OKF PoC project. It provides guidance on leveraging these services for content
  delivery, security, foundation model access, and serverles
category: tutorial
tags:
- Amazon CloudFront
- AWS WAF
- Amazon Bedrock
- AWS Lambda
- Cloud Architecture
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
