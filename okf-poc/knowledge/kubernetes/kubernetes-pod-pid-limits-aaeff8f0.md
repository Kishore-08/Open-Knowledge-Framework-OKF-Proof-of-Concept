---
id: kubernetes-pod-pid-limits-aaeff8f0
type: concept
title: Pod PID limits
description: Kubernetes allows you to limit the number of processes running in a Pod.
  You
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/pid-limiting/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Pod PID limits

Kubernetes allows you to limit the number of processes running in a Pod. You
specify this limit at the node level, rather than configuring it as a resource
limit for a particular Pod. Each Node can have a different PID limit.  
To configure the limit, you can specify the command line parameter `--pod-max-pids`
to the kubelet, or set `PodPidsLimit` in the kubelet
[configuration file](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/).