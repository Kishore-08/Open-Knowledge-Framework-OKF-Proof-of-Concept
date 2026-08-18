---
id: kubernetes-escalate-verb-f9926ce8
type: concept
title: Escalate verb
description: Generally, the RBAC system prevents users from creating clusterroles
  with more rights than the user possesses.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Escalate verb

Generally, the RBAC system prevents users from creating clusterroles with more rights than the user possesses.
The exception to this is the `escalate` verb. As noted in the [RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#restrictions-on-role-creation-or-update),
users with this right can effectively escalate their privileges.