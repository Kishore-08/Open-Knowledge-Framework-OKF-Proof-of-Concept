---
id: kubernetes-understanding-kubernetes-objects-65511bde
type: concept
title: Understanding Kubernetes objects
description: '*Kubernetes objects* are persistent entities in the Kubernetes system.
  Kubernetes uses these'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Understanding Kubernetes objects

*Kubernetes objects* are persistent entities in the Kubernetes system. Kubernetes uses these
entities to represent the state of your cluster. Specifically, they can describe:

- What containerized applications are running (and on which nodes)
- The resources available to those applications
- The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance

A Kubernetes object is a "record of intent"--once you create the object, the Kubernetes system
will constantly work to ensure that the object exists. By creating an object, you're effectively
telling the Kubernetes system what you want your cluster's workload to look like; this is your
cluster's *desired state*.

To work with Kubernetes objects—whether to create, modify, or delete them—you'll need to use the
[Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/). When you use the `kubectl` command-line
interface, for example, the CLI makes the necessary Kubernetes API calls for you. You can also use
the Kubernetes API directly in your own programs using one of the
[Client Libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/).