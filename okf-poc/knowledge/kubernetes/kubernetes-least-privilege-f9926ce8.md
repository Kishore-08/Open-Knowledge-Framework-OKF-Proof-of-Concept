---
id: kubernetes-least-privilege-f9926ce8
type: concept
title: Least privilege
description: Ideally, minimal RBAC rights should be assigned to users and service
  accounts. Only permissions
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Least privilege

Ideally, minimal RBAC rights should be assigned to users and service accounts. Only permissions
explicitly required for their operation should be used. While each cluster will be different,
some general rules that can be applied are :

- Assign permissions at the namespace level where possible. Use RoleBindings as opposed to
  ClusterRoleBindings to give users rights only within a specific namespace.
- Avoid providing wildcard permissions when possible, especially to all resources.
  As Kubernetes is an extensible system, providing wildcard access gives rights
  not just to all object types that currently exist in the cluster, but also to all object types
  which are created in the future.
- Administrators should not use `cluster-admin` accounts except where specifically needed.
  Providing a low privileged account with
  [impersonation rights](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation)
  can avoid accidental modification of cluster resources.
- Avoid adding users to the `system:masters` group. Any user who is a member of this group
  bypasses all RBAC rights checks and will always have unrestricted superuser access, which cannot be
  revoked by removing RoleBindings or ClusterRoleBindings. As an aside, if a cluster is
  using an authorization webhook, membership of this group also bypasses that webhook (requests
  from users who are members of that group are never sent to the webhook)