---
id: k8s-deployment
type: concept
title: Kubernetes Deployment
description: Declarative controller for managing stateless workload replicas
category: kubernetes
tags: [deployment, workload, controller, replicas, rollout]
source:
  name: Kubernetes Documentation
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: 2026-08-05
created_at: 2026-08-05
aliases: [Deployment, Deployments]
related: [k8s-replicaset, k8s-pod, k8s-service]
---

## Deployment

A Deployment provides declarative updates for Pods and ReplicaSets.

You describe a desired state in a Deployment, and the Deployment Controller changes
the actual state to the desired state at a controlled rate. You can define
Deployments to create new ReplicaSets, or to remove existing Deployments and adopt
all their resources with new Deployments.

## Use Cases

- Run a replica set of Pods (such as a stateless web tier).
- Roll out a change to the workload declaratively.
- Roll back to an earlier Deployment revision.
- Scale up or down the workload.
- Pause and resume a rollout.

## Creating a Deployment

The following is an example of a Deployment. It creates a ReplicaSet to bring up
three nginx Pods:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

In this example a `.spec.selector.matchLabels` pair with `app: nginx` must match
the labels in the Pod template.

## Updating a Deployment

A Deployment's rollout is triggered when its Pod template is changed, for example
when updating the container image. The Deployment creates a new ReplicaSet and
moves replicas gradually (maximum surge / unavailable controlled by
`.spec.strategy`).

## Rollback

Deployments keep revision history. `kubectl rollout undo deployment/nginx-deployment`
rolls back to the previous revision. The history is bounded by
`.spec.revisionHistoryLimit`.

## Scaling

`kubectl scale deployment nginx-deployment --replicas=5` changes the desired number
of replicas. Horizontal scaling can also be managed by a HorizontalPodAutoscaler.

## Pausing a Rollout

`kubectl rollout pause deployment/nginx-deployment` stops new changes from
triggering a rollout until you resume it with `kubectl rollout resume`.

## Deployment Status

A Deployment is considered available when it has the required number of available
replicas, all replicas are updated to the latest revision, and the rollout deadline
(`.spec.progressDeadlineSeconds`) has not been exceeded.
