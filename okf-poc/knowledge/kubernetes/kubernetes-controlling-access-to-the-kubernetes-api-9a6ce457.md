---
id: kubernetes-controlling-access-to-the-kubernetes-api-9a6ce457
type: concept
title: Controlling Access to the Kubernetes API
description: This page provides an overview of controlling access to the Kubernetes
  API.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/controlling-access/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Controlling Access to the Kubernetes API

This page provides an overview of controlling access to the Kubernetes API.

Users access the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) using `kubectl`,
client libraries, or by making REST requests. Both human users and
[Kubernetes service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) can be
authorized for API access.
When a request reaches the API, it goes through several stages, illustrated in the
following diagram: