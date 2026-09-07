---
id: kubernetes-resource-claims-497d3b3e
type: concept
title: Resource claims
description: The resource claims block expresses which
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Resource claims

The resource claims block expresses which
[dynamic resource allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/)
claims are shared by every Pod in the group rather than allocated per Pod. Each entry names
the claim within the group and points at either an existing
[ResourceClaim](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Describes the resources that a workload needs, such as devices. ResourceClaims can request devices from DeviceClasses.") or a
[ResourceClaimTemplate](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Defines a template for Kubernetes to create ResourceClaims. Used to provide per-Pod or per-PodGroup access to separate, similar resources.")
from which one is generated. A group may declare at most four claims.

Pods consume the devices allocated to the group by declaring a matching claim in their own
spec, using the same name and referring to the same object.