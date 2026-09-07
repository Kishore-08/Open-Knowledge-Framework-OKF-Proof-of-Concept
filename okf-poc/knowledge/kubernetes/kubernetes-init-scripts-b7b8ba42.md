---
id: kubernetes-init-scripts-b7b8ba42
type: concept
title: Init scripts
description: It is certainly possible to run daemon processes by directly starting
  them on a node (e.g. using
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Init scripts

It is certainly possible to run daemon processes by directly starting them on a node (e.g. using
`init`, `upstartd`, or `systemd`). This is perfectly fine. However, there are several advantages to
running such processes via a DaemonSet:

- Ability to monitor and manage logs for daemons in the same way as applications.
- Same config language and tools (e.g. Pod templates, `kubectl`) for daemons and applications.
- Running daemons in containers with resource limits increases isolation between daemons from app
  containers. However, this can also be accomplished by running the daemons in a container but not in a Pod.