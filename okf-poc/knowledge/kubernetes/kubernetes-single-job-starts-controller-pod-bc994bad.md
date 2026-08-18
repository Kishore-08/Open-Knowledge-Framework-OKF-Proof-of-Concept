---
id: kubernetes-single-job-starts-controller-pod-bc994bad
type: concept
title: Single Job starts controller Pod
description: Another pattern is for a single Job to create a Pod which then creates
  other Pods, acting as a sort
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Single Job starts controller Pod

Another pattern is for a single Job to create a Pod which then creates other Pods, acting as a sort
of custom controller for those Pods. This allows the most flexibility, but may be somewhat
complicated to get started with and offers less integration with Kubernetes.

An advantage of this approach is that the overall process gets the completion guarantee of a Job
object, but maintains complete control over what Pods are created and how work is assigned to them.