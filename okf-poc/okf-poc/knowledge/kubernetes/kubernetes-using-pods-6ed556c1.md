---
id: kubernetes-using-pods-6ed556c1
type: concept
title: Using Pods
description: The following is an example of a Pod which consists of a container running
  the image `nginx:1.14.2`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Using Pods

The following is an example of a Pod which consists of a container running the image `nginx:1.14.2`.

[`pods/simple-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/simple-pod.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/simple-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```

To create the Pod shown above, run the following command:

```
kubectl apply -f https://k8s.io/examples/pods/simple-pod.yaml
```

Pods are generally not created directly and are created using workload resources.
See [Working with Pods](https://kubernetes.io/docs/concepts/workloads/pods/#working-with-pods) for more information on how Pods are used
with workload resources.