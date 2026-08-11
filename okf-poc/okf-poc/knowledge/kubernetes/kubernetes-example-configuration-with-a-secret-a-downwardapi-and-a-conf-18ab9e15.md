---
id: kubernetes-example-configuration-with-a-secret-a-downwardapi-and-a-conf-18ab9e15
type: concept
title: Example configuration with a secret, a downwardAPI, and a configMap
description: '[`pods/storage/projected-secret-downwardapi-configmap.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/storage/projected-secret-downwardapi-configmap.yaml)![]('
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Example configuration with a secret, a downwardAPI, and a configMap

[`pods/storage/projected-secret-downwardapi-configmap.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/storage/projected-secret-downwardapi-configmap.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/storage/projected-secret-downwardapi-configmap.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: volume-test
spec:
  containers:
  - name: container-test
    image: busybox:1.28
    command: ["sleep", "3600"]
    volumeMounts:
    - name: all-in-one
      mountPath: "/projected-volume"
      readOnly: true
  volumes:
  - name: all-in-one
    projected:
      sources:
      - secret:
          name: mysecret
          items:
          - key: username
            path: my-group/my-username
      - downwardAPI:
          items:
          - path: "labels"
            fieldRef:
              fieldPath: metadata.labels
          - path: "cpu_limit"
            resourceFieldRef:
              containerName: container-test
              resource: limits.cpu
      - configMap:
          name: myconfigmap
          items:
          - key: config
            path: my-group/my-config
```