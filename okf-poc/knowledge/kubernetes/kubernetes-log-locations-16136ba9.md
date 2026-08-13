---
id: kubernetes-log-locations-16136ba9
type: concept
title: Log locations
description: The way that the kubelet and container runtime write logs depends on
  the operating
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Log locations

The way that the kubelet and container runtime write logs depends on the operating
system that the node uses:



On Linux nodes that use systemd, the kubelet and container runtime write to journald
by default. You use `journalctl` to read the systemd journal; for example:
`journalctl -u kubelet`.

If systemd is not present, the kubelet and container runtime write to `.log` files in the
`/var/log` directory. If you want to have logs written elsewhere, you can indirectly
run the kubelet via a helper tool, `kube-log-runner`, and use that tool to redirect
kubelet logs to a directory that you choose.

By default, kubelet directs your container runtime to write logs into directories within
`/var/log/pods`.

For more information on `kube-log-runner`, read [System Logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/#klog).

By default, the kubelet writes logs to files within the directory `C:\var\logs`
(notice that this is not `C:\var\log`).

Although `C:\var\log` is the Kubernetes default location for these logs, several
cluster deployment tools set up Windows nodes to log to `C:\var\log\kubelet` instead.

If you want to have logs written elsewhere, you can indirectly
run the kubelet via a helper tool, `kube-log-runner`, and use that tool to redirect
kubelet logs to a directory that you choose.

However, by default, kubelet directs your container runtime to write logs within the
directory `C:\var\log\pods`.

For more information on `kube-log-runner`, read [System Logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/#klog).

For Kubernetes cluster components that run in pods, these write to files inside
the `/var/log` directory, bypassing the default logging mechanism (the components
do not write to the systemd journal). You can use Kubernetes' storage mechanisms
to map persistent storage into the container that runs the component.

Kubelet allows changing the pod logs directory from default `/var/log/pods`
to a custom path. This adjustment can be made by configuring the `podLogsDir`
parameter in the kubelet's configuration file.

#### Caution:

It's important to note that the default location `/var/log/pods` has been in use for
an extended period and certain processes might implicitly assume this path.
Therefore, altering this parameter must be approached with caution and at your own risk.

Another caveat to keep in mind is that the kubelet supports the location being on the same
disk as `/var`. Otherwise, if the logs are on a separate filesystem from `/var`,
then the kubelet will not track that filesystem's usage, potentially leading to issues if
it fills up.

For details about etcd and its logs, view the [etcd documentation](https://etcd.io/docs/).
Again, you can use Kubernetes' storage mechanisms to map persistent storage into
the container that runs the component.

#### Note:

If you deploy Kubernetes cluster components (such as the scheduler) to log to
a volume shared from the parent node, you need to consider and ensure that those
logs are rotated. **Kubernetes does not manage that log rotation**.

Your operating system may automatically implement some log rotation - for example,
if you share the directory `/var/log` into a static Pod for a component, node-level
log rotation treats a file in that directory the same as a file written by any component
outside Kubernetes.

Some deploy tools account for that log rotation and automate it; others leave this
as your responsibility.