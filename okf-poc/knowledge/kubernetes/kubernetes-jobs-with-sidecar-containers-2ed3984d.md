---
id: kubernetes-jobs-with-sidecar-containers-2ed3984d
type: concept
title: Jobs with sidecar containers
description: If you define a Job that uses sidecar using Kubernetes-style init containers,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Jobs with sidecar containers

If you define a Job that uses sidecar using Kubernetes-style init containers,
the sidecar container in each Pod does not prevent the Job from completing after the
main container has finished.

Here's an example of a Job with two containers, one of which is a sidecar:

[`application/job/job-sidecar.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/application/job/job-sidecar.yaml)![](https://kubernetes.io/images/copycode.svg "Copy application/job/job-sidecar.yaml to clipboard")

```
apiVersion: batch/v1
kind: Job
metadata:
  name: myjob
spec:
  template:
    spec:
      containers:
        - name: myjob
          image: alpine:latest
          command: ['sh', '-c', 'echo "logging" > /opt/logs.txt']
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
      restartPolicy: Never
      volumes:
        - name: data
          emptyDir: {}
```