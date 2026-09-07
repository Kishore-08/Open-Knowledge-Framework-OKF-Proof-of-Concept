---
id: kubernetes-topology-manager-s-pod-scope-and-pod-level-resources-0cecd4eb
type: concept
title: Topology manager's pod scope and pod-level resources
description: When the Topology Manager scope is set to `pod`, the `kubelet` performs
  a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Topology manager's pod scope and pod-level resources

When the Topology Manager scope is set to `pod`, the `kubelet` performs a
single NUMA alignment for the entire Pod based on the resource budget defined
in `.spec.resources`.

The resulting NUMA-aligned resource pool is then partitioned:

1. **Exclusive slices:** Containers that specify `Guaranteed` resources
   (requests equal to limits for both CPU and memory, and the CPU request is
   a positive integer) receive exclusive slices from the Pod's total
   allocation.
2. **Pod shared pool:** The remaining resources form a shared pool for all
   other containers in the Pod that do not receive an exclusive allocation.
   While containers in this pool share resources with each other, they are
   strictly isolated from the exclusive slices and the general node-wide
   shared pool.

Note that when standard init containers run to completion, their resources
enter a per-Pod reusable set rather than returning to the Node's resource
pool. Because they run sequentially, subsequent app containers can reuse
these resources (either for their own exclusive slices or for the shared
pool).

This allows you to co-locate containers that require exclusive resources
(for example, a high-performance primary application) with those that do not
(for example, sidecars for logging or monitoring), all within a single
NUMA-aligned Pod.

Consider the containers in the following Pod spec, where the Topology Manager
scope is `pod` and the Pod has a total budget of 4 CPUs. `main-app` requests
an exclusive 2 CPU slice, while the sidecars share the remaining 2 CPUs in
the Pod's shared pool:

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
    # Note: This is a placeholder image for demonstration purposes, not an
    #actual metrics helper.
    image: registry.k8s.io/pause:3.9
    restartPolicy: Always
  - name: logging-sidecar
    # Note: This is a placeholder image for demonstration purposes, not an
    # actual logging agent.
    image: registry.k8s.io/pause:3.9
    restartPolicy: Always
  containers:
  - name: main-app
    # Note: This is a placeholder image for demonstration purposes.
    image: registry.k8s.io/pause:3.9
    resources:
      requests:
        cpu: "2"
        memory: "2Gi"
      limits:
        cpu: "2"
        memory: "2Gi"
```

**Important considerations:**

When using pod-level resources with the Topology manager's `pod` scope, there
are some important considerations:

- **Empty shared pool restriction:** This configuration does not allow Pod
  specifications that would produce an empty Pod shared pool if there are
  containers that require one. If the sum of resource requests from all
  containers that are `Guaranteed` exactly equals the total resource budget,
  and there is at