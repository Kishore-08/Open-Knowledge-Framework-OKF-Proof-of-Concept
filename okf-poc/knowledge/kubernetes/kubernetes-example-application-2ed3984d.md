---
id: kubernetes-example-application-2ed3984d
type: concept
title: Example application
description: 'Here''s an example of a Deployment with two containers, one of which
  is a sidecar:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Example application

Here's an example of a Deployment with two containers, one of which is a sidecar:

#### Note:

In this example, the sidecar container is intentionally defined under `initContainers`
with `restartPolicy: Always`. Kubernetes treats such containers as sidecars that continue
running for the lifetime of the Pod.

[`application/deployment-sidecar.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/application/deployment-sidecar.yaml)![](https://kubernetes.io/images/copycode.svg "Copy application/deployment-sidecar.yaml to clipboard")

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: alpine:latest
          command: ['sh', '-c', 'while true; do echo "logging" >> /opt/logs.txt; sleep 1; done']
          volumeMounts:
            - name: data
              mountPath: /opt
      initContainers:
        - name: logshipper
          image: alpine:latest
          # Setting restartPolicy: Always makes this a sidecar container.
          restartPolicy: Always
          command: ['sh', '-c', 'tail -F /opt/logs.txt']
          volumeMounts:
            - name: data
              mountPath: /opt
      volumes:
        - name: data
          emptyDir: {}
```