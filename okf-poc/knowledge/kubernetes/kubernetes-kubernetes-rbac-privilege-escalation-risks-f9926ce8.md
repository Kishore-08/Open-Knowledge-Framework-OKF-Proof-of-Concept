---
id: kubernetes-kubernetes-rbac-privilege-escalation-risks-f9926ce8
type: concept
title: Kubernetes RBAC - privilege escalation risks
description: Within Kubernetes RBAC there are a number of privileges which, if granted,
  can allow a user or a service account
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Kubernetes RBAC - privilege escalation risks

Within Kubernetes RBAC there are a number of privileges which, if granted, can allow a user or a service account
to escalate their privileges in the cluster or affect systems outside the cluster.

This section is intended to provide visibility of the areas where cluster operators
should take care, to ensure that they do not inadvertently allow for more access to clusters than intended.