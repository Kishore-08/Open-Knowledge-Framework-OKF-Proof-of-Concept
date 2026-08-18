---
id: kubernetes-pod-and-container-logs-16136ba9
type: concept
title: Pod and container logs
description: Kubernetes captures logs from each container in a running Pod.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Pod and container logs

Kubernetes captures logs from each container in a running Pod.

This example uses a manifest for a `Pod` with a container
that writes text to the standard output stream, once per second.

[`debug/counter-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/debug/counter-pod.yaml)![](https://kubernetes.io/images/copycode.svg "Copy debug/counter-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: counter
spec:
  containers:
  - name: count
    image: busybox:1.28
    args: [/bin/sh, -c,
            'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done']
```

To run this pod, use the following command:

```
kubectl apply -f https://k8s.io/examples/debug/counter-pod.yaml
```

The output is:

```
pod/counter created
```

To fetch the logs, use the `kubectl logs` command, as follows:

```
kubectl logs counter
```

The output is similar to:

```
0: Fri Apr  1 11:42:23 UTC 2022
1: Fri Apr  1 11:42:24 UTC 2022
2: Fri Apr  1 11:42:25 UTC 2022
```

You can use `kubectl logs --previous` to retrieve logs from a previous instantiation of a container.
If your pod has multiple containers, specify which container's logs you want to access by
appending a container name to the command, with a `-c` flag, like so:

```
kubectl logs counter -c count
```