---
id: kubernetes-allocation-result-and-execution-e72e225b
type: concept
title: Allocation result and execution
description: When the Kubernetes scheduler allocates a device to a ResourceClaim,
  it copies
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Allocation result and execution

When the Kubernetes scheduler allocates a device to a ResourceClaim, it copies
the `skipNodeOperations` list from the ResourceSlice into the allocation
result:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
...
status:
  allocation:
    devices:
      results:
      - device: virtual-device-1
        driver: control-plane.example.com
        pool: central-pool
        skipNodeOperations:
        - "*"
```

When a Pod runs on a node, the `kubelet` reads the allocation results. If all
allocated devices for a given driver within a ResourceClaim skip a specific
operation, the `kubelet` completely bypasses calling that gRPC hook for that
driver.