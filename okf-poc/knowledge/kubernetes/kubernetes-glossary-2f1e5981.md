---
id: kubernetes-glossary-2f1e5981
type: concept
title: Glossary
description: Pod level resources specification
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Glossary

Pod level resources specification
:   The resource budget defined at the Pod level in `.spec.resources`, that
    specifies the collective requests and limits for the entire pod.

Guaranteed Container
:   Within the context of this feature, a container is considered `Guaranteed`
    if it specifies resource requests equal to its limits for both CPU
    (exclusive CPU allocation requires a positive integer value) and Memory.
    This status makes it eligible for exclusive resource allocation from the
    resource managers.

Exclusive slice
:   A dedicated portion of resources (for example: specific CPUs or memory
    pages) allocated solely to a single container, ensuring isolation from other
    containers.

Pod shared pool
:   The subset of a pod's allocated resources that remains after all exclusive
    slices have been reserved. These resources are shared by all containers in
    the pod that do not receive an exclusive allocation. While containers in
    this pool share resources with each other, they are strictly isolated from
    the exclusive slices and the general node-wide shared pool.