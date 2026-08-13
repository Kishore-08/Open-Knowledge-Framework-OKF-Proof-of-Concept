---
id: kubernetes-consistency-4f7e995f
type: concept
title: Consistency
description: You should set the same Pod topology spread constraints on all pods in
  a group.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Consistency

You should set the same Pod topology spread constraints on all pods in a group.

Usually, if you are using a workload controller such as a Deployment, the pod template
takes care of this for you. If you mix different spread constraints then Kubernetes
follows the API definition of the field; however, the behavior is more likely to become
confusing and troubleshooting is less straightforward.

You need a mechanism to ensure that all the nodes in a topology domain (such as a
cloud provider region) are labeled consistently.
To avoid you needing to manually label nodes, most clusters automatically
populate well-known labels such as `kubernetes.io/hostname`. Check whether
your cluster supports this.

## Topology spread constraint examples