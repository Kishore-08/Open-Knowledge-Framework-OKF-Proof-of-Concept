---
id: kubernetes-get-grpc-endpoint-3614a558
type: concept
title: '`Get` gRPC endpoint'
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### `Get` gRPC endpoint

FEATURE STATE:
`Kubernetes v1.34 [beta]`

The `Get` endpoint provides information on resources of a running Pod. It exposes information
similar to those described in the `List` endpoint. The `Get` endpoint requires `PodName`
and `PodNamespace` of the running Pod.

```
// GetPodResourcesRequest contains information about the pod
message GetPodResourcesRequest {
    string pod_name = 1;
    string pod_namespace = 2;
}
```

The `Get` endpoint can provide Pod information related to dynamic resources
allocated by the dynamic resource allocation API.
Starting from Kubernetes v1.34, this feature is enabled by default.