---
id: kubernetes-design-8c98aece
type: concept
title: Design
description: The cloud controller manager runs in the control plane as a replicated
  set of processes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Design

The cloud controller manager runs in the control plane as a replicated set of processes
(usually, these are containers in Pods). Each cloud-controller-manager implements
multiple [controllers](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") in a single
process.

#### Note:

You can also run the cloud controller manager as a Kubernetes
[addon](https://kubernetes.io/docs/concepts/cluster-administration/addons/ "Resources that extend the functionality of Kubernetes.") rather than as part
of the control plane.

## Cloud controller manager functions

The controllers inside the cloud controller manager include: