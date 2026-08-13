---
id: kubernetes-listing-secrets-f9926ce8
type: concept
title: Listing secrets
description: It is generally clear that allowing `get` access on Secrets will allow
  a user to read their contents.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Listing secrets

It is generally clear that allowing `get` access on Secrets will allow a user to read their contents.
It is also important to note that `list` and `watch` access also effectively allow for users to reveal the Secret contents.
For example, when a List response is returned (for example, via `kubectl get secrets -A -o yaml`), the response
includes the contents of all Secrets.