---
id: kubernetes-what-s-the-difference-between-a-security-profile-and-a-secur-1a2d7179
type: concept
title: What's the difference between a security profile and a security context?
description: '[Security Contexts](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/)
  configure Pods and'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### What's the difference between a security profile and a security context?

[Security Contexts](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) configure Pods and
Containers at runtime. Security contexts are defined as part of the Pod and container specifications
in the Pod manifest, and represent parameters to the container runtime.

Security profiles are control plane mechanisms to enforce specific settings in the Security Context,
as well as other related parameters outside the Security Context. As of July 2021,
[Pod Security Policies](https://kubernetes.io/docs/concepts/security/pod-security-policy/) are deprecated in favor of the
built-in [Pod Security Admission Controller](https://kubernetes.io/docs/concepts/security/pod-security-admission/).