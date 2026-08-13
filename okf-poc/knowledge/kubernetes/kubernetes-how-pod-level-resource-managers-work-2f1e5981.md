---
id: kubernetes-how-pod-level-resource-managers-work-2f1e5981
type: concept
title: How pod-level resource managers work
description: The CPU and Memory resource managers operate differently depending on
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### How pod-level resource managers work

The CPU and Memory resource managers operate differently depending on the
configured Topology Manager scope.

#### Topology manager's pod scope and pod-level resources

When the Topology Manager scope is set to `pod`, the Kubelet performs a single
NUMA alignment for the entire pod based on the resource budget defined in
`.spec.resources`.

The resulting NUMA-aligned resource pool is then partitioned:

1. **Exclusive Slices:** Containers that specify `Guaranteed` resources
   (requests equal to limits for both CPU and memory, and the CPU request is a
   positive integer) are allocated exclusive slices from the pod's total
   allocation.
2. **Pod Shared Pool:** The remaining resources form a shared pool that is
   shared among all other containers in the pod that do not receive an
   exclusive allocation. While containers in this pool share resources with
   each other, they are strictly isolated from the exclusive slices and the
   general node-wide shared pool.

Note that when standard init containers run to completion, their resources are
added to a per-pod reusable set, rather than being returned to the node's
resource pool. Because they run sequentially, these resources are made reusable
for subsequent app containers (either for their own exclusive slices or for the
shared pool).

This allows you to co-locate containers that require exclusive resources (for
example: a high-performance primary application) with those that do not (for
example: sidecars for logging or monitoring), all within a single NUMA-aligned
pod.

Consider the containers in the following pod spec, where the Topology Manager
scope is `pod` and the pod has a total budget of 4 CPUs. `main-app` requests an
exclusive 2 CPU slice, while the sidecars share the remaining 2 CPUs in the
pod's shared pool:

[`pods/resource/pod-level-resource-managers-pod-scope-mixed.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/resource/pod-level-resource-managers-pod-scope-mixed.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/resource/pod-level-resource-managers-pod-scope-mixed.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: pod-scope-mixed
  annotations:
    kubernetes.io/description: "A pod demonstrating pod-level scope where one container gets exclusive resources and others share the remaining pod resources in a shared pool."
spec:
  # At Pod level, the Pod has CPU request equal to limits and memory request
  # also equal to memory limits. The main-app container meets the requirements
  # for the Guaranteed QoS class at container level, and the sidecar containers
  # don't specify any resource request. Under pod scope, this means that the
  # kubelet could statically assign 4 CPUs to the overall Pod, of which 2 are
  # assigned exclusively to the main-app container, and the remaining 2 are
  # shared by the sidecars in the pod's shared pool.
  resources:
    requests:
      cpu: "4"
      memory: "4Gi"
    limits:
      cpu: "4"
      memory: "4Gi"
  initContainers:
  - name: metrics-sidecar
    image: registry.example/example-image:v1
    restartPolicy: Always
  - name: logging-sidecar
    image: registry.example/example-image:v1
    restartPolicy: Always
  containers:
  - name: main-app
    image: registry.example/example-image:v1
    resources:
      requests:
        cpu: "2"
        memory: "2Gi"
      limits:
        cpu: "2"
        memory: "2Gi"
```

**Important considerations:**

When using pod-level resources with the Topology manager's pod scope, there are
some important considerations:

- **Empty shared pool restriction:** This configuration does not allow pod
  specifications that would produce an empty pod shared pool if there are
  containers that require one. If the sum of resource requests from all
  containers that are `Guaranteed` exactly equals the total resource budget,
  and there is at least one other container that requires a shared pool