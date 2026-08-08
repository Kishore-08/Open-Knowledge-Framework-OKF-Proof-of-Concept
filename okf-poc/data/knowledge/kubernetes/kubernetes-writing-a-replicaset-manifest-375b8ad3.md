---
id: kubernetes-writing-a-replicaset-manifest-375b8ad3
type: concept
title: Writing a ReplicaSet manifest
description: As with all other Kubernetes API objects, a ReplicaSet needs the `apiVersion`,
  `kind`, and `metadata` fields.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Writing a ReplicaSet manifest

As with all other Kubernetes API objects, a ReplicaSet needs the `apiVersion`, `kind`, and `metadata` fields.
For ReplicaSets, the `kind` is always a ReplicaSet.

When the control plane creates new Pods for a ReplicaSet, the `.metadata.name` of the
ReplicaSet is part of the basis for naming those Pods. The name of a ReplicaSet must be a valid
[DNS subdomain](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names)
value, but this can produce unexpected results for the Pod hostnames. For best compatibility,
the name should follow the more restrictive rules for a
[DNS label](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).

A ReplicaSet also needs a [`.spec` section](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).