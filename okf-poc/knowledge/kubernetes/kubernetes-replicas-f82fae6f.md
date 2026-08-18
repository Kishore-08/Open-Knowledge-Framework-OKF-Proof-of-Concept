---
id: kubernetes-replicas-f82fae6f
type: concept
title: Replicas
description: '`.spec.replicas` is an optional field that specifies the number of desired
  Pods. It defaults to 1.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Replicas

`.spec.replicas` is an optional field that specifies the number of desired Pods. It defaults to 1.

Should you manually scale a StatefulSet, via `kubectl scale statefulset statefulset --replicas=X`, and then you update that StatefulSet
based on a manifest (for example: by running `kubectl apply -f statefulset.yaml`), then applying that manifest overwrites the manual scaling
that you previously did.

If a [HorizontalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
(or any similar API for horizontal scaling) is managing scaling for a
Statefulset, don't set `.spec.replicas`. Instead, allow the Kubernetes
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") to manage
the `.spec.replicas` field automatically.