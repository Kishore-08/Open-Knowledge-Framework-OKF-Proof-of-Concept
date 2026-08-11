---
id: tutorial-aws-services-project-guide-ci-cd-container-registry
type: concept
title: 'AWS Services Project Guide: CI/CD & Container Registry'
description: This document outlines the AWS services used for continuous integration,
  continuous deployment, and container registry management in a proof-of-concept project.
  It details the purpose, usage, and project fit for Amazon ECR, AWS CodeBuild, AWS
  CodePipeline, and AWS CodeDeploy.
category: tutorial
tags:
- AWS ECR
- AWS CodeBuild
- AWS CodePipeline
- CI/CD
- Container Registry
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Tutorial
trust_level: Medium
source_file: aws_services_project_guide.pdf
---

AWS Services Guide — OKF PoC
Page 6
5. CI/CD & Container Registry
Amazon ECR
What it is: Private Docker container registry.
Why it is used: Your project already uses Docker images, and ECR is the natural AWS registry.
How it is used: Build, tag, scan, and push API/UI images; deploy specific immutable tags.
Project fit: Store your production container images.
AWS CodeBuild
What it is: Managed build service.
Why it is used: Can run tests, linting, Docker builds, security checks, and image publishing without maintaining a build
server.
How it is used: Define build phases in buildspec.yml and authenticate to ECR.
Project fit: AWS-native CI option; GitHub Actions/Jenkins can also do this.
AWS CodePipeline
What it is: CI/CD orchestration service.
Why it is used: Connects source, build, approval, and deployment stages.
How it is used: Typical flow: source → CodeBuild → ECR → ECS deployment.
Project fit: Useful for demonstrating an end-to-end AWS DevOps pipeline.
AWS CodeDeploy
What it is: Deployment automation.
Why it is used: Helps automate controlled deployments and supported blue/green strategies.
How it is used: Configure deployment groups and deployment hooks for the chosen compute target.
Project fit: Useful when releases need stronger rollout control.
