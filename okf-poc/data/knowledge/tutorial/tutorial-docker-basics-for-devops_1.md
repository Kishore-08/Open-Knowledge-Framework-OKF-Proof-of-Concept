---
id: tutorial-docker-basics-for-devops
type: concept
title: Docker Basics for DevOps
description: This document provides an introduction to Docker containerization, covering
  core concepts like images and containers, essential CLI commands, a minimal Dockerfile
  example, and key production best practices. It serves as a foundational guide for
  integrating Docker into CI/CD pipelines.
category: tutorial
tags:
- Docker
- Containers
- Dockerfile
- DevOps
- CI/CD
source:
  name: Ingested document
  url: ''
created_at: '2026-08-08'
updated_at: '2026-08-08'
aliases: []
related: []
document_type: Tutorial
trust_level: Medium
source_file: docker-basics.txt
---

# Docker Basics for DevOps

Docker is a containerization platform that packages an application with all its
dependencies into a portable container image. Containers run the same on any
machine, which removes the classic "it works on my machine" problem.

## Images and Containers

A Docker image is a read-only template with instructions for creating a
container. A container is a runnable instance of an image. You build an image
from a Dockerfile, then run containers from that image.

Common commands:

- `docker build -t myapp .` builds an image named myapp from the Dockerfile in
  the current directory.
- `docker run -d -p 8080:80 myapp` starts a container in detached mode and maps
  host port 8080 to container port 80.
- `docker ps` lists running containers.
- `docker images` lists local images.
- `docker exec -it <container> sh` opens a shell inside a running container.

## A Minimal Dockerfile

FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]

The FROM line picks a base image, COPY copies files, RUN executes build steps,
EXPOSE documents the port, and CMD defines the startup command.

## Best Practices

- Use small base images such as alpine variants to reduce attack surface and
  download size.
- Keep images layered and cached-friendly: copy dependency manifests before
  application source code.
- Run containers as a non-root user.
- Tag images with meaningful versions and never use the latest tag in
  production deployments.

Docker is the foundation of most CI/CD pipelines: build the image, push it to a
container registry, and deploy it to Kubernetes or a server.
