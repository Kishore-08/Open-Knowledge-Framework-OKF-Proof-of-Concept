---
id: kubernetes-container-log-streams-16136ba9
type: concept
title: Container log streams
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Container log streams

FEATURE STATE:
`Kubernetes v1.32 [alpha]`(disabled by default)

As an alpha feature, the kubelet can split out the logs from the two standard streams produced
by a container: [standard output](https://en.wikipedia.org/wiki/Standard_streams#Standard_output_(stdout))
and [standard error](https://en.wikipedia.org/wiki/Standard_streams#Standard_error_(stderr)).
To use this behavior, you must enable the `PodLogsQuerySplitStreams`
[feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/).
With that feature gate enabled, Kubernetes 1.36 allows access to these
log streams directly via the Pod API. You can fetch a specific stream by specifying the stream name (either `Stdout` or `Stderr`),
using the `stream` query string. You must have access to read the `log` subresource of that Pod.

To demonstrate this feature, you can create a Pod that periodically writes text to both the standard output and error stream.

[`debug/counter-pod-err.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/debug/counter-pod-err.yaml)![](https://kubernetes.io/images/copycode.svg "Copy debug/counter-pod-err.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: counter-err
spec:
  containers:
  - name: count
    image: busybox:1.28
    args: [/bin/sh, -c,
            'i=0; while true; do echo "$i: $(date)"; echo "$i: err" >&2 ; i=$((i+1)); sleep 1; done']
```

To run this pod, use the following command:

```
kubectl apply -f https://k8s.io/examples/debug/counter-pod-err.yaml
```

To fetch only the stderr log stream, you can run:

```
kubectl get --raw "/api/v1/namespaces/default/pods/counter-err/log?stream=Stderr"
```

See the [`kubectl logs` documentation](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs)
for more details.