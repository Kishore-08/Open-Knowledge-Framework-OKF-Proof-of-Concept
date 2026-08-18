---
id: kubernetes-horizontal-pod-autoscaling-cdcbb833
type: concept
title: Horizontal Pod Autoscaling
description: In Kubernetes, a *HorizontalPodAutoscaler* automatically updates a workload
  resource (such as
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Horizontal Pod Autoscaling

In Kubernetes, a *HorizontalPodAutoscaler* automatically updates a workload resource (such as
a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.") or
[StatefulSet](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ "A StatefulSet manages deployment and scaling of a set of Pods, with durable storage and persistent identifiers for each Pod.")), with the
aim of automatically scaling capacity to match demand.

Horizontal scaling means that the response to increased load is to deploy more
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").
This is different from *vertical* scaling, which for Kubernetes would mean
assigning more resources (for example: memory or CPU) to the Pods that are already
running for the workload.

If the load decreases, and the number of Pods is above the configured minimum,
the HorizontalPodAutoscaler instructs the workload resource (the Deployment, StatefulSet,
or other similar resource) to scale back down.

Horizontal pod autoscaling does not apply to objects that can't be scaled (for example:
a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset "Ensures a copy of a Pod is running across a set of nodes in a cluster.").)

The HorizontalPodAutoscaler is implemented as a Kubernetes API resource and a
[controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.").
The resource determines the behavior of the controller.
The horizontal pod autoscaling controller, running within the Kubernetes
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers."), periodically adjusts the
desired scale of its target (for example, a Deployment) to match observed metrics such as average
CPU utilization, average memory utilization, or any other custom metric you specify.

There is [walkthrough example](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/) of using
horizontal pod autoscaling.