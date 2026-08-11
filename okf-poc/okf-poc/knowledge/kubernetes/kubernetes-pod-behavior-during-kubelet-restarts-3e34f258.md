---
id: kubernetes-pod-behavior-during-kubelet-restarts-3e34f258
type: concept
title: Pod behavior during kubelet restarts
description: If you restart the kubelet, Pods (and their containers) continue to run
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod behavior during kubelet restarts

If you restart the kubelet, Pods (and their containers) continue to run
even during the restart.
When there are running Pods on a node, stopping or restarting the kubelet
on that node does **not** cause the kubelet to stop all local Pods
before the kubelet itself stops.
To stop the Pods on a node, you can use `kubectl drain`.