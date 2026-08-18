---
id: kubernetes-usage-3540e4aa
type: concept
title: Usage
description: Once RuntimeClasses are configured for the cluster, you can specify a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/runtime-class/
updated_at: '2026-08-18'
created_at: '2026-08-18'
---

## Usage

Once RuntimeClasses are configured for the cluster, you can specify a
`runtimeClassName` in the Pod spec to use it. For example:

```
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  runtimeClassName: myclass
  # ...
```

This will instruct the kubelet to use the named RuntimeClass to run this pod. If the named
RuntimeClass does not exist, or the CRI cannot run the corresponding handler, the pod will enter the
`Failed` terminal [phase](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase). Look for a
corresponding [event](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/) for an
error message.

If no `runtimeClassName` is specified, the default RuntimeHandler will be used, which is equivalent
to the behavior when the RuntimeClass feature is disabled.