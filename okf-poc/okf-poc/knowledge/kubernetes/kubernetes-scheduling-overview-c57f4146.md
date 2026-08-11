---
id: kubernetes-scheduling-overview-c57f4146
type: concept
title: Scheduling overview
description: A scheduler watches for newly created Pods that have no Node assigned.
  For
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Scheduling overview

A scheduler watches for newly created Pods that have no Node assigned. For
every Pod that the scheduler discovers, the scheduler becomes responsible
for finding the best Node for that Pod to run on. The scheduler reaches
this placement decision taking into account the scheduling principles
described below.

If you want to understand why Pods are placed onto a particular Node,
or if you're planning to implement a custom scheduler yourself, this
page will help you learn about scheduling.