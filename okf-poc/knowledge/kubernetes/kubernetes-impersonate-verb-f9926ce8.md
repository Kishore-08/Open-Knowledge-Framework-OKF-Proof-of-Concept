---
id: kubernetes-impersonate-verb-f9926ce8
type: concept
title: Impersonate verb
description: This verb allows users to impersonate and gain the rights of other users
  in the cluster.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Impersonate verb

This verb allows users to impersonate and gain the rights of other users in the cluster.
Care should be taken when granting it, to ensure that excessive permissions cannot be gained
via one of the impersonated accounts.