---
id: kubernetes-namespace-modification-f9926ce8
type: concept
title: Namespace modification
description: Users who can perform **patch** operations on Namespace objects (through
  a namespaced RoleBinding to a Role with that access) can modify
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Namespace modification

Users who can perform **patch** operations on Namespace objects (through a namespaced RoleBinding to a Role with that access) can modify
labels on that namespace. In clusters where Pod Security Admission is used, this may allow a user to configure the namespace
for a more permissive policy than intended by the administrators.
For clusters where NetworkPolicy is used, users may be set labels that indirectly allow
access to services that an administrator did not intend to allow.

## Kubernetes RBAC - denial of service risks