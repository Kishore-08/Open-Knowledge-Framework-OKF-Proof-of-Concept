---
id: kubernetes-containers-4bbf1e9c
type: concept
title: Containers
description: Technology for packaging an application along with its runtime dependencies.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Containers

Technology for packaging an application along with its runtime dependencies.

This page will discuss containers and container images, as well as their use in operations and solution development.

The word *container* is an overloaded term. Whenever you use the word, check whether your audience uses the same definition.

Each container that you run is repeatable; the standardization from having
dependencies included means that you get the same behavior wherever you
run it.

Containers decouple applications from the underlying host infrastructure.
This makes deployment easier in different cloud or OS environments.

Each [node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") in a Kubernetes
cluster runs the containers that form the
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/) assigned to that node.
Containers in a Pod are co-located and co-scheduled to run on the same node.