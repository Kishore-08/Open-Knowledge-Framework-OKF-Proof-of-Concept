---
id: kubernetes-requesting-dra-devices-for-a-podgroup-0cf588b5
type: concept
title: Requesting DRA devices for a PodGroup
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Requesting DRA devices for a PodGroup

FEATURE STATE:
`Kubernetes v1.36 [alpha]`(disabled by default)

[Devices](https://kubernetes.io/docs/reference/glossary/?all=true#term-device "Any resource that's directly or indirectly attached your cluster's nodes, like GPUs or circuit boards.") available through
[Dynamic Resource Allocation (DRA)](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/ "A Kubernetes feature for requesting and sharing resources, like hardware accelerators, among Pods.")
can be requested by a PodGroup through its `spec.resourceClaims` field:

```
apiVersion: scheduling.k8s.io/v1alpha2
kind: PodGroup
metadata:
  name: training-group
  namespace: some-ns
spec:
  ...
  resourceClaims:
  - name: pg-claim
    resourceClaimName: my-pg-claim
  - name: pg-claim-template
    resourceClaimTemplateName: my-pg-template
```

[ResourceClaims](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Describes the resources that a workload needs, such as devices. ResourceClaims can request devices from DeviceClasses.")
associated with PodGroups can be shared by all Pods belonging to the group. With
only a reference to the PodGroup in the ResourceClaim's `status.reservedFor`
instead of each individual Pod, any number of Pods in the same PodGroup can
share a ResourceClaim. ResourceClaims can also be generated from
[ResourceClaimTemplates](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#resourceclaims-templates "Defines a template for Kubernetes to create ResourceClaims. Used to provide per-Pod or per-PodGroup access to separate, similar resources.")
for each PodGroup, allowing the devices allocated to each generated
ResourceClaim to be shared by the Pods in each PodGroup.

For more details and a more complete example, see the
[DRA documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#workload-resource-claims).