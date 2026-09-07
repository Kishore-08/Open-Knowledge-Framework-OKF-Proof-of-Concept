---
id: kubernetes-replication-controller-bc994bad
type: concept
title: Replication Controller
description: Jobs are complementary to [Replication Controllers](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/).
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Replication Controller

Jobs are complementary to [Replication Controllers](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/).
A Replication Controller manages Pods which are not expected to terminate (e.g. web servers), and a Job
manages Pods that are expected to terminate (e.g. batch tasks).

As discussed in [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/), `Job` is *only* appropriate
for pods with `RestartPolicy` equal to `OnFailure` or `Never`.

#### Note:

If `RestartPolicy` is not set, the default value is `Always`.