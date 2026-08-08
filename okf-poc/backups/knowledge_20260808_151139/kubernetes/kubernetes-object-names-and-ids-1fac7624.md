---
id: kubernetes-object-names-and-ids-1fac7624
type: concept
title: Object Names and IDs
description: Each [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects
  "An entity in the Kubernetes system, representing part of the state of your cluster.")
  in your clust
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Object Names and IDs

Each [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") in your cluster has a [*Name*](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names) that is unique for that type of resource.
Every Kubernetes object also has a [*UID*](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids) that is unique across your whole cluster.

For example, you can only have one Pod named `myapp-1234` within the same [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/), but you can have one Pod and one Deployment that are each named `myapp-1234`.

For non-unique user-provided attributes, Kubernetes provides [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).