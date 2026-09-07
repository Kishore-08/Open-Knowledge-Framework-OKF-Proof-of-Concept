---
id: kubernetes-pod-resources-example-d3611dbe
type: concept
title: Pod resources example
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Pod resources example

FEATURE STATE:
`Kubernetes v1.34 [beta]`(enabled by default)

This feature can be enabled by setting the `PodLevelResources`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/).
The following Pod has an explicit request of 1 CPU and 100 MiB of memory, and an
explicit limit of 1 CPU and 200 MiB of memory. The `pod-resources-demo-ctr-1`
container has explicit requests and limits set. However, the
`pod-resources-demo-ctr-2` container will simply share the resources available
within the Pod resource boundaries, as it does not have explicit requests and limits
set.

[`pods/resource/pod-level-resources.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/resource/pod-level-resources.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/resource/pod-level-resources.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: pod-resources-demo
  namespace: pod-resources-example
spec:
  resources:
    limits:
      cpu: "1"
      memory: "200Mi"
    requests:
      cpu: "1"
      memory: "100Mi"
  containers:
  - name: pod-resources-demo-ctr-1
    image: nginx
    resources:
      limits:
        cpu: "0.5"
        memory: "100Mi"
      requests:
        cpu: "0.5"
        memory: "50Mi"
  - name: pod-resources-demo-ctr-2
    image: fedora
    command:
    - sleep
    - inf
```