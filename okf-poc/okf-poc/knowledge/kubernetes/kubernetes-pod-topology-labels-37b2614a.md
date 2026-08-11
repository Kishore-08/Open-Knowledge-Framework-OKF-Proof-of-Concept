---
id: kubernetes-pod-topology-labels-37b2614a
type: concept
title: Pod topology labels
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod topology labels

FEATURE STATE:
`Kubernetes v1.35 [beta]`(enabled by default)

Pods inherit the topology labels (`topology.kubernetes.io/zone` and `topology.kubernetes.io/region`) from their assigned Node if those labels are present. These labels can then be utilized via the Downward API to provide the workload with node topology awareness.

Here is an example of a Pod using downward API for it's zone and region:

```
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-topology-labels
spec:
  containers:
    - name: app
      image: alpine
      command: ["sh", "-c", "env"]
      env:
        - name: MY_ZONE
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['topology.kubernetes.io/zone']
        - name: MY_REGION
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['topology.kubernetes.io/region']
```