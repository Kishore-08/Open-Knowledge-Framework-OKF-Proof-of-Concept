---
id: kubernetes-init-containers-0818d160
type: concept
title: Init Containers
description: 'This page provides an overview of init containers: specialized containers
  that run'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Init Containers

This page provides an overview of init containers: specialized containers that run
before app containers in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").
Init containers can contain utilities or setup scripts not present in an app image.

You can specify init containers in the Pod specification alongside the `containers`
array (which describes app containers).

In Kubernetes, a [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) is a container that
starts before the main application container and *continues to run*. This document is about init containers:
containers that run to completion during Pod initialization.