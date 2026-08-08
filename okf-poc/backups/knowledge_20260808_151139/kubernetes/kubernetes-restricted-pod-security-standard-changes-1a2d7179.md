---
id: kubernetes-restricted-pod-security-standard-changes-1a2d7179
type: concept
title: Restricted Pod Security Standard changes
description: Another important change, made in Kubernetes v1.25 is that the *Restricted*
  policy
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Restricted Pod Security Standard changes

Another important change, made in Kubernetes v1.25 is that the *Restricted* policy
has been updated to use the `pod.spec.os.name` field. Based on the OS name, certain policies that are specific
to a particular OS can be relaxed for the other OS.

#### OS-specific policy controls

Restrictions on the following controls are only required if `.spec.os.name` is not `windows`:

- Privilege Escalation
- Seccomp
- Linux Capabilities