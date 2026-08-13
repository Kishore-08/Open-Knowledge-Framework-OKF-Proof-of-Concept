---
id: kubernetes-motivation-0cf968e6
type: concept
title: Motivation
description: Labels enable users to map their own organizational structures onto system
  objects
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Motivation

Labels enable users to map their own organizational structures onto system objects
in a loosely coupled fashion, without requiring clients to store these mappings.

Service deployments and batch processing pipelines are often multi-dimensional entities
(e.g., multiple partitions or deployments, multiple release tracks, multiple tiers,
multiple micro-services per tier). Management often requires cross-cutting operations,
which breaks encapsulation of strictly hierarchical representations, especially rigid
hierarchies determined by the infrastructure rather than by users.

Example labels:

- `"release" : "stable"`, `"release" : "canary"`
- `"environment" : "dev"`, `"environment" : "qa"`, `"environment" : "production"`
- `"tier" : "frontend"`, `"tier" : "backend"`, `"tier" : "cache"`
- `"partition" : "customerA"`, `"partition" : "customerB"`
- `"track" : "daily"`, `"track" : "weekly"`

These are examples of
[commonly used labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/);
you are free to develop your own conventions.
Keep in mind that label Key must be unique for a given object.