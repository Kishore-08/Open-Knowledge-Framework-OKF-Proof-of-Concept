---
id: kubernetes-role-based-access-control-good-practices-f9926ce8
type: concept
title: Role Based Access Control Good Practices
description: Principles and practices for good RBAC design for cluster operators.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Role Based Access Control Good Practices

Principles and practices for good RBAC design for cluster operators.

Kubernetes [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "Manages authorization decisions, allowing admins to dynamically configure access policies through the Kubernetes API.") is a key security control
to ensure that cluster users and workloads have only the access to resources required to
execute their roles. It is important to ensure that, when designing permissions for cluster
users, the cluster administrator understands the areas where privilege escalation could occur,
to reduce the risk of excessive access leading to security incidents.

The good practices laid out here should be read in conjunction with the general
[RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#restrictions-on-role-creation-or-update).

## General good practice