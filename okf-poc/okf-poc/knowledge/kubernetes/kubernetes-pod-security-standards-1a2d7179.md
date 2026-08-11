---
id: kubernetes-pod-security-standards-1a2d7179
type: concept
title: Pod Security Standards
description: A detailed look at the different policy levels defined in the Pod Security
  Standards.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Pod Security Standards

A detailed look at the different policy levels defined in the Pod Security Standards.

The Pod Security Standards define three different *policies* to broadly cover the security
spectrum. These policies are *cumulative* and range from highly-permissive to highly-restrictive.
This guide outlines the requirements of each policy.

| Profile | Description |
| --- | --- |
| **Privileged** | Unrestricted policy, providing the widest possible level of permissions. This policy allows for known privilege escalations. |
| **Baseline** | Minimally restrictive policy which prevents known privilege escalations. Allows the default (minimally specified) Pod configuration. |
| **Restricted** | Heavily restricted policy, following current Pod hardening best practices. |

## Profile Details