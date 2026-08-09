---
id: kubernetes-monitoring-device-plugin-resources-3614a558
type: concept
title: Monitoring device plugin resources
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Monitoring device plugin resources

FEATURE STATE:
`Kubernetes v1.28 [stable]`

In order to monitor resources provided by device plugins, monitoring agents need to be able to
discover the set of devices that are in-use on the node and obtain metadata to describe which
container the metric should be associated with. [Prometheus](https://prometheus.io/) metrics
exposed by device monitoring agents should follow the
[Kubernetes Instrumentation Guidelines](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-instrumentation/metric-instrumentation.md),
identifying containers using `pod`, `namespace`, and `container` prometheus labels.

The kubelet provides a gRPC service to enable discovery of in-use devices, and to provide metadata
for these devices:

```
// PodResourcesLister is a service provided by the kubelet that provides information about the
// node resources consumed by pods and containers on the node
service PodResourcesLister {
    rpc List(ListPodResourcesRequest) returns (ListPodResourcesResponse) {}
    rpc GetAllocatableResources(AllocatableResourcesRequest) returns (AllocatableResourcesResponse) {}
    rpc Get(GetPodResourcesRequest) returns (GetPodResourcesResponse) {}
}
```