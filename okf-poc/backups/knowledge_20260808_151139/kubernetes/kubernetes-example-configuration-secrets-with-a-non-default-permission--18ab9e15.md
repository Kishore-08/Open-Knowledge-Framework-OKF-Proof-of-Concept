---
id: kubernetes-example-configuration-secrets-with-a-non-default-permission--18ab9e15
type: concept
title: 'Example configuration: secrets with a non-default permission mode set'
description: '[`pods/storage/projected-secrets-nondefault-permission-mode.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/storage/projected-secrets-nondefault-permission-mo'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Example configuration: secrets with a non-default permission mode set

[`pods/storage/projected-secrets-nondefault-permission-mode.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/storage/projected-secrets-nondefault-permission-mode.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/storage/projected-secrets-nondefault-permission-mode.yaml to clipboard")

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
      - secret:
          name: mysecret2
          items:
          - key: password
            path: my-group/my-password
            mode: 0777
```

Each projected volume source is listed in the spec under `sources`. The
parameters are nearly the same with two exceptions:

- For secrets, the `secretName` field has been changed to `name` to be consistent
  with ConfigMap naming.
- The `defaultMode` can only be specified at the projected level and not for each
  volume source. However, as illustrated above, you can explicitly set the `mode`
  for each individual projection.