---
id: kubernetes-pod-level-security-isolation-f312a3ee
type: concept
title: Pod-level security isolation
description: Linux-specific pod security context mechanisms (such as SELinux, AppArmor,
  Seccomp, or custom
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/windows-security/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Pod-level security isolation

Linux-specific pod security context mechanisms (such as SELinux, AppArmor, Seccomp, or custom
POSIX capabilities) are not supported on Windows nodes.

Privileged containers are [not supported](https://kubernetes.io/docs/concepts/windows/intro/#compatibility-v1-pod-spec-containers-securitycontext)
on Windows.
Instead [HostProcess containers](https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/)
can be used on Windows to perform many of the tasks performed by privileged containers on Linux.