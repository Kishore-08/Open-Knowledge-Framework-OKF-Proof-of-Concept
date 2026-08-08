---
id: kubernetes-service-fb91f326
type: concept
title: Service
description: Expose an application running in your cluster behind a single outward-facing
  endpoint, even when the workload is split across multiple backends.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Service

Expose an application running in your cluster behind a single outward-facing endpoint, even when the workload is split across multiple backends.

In Kubernetes, a Service is a method for exposing a network application that is running as one or more
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") in your cluster.

A key aim of Services in Kubernetes is that you don't need to modify your existing
application to use an unfamiliar service discovery mechanism.
You can run code in Pods, whether this is a code designed for a cloud-native world, or
an older app you've containerized. You use a Service to make that set of Pods available
on the network so that clients can interact with it.

If you use a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster.") to run your app,
that Deployment can create and destroy Pods dynamically. From one moment to the next,
you don't know how many of those Pods are working and healthy; you might not even know
what those healthy Pods are named.
Kubernetes [Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") are created and destroyed
to match the desired state of your cluster. Pods are ephemeral resources (you should not
expect that an individual Pod is reliable and durable).

Each Pod gets its own IP address (Kubernetes expects network plugins to ensure this).
For a given Deployment in your cluster, the set of Pods running in one moment in
time could be different from the set of Pods running that application a moment later.

This leads to a problem: if some set of Pods (call them "backends") provides
functionality to other Pods (call them "frontends") inside your cluster,
how do the frontends find out and keep track of which IP address to connect
to, so that the frontend can use the backend part of the workload?

Enter *Services*.