---
id: kubernetes-hardening-f9926ce8
type: concept
title: Hardening
description: Kubernetes defaults to providing access which may not be required in
  every cluster. Reviewing
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Hardening

Kubernetes defaults to providing access which may not be required in every cluster. Reviewing
the RBAC rights provided by default can provide opportunities for security hardening.
In general, changes should not be made to rights provided to `system:` accounts some options
to harden cluster rights exist:

- Review bindings for the `system:unauthenticated` group and remove them where possible, as this gives
  access to anyone who can contact the API server at a network level.
- Avoid the default auto-mounting of service account tokens by setting
  `automountServiceAccountToken: false`. For more details, see
  [using default service account token](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server).
  Setting this value for a Pod will overwrite the service account setting, workloads
  which require service account tokens can still mount them.