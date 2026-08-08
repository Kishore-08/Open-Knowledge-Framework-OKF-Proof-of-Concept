---
id: kubernetes-using-subpath-with-expanded-environment-variables-4142258a
type: concept
title: Using subPath with expanded environment variables
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Using subPath with expanded environment variables

FEATURE STATE:
`Kubernetes v1.17 [stable]`

Use the `subPathExpr` field to construct `subPath` directory names from
downward API environment variables.
The `subPath` and `subPathExpr` properties are mutually exclusive.

In this example, a `Pod` uses `subPathExpr` to create a directory `pod1` within
the `hostPath` volume `/var/log/pods`.
The `hostPath` volume takes the `Pod` name from the `downwardAPI`.
The host directory `/var/log/pods/pod1` is mounted at `/logs` in the container.

```
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  containers:
  - name: container1
    env:
    - name: POD_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.name
    image: busybox:1.28
    command: [ "sh", "-c", "while [ true ]; do echo 'Hello'; sleep 10; done | tee -a /logs/hello.txt" ]
    volumeMounts:
    - name: workdir1
      mountPath: /logs
      # The variable expansion uses round brackets (not curly brackets).
      subPathExpr: $(POD_NAME)
  restartPolicy: Never
  volumes:
  - name: workdir1
    hostPath:
      path: /var/log/pods
```