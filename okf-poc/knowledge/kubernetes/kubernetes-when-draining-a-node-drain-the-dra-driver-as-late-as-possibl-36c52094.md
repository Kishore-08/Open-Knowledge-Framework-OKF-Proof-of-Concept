---
id: kubernetes-when-draining-a-node-drain-the-dra-driver-as-late-as-possibl-36c52094
type: concept
title: When draining a node, drain the DRA driver as late as possible
description: The DRA driver is responsible for unpreparing any devices that were allocated
  to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### When draining a node, drain the DRA driver as late as possible

The DRA driver is responsible for unpreparing any devices that were allocated to
Pods, and if the DRA driver is [drained](https://kubernetes.io/docs/reference/glossary/?all=true#term-drain "Safely evicts Pods from a Node to prepare for maintenance or removal.") before Pods with claims have been deleted, it will not be
able to finalize its cleanup. If you implement custom drain logic for nodes,
consider checking that there are no allocated/reserved ResourceClaim or
ResourceClaimTemplates before terminating the DRA driver itself.