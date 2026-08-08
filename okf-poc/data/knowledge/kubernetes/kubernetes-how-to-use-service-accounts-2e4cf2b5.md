---
id: kubernetes-how-to-use-service-accounts-2e4cf2b5
type: concept
title: How to use service accounts
description: 'To use a Kubernetes service account, you do the following:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/service-accounts/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## How to use service accounts

To use a Kubernetes service account, you do the following:

1. Create a ServiceAccount object using a Kubernetes
   client like `kubectl` or a manifest that defines the object.
2. Grant permissions to the ServiceAccount object using an authorization
   mechanism such as
   [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).
3. Assign the ServiceAccount object to Pods during Pod creation.

   If you're using the identity from an external service,
   [retrieve the ServiceAccount token](https://kubernetes.io/docs/concepts/security/service-accounts/#get-a-token) and use it from that
   service instead.

For instructions, refer to
[Configure Service Accounts for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/).