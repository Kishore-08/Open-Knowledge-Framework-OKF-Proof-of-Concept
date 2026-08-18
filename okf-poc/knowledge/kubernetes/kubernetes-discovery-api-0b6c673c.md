---
id: kubernetes-discovery-api-0b6c673c
type: concept
title: Discovery API
description: Kubernetes publishes a list of all group versions and resources supported
  via
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Discovery API

Kubernetes publishes a list of all group versions and resources supported via
the Discovery API. This includes the following for each resource:

- Name
- Cluster or namespaced scope
- Endpoint URL and supported verbs
- Alternative names
- Group, version, kind

The API is available in both aggregated and unaggregated form. The aggregated
discovery serves two endpoints, while the unaggregated discovery serves a
separate endpoint for each group version.