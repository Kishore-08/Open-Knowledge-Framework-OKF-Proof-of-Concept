---
id: kubernetes-using-kubectl-top-show-swap-9edb5061
type: concept
title: Using `kubectl top --show-swap`
description: Querying metrics is valuable, but somewhat cumbersome, as these metrics
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Using `kubectl top --show-swap`

Querying metrics is valuable, but somewhat cumbersome, as these metrics
are designed to be used by software rather than humans.
In order to consume this data in a more user-friendly way,
the `kubectl top` command has been extended to support swap metrics, using the `--show-swap` flag.

In order to receive information about swap usage on nodes, `kubectl top nodes --show-swap` can be used:

```
kubectl top nodes --show-swap
```

This will result in an output similar to:

```
NAME    CPU(cores)   CPU(%)   MEMORY(bytes)   MEMORY(%)   SWAP(bytes)    SWAP(%)       
node1   1m           10%      2Mi             10%         1Mi            0%   
node2   5m           10%      6Mi             10%         2Mi            0%   
node3   3m           10%      4Mi             10%         <unknown>      <unknown>
```

In order to receive information about swap usage by pods, `kubectl top pods --show-swap` can be used:

```
kubectl top pod -n kube-system --show-swap
```

This will result in an output similar to:

```
NAME                                      CPU(cores)   MEMORY(bytes)   SWAP(bytes)
coredns-58d5bc5cdb-5nbk4                  2m           19Mi            0Mi
coredns-58d5bc5cdb-jsh26                  3m           37Mi            0Mi
etcd-node01                               51m          143Mi           5Mi
kube-apiserver-node01                     98m          824Mi           16Mi
kube-controller-manager-node01            20m          135Mi           9Mi
kube-proxy-ffgs2                          1m           24Mi            0Mi
kube-proxy-fhvwx                          1m           39Mi            0Mi
kube-scheduler-node01                     13m          69Mi            0Mi
metrics-server-8598789fdb-d2kcj           5m           26Mi            0Mi
```