---
id: k8s-pod
type: concept
title: Kubernetes Pod
description: The smallest deployable unit that holds one or more containers
category: kubernetes
tags: [pod, container, workload, scheduling, kubelet]
source:
  name: Kubernetes Documentation
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: 2026-08-05
created_at: 2026-08-05
aliases: [Pod, Pods]
related: [k8s-deployment, k8s-replicaset, k8s-service]
---

## Pod

A Pod is the smallest deployable unit of computing that you can create and manage
in Kubernetes. A Pod is a group of one or more containers, with shared storage and
network resources, and a specification for how to run the containers.

## Pods and Containers

Each Pod is meant to run a single instance of a given application. Each container
within a Pod shares:

- A unique cluster IP address
- Storage volumes
- A namespace for IPC (if enabled)
- Hostname and network interfaces

Containers in a Pod are scheduled to the same node and share lifecycle.

## Workload Resources

Pods are usually not created directly. Instead, you create them through a workload
resource such as a Deployment, StatefulSet, DaemonSet, or Job. These controllers
manage the lifecycle of Pods, including scaling, updates, and rescheduling.

## Pod Lifecycle

A Pod has a phase: `Pending`, `Running`, `Succeeded`, `Failed`, or `Unknown`.

- **Pending**: accepted but containers not yet running (image pull / scheduling).
- **Running**: at least one container is running.
- **Succeeded**: all containers terminated successfully.
- **Failed**: at least one container terminated with failure.
- **Unknown**: state could not be obtained (usually node communication failure).

The status also includes `containerStatuses` with each container's state
(`Waiting`, `Running`, `Terminated`) and its `restartCount`.

## Static Pods

Static Pods are managed directly by the kubelet on a specific node, without the
API server. The kubelet watches each static Pod and restarts it if it fails.

## Probes

Kubernetes can check containers with liveness, readiness, and startup probes so
the kubelet knows when to restart a container, when it is ready to accept traffic,
and when an application has started successfully.
