---
id: kubernetes-periodic-review-f9926ce8
type: concept
title: Periodic review
description: It is vital to periodically review the Kubernetes RBAC settings for redundant
  entries and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Periodic review

It is vital to periodically review the Kubernetes RBAC settings for redundant entries and
possible privilege escalations.
If an attacker is able to create a user account with the same name as a deleted user,
they can automatically inherit all the rights of the deleted user, especially the
rights assigned to that user.