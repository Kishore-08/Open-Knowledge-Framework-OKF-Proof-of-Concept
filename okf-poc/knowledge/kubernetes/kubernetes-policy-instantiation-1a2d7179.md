---
id: kubernetes-policy-instantiation-1a2d7179
type: concept
title: Policy Instantiation
description: Decoupling policy definition from policy instantiation allows for a common
  understanding and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Policy Instantiation

Decoupling policy definition from policy instantiation allows for a common understanding and
consistent language of policies across clusters, independent of the underlying enforcement
mechanism.

As mechanisms mature, they will be defined below on a per-policy basis. The methods of enforcement
of individual policies are not defined here.

[**Pod Security Admission Controller**](https://kubernetes.io/docs/concepts/security/pod-security-admission/)

- [Privileged namespace](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/security/podsecurity-privileged.yaml)
- [Baseline namespace](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/security/podsecurity-baseline.yaml)
- [Restricted namespace](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/security/podsecurity-restricted.yaml)