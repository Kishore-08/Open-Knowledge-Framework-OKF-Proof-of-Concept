---
id: kubernetes-replicaset-375b8ad3
type: concept
title: ReplicaSet
description: A ReplicaSet's purpose is to maintain a stable set of replica Pods running
  at any given time. Usually, you define a Deployment and let that Deployment manage
  ReplicaSets automatically.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# ReplicaSet

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. Usually, you define a Deployment and let that Deployment manage ReplicaSets automatically.

A ReplicaSet's purpose is to maintain a stable set of replica Pods running at any given time. As such, it is often
used to guarantee the availability of a specified number of identical Pods.