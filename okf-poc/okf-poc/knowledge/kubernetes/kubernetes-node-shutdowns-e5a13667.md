---
id: kubernetes-node-shutdowns-e5a13667
type: concept
title: Node Shutdowns
description: In a Kubernetes cluster, a [node](https://kubernetes.io/docs/concepts/architecture/nodes/
  "A node is a worker machine in Kubernetes.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Node Shutdowns

In a Kubernetes cluster, a [node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.")
can be shut down in a planned graceful way or unexpectedly because of reasons such
as a power outage or something else external. A node shutdown could lead to workload
failure if the node is not drained before the shutdown. A node shutdown can be
either **graceful** or **non-graceful**.

#### Caution:

The `unattended-upgrades` package from Debian conflicts with node graceful shutdown in
its normal configuration.
If you use the default configuration of `unattended-upgrades`, which customizes the server shutdown
grace period, then the kubelet fails to obtain the necessary lock to handle shutdown events properly.

This happens if the `shutdownGracePeriod` value is greater than 30 seconds.
To avoid this, you can suppress part of the `unattended-upgrades` configuration,
by making `/etc/systemd/logind.conf.d/unattended-upgrades-logind-maxdelay.conf` be a symbolic link
to `/dev/null`.

For more details, refer to the
[`logind.conf` documentation](https://www.freedesktop.org/software/systemd/man/latest/logind.conf.html).