---
id: kubernetes-container-probes-3e34f258
type: concept
title: Container probes
description: Kubernetes lets you define *probes* to continuously monitor the health
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Container probes

Kubernetes lets you define *probes* to continuously monitor the health
of containers in a Pod. A probe is a diagnostic performed periodically
by the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") on a container.
To perform a diagnostic, the kubelet either executes code within
the container or makes a network request.

Based on the probe results, Kubernetes can restart unhealthy containers
or stop sending traffic to containers that are not ready.

The kubelet can optionally perform and react to three kinds of probes on running
containers, each serving a different purpose. For probe mechanisms (`exec`,
`grpc`, `httpGet`, `tcpSocket`), configuration fields, and detailed usage
guidance, see [Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/).