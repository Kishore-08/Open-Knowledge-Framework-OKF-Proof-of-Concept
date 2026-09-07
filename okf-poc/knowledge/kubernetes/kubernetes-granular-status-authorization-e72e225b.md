---
id: kubernetes-granular-status-authorization-e72e225b
type: concept
title: Granular status authorization
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Granular status authorization

FEATURE STATE:
`Kubernetes v1.36 [beta]`(enabled by default)

Starting in Kubernetes v1.36, DRA enforces fine-grained authorization checks for updates
to `ResourceClaim` status by using synthetic subresources and node-aware verbs.

For security hardening guidance, including RBAC examples for scheduler and DRA
drivers, see
[Hardening Guide - Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/).

For a step-by-step cluster administrator procedure, see
[Harden Dynamic Resource Allocation in Your Cluster](https://kubernetes.io/docs/tasks/administer-cluster/hardening-dra/).