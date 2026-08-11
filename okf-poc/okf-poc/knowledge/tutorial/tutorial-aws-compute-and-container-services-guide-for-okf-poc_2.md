---
id: tutorial-aws-compute-and-container-services-guide-for-okf-poc
type: concept
title: AWS Compute and Container Services Guide for OKF PoC
description: This document outlines various AWS compute and container orchestration
  services, detailing their features, use cases, and applicability for a proof of
  concept project running FastAPI and Streamlit. It covers Amazon ECS, AWS Fargate,
  Amazon EKS, and Amazon EC2, highlighting their pros and cons for co
category: tutorial
tags:
- AWS
- Containers
- ECS
- Fargate
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
Page 3
2. Compute & Containers
Amazon ECS
What it is: Managed container orchestration for Docker workloads.
Why it is used: Your application is already containerized, so ECS is a natural path from Docker Compose to AWS.
How it is used: Build images, push them to ECR, define ECS task definitions, and run ECS services with a desired task
count.
Project fit: Run FastAPI and Streamlit as separate services.
AWS Fargate
What it is: Serverless compute for ECS containers where AWS manages the underlying servers.
Why it is used: Avoids EC2 instance administration and is convenient for a small production-like PoC.
How it is used: Specify CPU, memory, image, ports, environment, networking, and IAM task role in the ECS task
definition.
Project fit: Run API/UI containers without maintaining worker VMs.
Amazon EKS
What it is: Managed Kubernetes control plane.
Why it is used: Useful if you want Kubernetes-native deployments, Helm, ingress, autoscaling, and deeper DevOps
practice.
How it is used: Deploy Kubernetes Deployments/Services/Ingress and connect workloads to AWS resources through
IAM integrations.
Project fit: Strong advanced option because the project already uses Docker/Kubernetes concepts, but more complex
than Fargate.
Amazon EC2
What it is: Virtual machines in AWS.
Why it is used: Useful when you need OS-level control or want the closest cloud equivalent to a Docker-on-VM setup.
How it is used: Launch an instance, install Docker, configure security groups, and run containers.
Project fit: Good migration path for a simple PoC, but you maintain the VM.
