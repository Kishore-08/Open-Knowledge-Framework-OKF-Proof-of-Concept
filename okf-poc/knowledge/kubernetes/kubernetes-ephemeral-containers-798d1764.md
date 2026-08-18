---
id: kubernetes-ephemeral-containers-798d1764
type: concept
title: Ephemeral Containers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Ephemeral Containers

FEATURE STATE:
`Kubernetes v1.25 [stable]`

This page provides an overview of ephemeral containers: a special type of container
that runs temporarily in an existing [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") to
accomplish user-initiated actions such as troubleshooting. You use ephemeral
containers to inspect services rather than to build applications.