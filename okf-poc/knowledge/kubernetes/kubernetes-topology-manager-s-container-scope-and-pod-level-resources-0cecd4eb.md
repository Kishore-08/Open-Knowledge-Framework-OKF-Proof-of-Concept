---
id: kubernetes-topology-manager-s-container-scope-and-pod-level-resources-0cecd4eb
type: concept
title: Topology manager's container scope and pod-level resources
description: When the Topology Manager scope is set to `container`, the `kubelet`
  evaluates
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Topology manager's container scope and pod-level resources

When the Topology Manager scope is set to `container`, the `kubelet` evaluates
each container individually for exclusive allocation.

If the overall Pod achieves a `Guaranteed`
[QoS class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/ "QoS Class (Quality of Service Class) provides a way for Kubernetes to classify pods within the cluster into several classes and make decisions about scheduling and eviction.") (by specifying
appropriate values in the Pod-level `.spec.resources`), you can mix and match
containers:

- Containers with their own `Guaranteed` requests receive exclusive
  NUMA-aligned resources.
- Other containers in the Pod that do not specify `Guaranteed` requests
  run in the Node's shared pool.
- The collective resource consumption of all containers is still enforced
  by the Pod's `.spec.resources` limits.

This scope is useful when you have an infrastructure sidecar that needs to
be aligned to a specific NUMA Node for device access, while the main
workload can run in the general Node shared pool.

Consider the containers in the following Pod spec, where the Topology
Manager scope is `container` and the Pod represents a workload with an
infrastructure sidecar and two application workers, with a total budget of
4 CPUs. The `infrastructure-sidecar` gets an exclusive, NUMA-aligned 2 CPU
slice. The two application workers (`worker-1` and `worker-2`) run in the
general, node-wide shared pool:

[`pods/resource/pod-level-resource-managers-container-scope-mixed.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/resource/pod-level-resource-managers-container-scope-mixed.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/resource/pod-level-resource-managers-container-scope-mixed.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: container-scope-mixed
  annotations:
    kubernetes.io/description: "A pod demonstrating container-level scope where one container gets exclusive resources and others run in the node's shared pool."
spec:
  # At Pod level, the Pod has CPU request equal to limits and memory request
  # also equal to memory limits. The infrastructure-sidecar container meets the
  # requirements for the Guaranteed QoS class at container level, and the worker
  # containers don't specify any resource request. Under container scope, the
  # kubelet evaluates containers individually for exclusive allocation. This
  # means the infrastructure-sidecar gets an exclusive 2 CPU slice, while the
  # worker containers run in the node's general shared pool, all while bounded
  # by the overall pod limits.
  resources:
    requests:
      cpu: "4"
      memory: "4Gi"
    limits:
      cpu: "4"
      memory: "4Gi"
  initContainers:
  - name: infrastructure-sidecar
    # Note: This is a placeholder image for demonstration purposes, not an
    # actual infrastructure helper.
    image: registry.k8s.io/pause:3.9
    restartPolicy: Always
    resources:
      requests:
        cpu: "2"
        memory: "2Gi"
      limits:
        cpu: "2"
        memory: "2Gi"
  containers:
  - name: worker-1
    # Note: This is a placeholder image for demonstration purposes.
    image: registry.k8s.io/pause:3.9
  - name: worker-2
    # Note: This is a placeholder image for demonstration purposes.
    image: registry.k8s.io/pause:3.9
```