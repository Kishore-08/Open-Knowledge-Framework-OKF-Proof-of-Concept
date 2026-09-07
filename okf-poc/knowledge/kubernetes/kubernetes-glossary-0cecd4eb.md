---
id: kubernetes-glossary-0cecd4eb
type: concept
title: Glossary
description: Pod level resources specification
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Glossary

Pod level resources specification
:   The resource budget defined at the Pod level in `.spec.resources`, that
    specifies the collective requests and limits for the entire Pod.

Guaranteed container
:   A container that specifies resource requests equal to its limits for both
    CPU (exclusive CPU allocation requires a positive integer value) and Memory.
    Consistent with existing `kubelet` behavior, this makes the container
    eligible for exclusive resource allocation from the resource managers.

Exclusive slice
:   A dedicated portion of resources (for example: specific CPUs or memory
    pages) allocated solely to a single container, ensuring isolation from other
    containers.

Pod shared pool
:   The subset of a Pod's allocated resources that remains after all exclusive
    slices have been reserved. These resources are shared by all containers in
    the Pod that do not receive an exclusive allocation. While containers in
    this pool share resources with each other, they are strictly isolated from
    the exclusive slices and the general node-wide shared pool.

## How pod-level resource managers work

The CPU and Memory resource managers operate differently depending on the
configured Topology Manager scope.