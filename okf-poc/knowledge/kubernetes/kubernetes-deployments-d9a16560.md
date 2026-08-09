---
id: kubernetes-deployments-d9a16560
type: concept
title: Deployments
description: A Deployment manages a set of Pods to run an application workload, usually
  one that doesn't maintain state.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Deployments

A Deployment manages a set of Pods to run an application workload, usually one that doesn't maintain state.

A *Deployment* provides declarative updates for [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") and
[ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/ "ReplicaSet ensures that a specified number of Pod replicas are running at one time").

You describe a *desired state* in a Deployment, and the Deployment [Controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") changes the actual state to the desired state at a controlled rate. You can define Deployments to create new ReplicaSets, or to remove existing Deployments and adopt all their resources with new Deployments.

#### Note:

Do not manage ReplicaSets owned by a Deployment. Consider opening an issue in the main Kubernetes repository if your use case is not covered below.