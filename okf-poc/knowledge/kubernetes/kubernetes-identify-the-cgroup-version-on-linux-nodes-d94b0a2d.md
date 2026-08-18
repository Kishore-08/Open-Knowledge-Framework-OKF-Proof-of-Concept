---
id: kubernetes-identify-the-cgroup-version-on-linux-nodes-d94b0a2d
type: concept
title: Identify the cgroup version on Linux Nodes
description: The cgroup version depends on the Linux distribution being used and the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cgroups/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Identify the cgroup version on Linux Nodes

The cgroup version depends on the Linux distribution being used and the
default cgroup version configured on the OS. To check which cgroup version your
distribution uses, run the `stat -fc %T /sys/fs/cgroup/` command on
the node:

```
stat -fc %T /sys/fs/cgroup/
```

For cgroup v2, the output is `cgroup2fs`.

For cgroup v1, the output is `tmpfs.`