---
id: kubernetes-resource-sharing-within-containers-0818d160
type: concept
title: Resource sharing within containers
description: Given the order of execution for init, sidecar and app containers, the
  following rules
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Resource sharing within containers

Given the order of execution for init, sidecar and app containers, the following rules
for resource usage apply:

- The highest of any particular resource request or limit defined on all init
  containers is the *effective init request/limit*. If any resource has no
  resource limit specified this is considered as the highest limit.
- The Pod's *effective request/limit* for a resource is the higher of:
  - the sum of all app containers request/limit for a resource
  - the effective init request/limit for a resource
- Scheduling is done based on effective requests/limits, which means
  init containers can reserve resources for initialization that are not used
  during the life of the Pod.
- The QoS (quality of service) tier of the Pod's *effective QoS tier* is the
  QoS tier for init containers and app containers alike.

Quota and limits are applied based on the effective Pod request and
limit.

### Init containers and Linux cgroups

On Linux, resource allocations for Pod level control groups (cgroups) are based on the effective Pod
request and limit, the same as the scheduler.