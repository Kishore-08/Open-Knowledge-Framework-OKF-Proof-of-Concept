---
id: kubernetes-requirements-d94b0a2d
type: concept
title: Requirements
description: 'cgroup v2 has the following requirements:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cgroups/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Requirements

cgroup v2 has the following requirements:

- OS distribution enables cgroup v2
- Linux Kernel version is 5.8 or later
- Container runtime supports cgroup v2. For example:
  - [containerd](https://containerd.io/) v1.4 and later
  - [cri-o](https://cri-o.io/) v1.20 and later
- The kubelet and the container runtime are configured to use the [systemd cgroup driver](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#systemd-cgroup-driver)