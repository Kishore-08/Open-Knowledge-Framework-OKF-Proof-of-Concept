---
id: kubernetes-bind-verb-f9926ce8
type: concept
title: Bind verb
description: Similar to the `escalate` verb, granting users this right allows for
  the bypass of Kubernetes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Bind verb

Similar to the `escalate` verb, granting users this right allows for the bypass of Kubernetes
in-built protections against privilege escalation, allowing users to create bindings to
roles with rights they do not already have.