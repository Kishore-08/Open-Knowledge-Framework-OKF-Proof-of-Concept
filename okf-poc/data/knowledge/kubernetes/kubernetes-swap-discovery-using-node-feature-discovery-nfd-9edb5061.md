---
id: kubernetes-swap-discovery-using-node-feature-discovery-nfd-9edb5061
type: concept
title: Swap discovery using Node Feature Discovery (NFD)
description: '[Node Feature Discovery](https://github.com/kubernetes-sigs/node-feature-discovery)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Swap discovery using Node Feature Discovery (NFD)

[Node Feature Discovery](https://github.com/kubernetes-sigs/node-feature-discovery)
is a Kubernetes addon for detecting hardware features and configuration.
It can be utilized to discover which nodes are provisioned with swap.

As an example, to figure out which nodes are provisioned with swap,
use the following command:

```
kubectl get nodes -o jsonpath='{range .items[?(@.metadata.labels.feature\.node\.kubernetes\.io/memory-swap)]}{.metadata.name}{"\t"}{.metadata.labels.feature\.node\.kubernetes\.io/memory-swap}{"\n"}{end}'
```

This will result in an output similar to:

```
k8s-worker1: true
k8s-worker2: true
k8s-worker3: false
```

In this example, swap is provisioned on nodes `k8s-worker1` and `k8s-worker2`, but not on `k8s-worker3`.