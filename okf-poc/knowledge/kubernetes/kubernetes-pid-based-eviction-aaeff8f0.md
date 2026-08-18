---
id: kubernetes-pid-based-eviction-aaeff8f0
type: concept
title: PID based eviction
description: You can configure kubelet to start terminating a Pod when it is misbehaving
  and consuming abnormal amount of resources.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/pid-limiting/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## PID based eviction

You can configure kubelet to start terminating a Pod when it is misbehaving and consuming abnormal amount of resources.
This feature is called eviction. You can
[Configure Out of Resource Handling](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/)
for various eviction signals.
Use `pid.available` eviction signal to configure the threshold for number of PIDs used by Pod.
You can set soft and hard eviction policies.
However, even with the hard eviction policy, if the number of PIDs growing very fast,
node can still get into unstable state by hitting the node PIDs limit.
Eviction signal value is calculated periodically and does NOT enforce the limit.

PID limiting - per Pod and per Node sets the hard limit.
Once the limit is hit, workload will start experiencing failures when trying to get a new PID.
It may or may not lead to rescheduling of a Pod,
depending on how workload reacts on these failures and how liveness and readiness
probes are configured for the Pod. However, if limits were set correctly,
you can guarantee that other Pods workload and system processes will not run out of PIDs
when one Pod is misbehaving.