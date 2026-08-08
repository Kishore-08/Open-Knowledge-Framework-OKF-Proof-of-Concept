---
id: kubernetes-deploying-operators-d41317cc
type: concept
title: Deploying operators
description: The most common way to deploy an operator is to add the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Deploying operators

The most common way to deploy an operator is to add the
Custom Resource Definition and its associated Controller to your cluster.
The Controller will normally run outside of the
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers."),
much as you would run any containerized application.
For example, you can run the controller in your cluster as a Deployment.