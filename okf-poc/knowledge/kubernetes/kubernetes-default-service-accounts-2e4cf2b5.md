---
id: kubernetes-default-service-accounts-2e4cf2b5
type: concept
title: Default service accounts
description: When you create a cluster, Kubernetes automatically creates a ServiceAccount
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/service-accounts/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Default service accounts

When you create a cluster, Kubernetes automatically creates a ServiceAccount
object named `default` for every namespace in your cluster. The `default`
service accounts in each namespace get no permissions by default other than the
[default API discovery permissions](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings)
that Kubernetes grants to all authenticated principals if role-based access control (RBAC) is enabled.
If you delete the `default` ServiceAccount object in a namespace, the
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.")
replaces it with a new one.

If you deploy a Pod in a namespace, and you don't
[manually assign a ServiceAccount to the Pod](https://kubernetes.io/docs/concepts/security/service-accounts/#assign-to-pod), Kubernetes
assigns the `default` ServiceAccount for that namespace to the Pod.