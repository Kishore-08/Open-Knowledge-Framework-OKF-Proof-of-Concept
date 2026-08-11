---
id: kubernetes-pod-security-levels-ebd20ed7
type: concept
title: Pod Security levels
description: Pod Security admission places requirements on a Pod's [Security
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod Security levels

Pod Security admission places requirements on a Pod's [Security
Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) and other related fields according
to the three levels defined by the [Pod Security
Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/): `privileged`, `baseline`, and
`restricted`. Refer to the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/)
page for an in-depth look at those requirements.