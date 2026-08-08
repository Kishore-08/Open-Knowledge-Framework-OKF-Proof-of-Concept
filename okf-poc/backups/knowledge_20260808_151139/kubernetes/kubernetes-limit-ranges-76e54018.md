---
id: kubernetes-limit-ranges-76e54018
type: concept
title: Limit Ranges
description: By default, containers run with unbounded
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/limit-range/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Limit Ranges

By default, containers run with unbounded
[compute resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) on a Kubernetes cluster.
Using Kubernetes [resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/),
administrators (also termed *cluster operators*) can restrict consumption and creation
of cluster resources (such as CPU time, memory, and persistent storage) within a specified
[namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.").
Within a namespace, a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") can consume as much CPU and memory as is allowed by the ResourceQuotas that apply to that namespace.
As a cluster operator, or as a namespace-level administrator, you might also be concerned
about making sure that a single object cannot monopolize all available resources within a namespace.

A LimitRange is a policy to constrain the resource allocations (limits and requests) that you can specify for
each applicable object kind (such as Pod or [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container.")) in a namespace.

A *LimitRange* provides constraints that can:

- Enforce minimum and maximum compute resources usage per Pod or Container in a namespace.
- Enforce minimum and maximum storage request per
  [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims "Claims storage resources defined in a PersistentVolume so that it can be mounted as a volume in a container.") in a namespace.
- Enforce a ratio between request and limit for a resource in a namespace.
- Set default request/limit for compute resources in a namespace and automatically
  inject them to Containers at runtime.

Kubernetes constrains resource allocations to Pods in a particular namespace
whenever there is at least one LimitRange object in that namespace.

The name of a LimitRange object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).