---
id: kubernetes-node-pid-limits-aaeff8f0
type: concept
title: Node PID limits
description: Kubernetes allows you to reserve a number of process IDs for the system
  use. To
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/pid-limiting/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Node PID limits

Kubernetes allows you to reserve a number of process IDs for the system use. To
configure the reservation, use the parameter `pid=<number>` in the
`--system-reserved` and `--kube-reserved` command line options to the kubelet.
The value you specified declares that the specified number of process IDs will
be reserved for the system as a whole and for Kubernetes system daemons
respectively.