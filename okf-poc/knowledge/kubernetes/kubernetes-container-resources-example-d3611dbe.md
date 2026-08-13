---
id: kubernetes-container-resources-example-d3611dbe
type: concept
title: Container resources example
description: The following Pod has two containers. Both containers are defined with
  a request for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Container resources example

The following Pod has two containers. Both containers are defined with a request for
0.25 CPU
and 64MiB (226 bytes) of memory. Each container has a limit of 0.5
CPU and 128MiB of memory. You can say the Pod has a request of 0.5 CPU and 128
MiB of memory, and a limit of 1 CPU and 256MiB of memory.

```
---
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```