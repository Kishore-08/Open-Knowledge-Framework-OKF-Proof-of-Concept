---
id: kubernetes-pods-6ed556c1
type: concept
title: Pods
description: '*Pods* are the smallest deployable units of computing that you can create
  and manage in Kubernetes.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Pods

*Pods* are the smallest deployable units of computing that you can create and manage in Kubernetes.

A *Pod* (as in a pod of whales or pea pod) is a group of one or more
[containers](https://kubernetes.io/docs/concepts/containers/ "A lightweight and portable executable image that contains software and all of its dependencies."), with shared storage and network resources, and a specification for how to run the containers. A Pod's contents are always co-located and
co-scheduled, and run in a shared context. A Pod models an
application-specific "logical host": it contains one or more application
containers which are relatively tightly coupled.
In non-cloud contexts, applications executed on the same physical or virtual machine are analogous to cloud applications executed on the same logical host.

As well as application containers, a Pod can contain
[init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ "One or more initialization containers that must run to completion before any app containers run.") that run
during Pod startup. You can also inject
[ephemeral containers](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/ "A type of container type that you can temporarily run inside a Pod")
for debugging a running Pod.