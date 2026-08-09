---
id: kubernetes-privileged-1a2d7179
type: concept
title: Privileged
description: '**The *Privileged* policy is purposely-open, and entirely unrestricted.**
  This type of policy is'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Privileged

**The *Privileged* policy is purposely-open, and entirely unrestricted.** This type of policy is
typically aimed at system- and infrastructure-level workloads managed by privileged, trusted users.

The Privileged policy is defined by an absence of restrictions. If you define a Pod where the Privileged
security policy applies, the Pod you define is able to bypass typical container isolation mechanisms.
For example, you can define a Pod that has access to the node's host network.