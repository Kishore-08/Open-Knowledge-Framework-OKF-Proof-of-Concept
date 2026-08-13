---
id: kubernetes-namespaces-0663647e
type: concept
title: Namespaces
description: In Kubernetes, *namespaces* provide a mechanism for isolating groups
  of resources within a single cluster. Names of resources need to be unique within
  a namespace, but not across namespaces. Namespace
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# Namespaces

In Kubernetes, *namespaces* provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") *(e.g. Deployments, Services, etc.)* and not for cluster-wide objects *(e.g. StorageClass, Nodes, PersistentVolumes, etc.)*.