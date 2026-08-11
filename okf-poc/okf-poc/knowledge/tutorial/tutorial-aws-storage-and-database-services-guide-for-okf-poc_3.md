---
id: tutorial-aws-storage-and-database-services-guide-for-okf-poc
type: concept
title: AWS Storage and Database Services Guide for OKF PoC
description: This document outlines various AWS storage and database services, including
  Amazon S3, EBS, RDS, and DynamoDB. It details their descriptions, use cases, implementation
  methods, and specific project fits for the OKF Proof of Concept architecture.
category: tutorial
tags:
- Amazon S3
- Amazon EBS
- Amazon RDS
- Amazon DynamoDB
- Cloud Storage
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
Page 4
3. Storage & Databases
Amazon S3
What it is: Durable object storage.
Why it is used: Ideal for PDFs, Markdown, TXT, JSON, generated OKF files, backups, and other artifacts.
How it is used: Create prefixes such as uploads/, raw/, knowledge/, and backups/. Access S3 through IAM roles.
Project fit: Recommended durable storage for uploaded source documents and generated OKF Markdown.
Amazon EBS
What it is: Persistent block storage for EC2.
Why it is used: Useful when self-hosting Qdrant or another database on EC2 and needing persistent disk.
How it is used: Attach and mount an EBS volume and keep database data there.
Project fit: Useful for a self-managed Qdrant-on-EC2 architecture.
Amazon RDS
What it is: Managed relational database service.
Why it is used: Useful for structured metadata such as users, ingestion jobs, document records, and audit information.
How it is used: Use PostgreSQL/MySQL privately in a VPC and retrieve credentials from Secrets Manager.
Project fit: Optional; it complements rather than replaces Qdrant.
Amazon DynamoDB
What it is: Managed NoSQL key-value/document database.
Why it is used: Useful for high-scale, simple job state, sessions, or document processing records.
How it is used: Create tables keyed by job/document ID and access them using IAM.
Project fit: Optional; use when the data model favors key-value/document access.
