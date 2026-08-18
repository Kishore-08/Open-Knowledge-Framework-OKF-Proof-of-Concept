---
id: kubernetes-using-a-sidecar-container-with-the-logging-agent-16136ba9
type: concept
title: Using a sidecar container with the logging agent
description: 'You can use a sidecar container in one of the following ways:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Using a sidecar container with the logging agent

You can use a sidecar container in one of the following ways:

- The sidecar container streams application logs to its own `stdout`.
- The sidecar container runs a logging agent, which is configured to pick up logs
  from an application container.

#### Streaming sidecar container

By having your sidecar containers write to their own `stdout` and `stderr`
streams, you can take advantage of the kubelet and the logging agent that
already run on each node. The sidecar containers read logs from a file, a socket,
or journald. Each sidecar container prints a log to its own `stdout` or `stderr` stream.

This approach allows you to separate several log streams from different
parts of your application, some of which can lack support
for writing to `stdout` or `stderr`. The logic behind redirecting logs
is minimal, so it's not a significant overhead. Additionally, because
`stdout` and `stderr` are handled by the kubelet, you can use built-in tools
like `kubectl logs`.

For example, a pod runs a single container, and the container
writes to two different log files using two different formats. Here's a
manifest for the Pod:

[`admin/logging/two-files-counter-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/admin/logging/two-files-counter-pod.yaml)![](https://kubernetes.io/images/copycode.svg "Copy admin/logging/two-files-counter-pod.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: counter
spec:
  containers:
  - name: count
    image: busybox:1.28
    args:
    - /bin/sh
    - -c
    - >
      i=0;
      while true;
      do
        echo "$i: $(date)" >> /var/log/1.log;
        echo "$(date) INFO $i" >> /var/log/2.log;
        i=$((i+1));
        sleep 1;
      done
    volumeMounts:
    - name: varlog
      mountPath: /var/log
  volumes:
  - name: varlog
    emptyDir: {}
```

It is not recommended to write log entries with different formats to the same log
stream, even if you managed to redirect both components to the `stdout` stream of
the container. Instead, you can create two sidecar containers. Each sidecar
container could tail a particular log file from a shared volume and then redirect
the logs to its own `stdout` stream.

Here's a manifest for a pod that has two sidecar containers:

[`admin/logging/two-files-counter-pod-streaming-sidecar.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/admin/logging/two-files-counter-pod-streaming-sidecar.yaml)![](https://kubernetes.io/images/copycode.svg "Copy admin/logging/two-files-counter-pod-streaming-sidecar.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: counter
spec:
  containers:
  - name: count
    image: busybox:1.28
    args:
    - /bin/sh
    - -c
    - >
      i=0;
      while true;
      do
        echo "$i: $(date)" >> /var/log/1.log;
        echo "$(date) INFO $i" >> /var/log/2.log;
        i=$((i+1));
        sleep 1;
      done
    volumeMounts:
    - name: varlog
      mountPath: /var/log
  - name: count-log-1
    image: busybox:1.28
    args: [/bin/sh, -c, 'tail -n+1 -F /var/log/1.log']
    volumeMounts:
    - name: varlog
      mountPath: /var/log
  - name: count-log-2
    image: busybox:1.28
    args: [/bin/sh, -c, 'tail -n+1 -F /var/log/2.log']
    volumeMounts:
    - name: varlog
      mountPath: /var/log
  volumes:
  - name: varlog
    emptyDir: {}
```

Now when you run this pod, you can access each log stream separately by
running the following commands:

```
kubectl logs counter count-log-1
```

The output is similar to:

```
0: Fri Apr  1 11:42:26 UTC 2022
1: Fri Apr  1 11:42:27 UTC 2022
2: Fri Apr  1 11:42:28 UTC 2022
...
```

```
kubectl logs counter count-log-2
```

The output is similar to:

```
Fri Apr  1 11:42:29 UTC 2022 INFO 0
Fri Apr  1 11:42:30 UTC 2022 INFO 0
Fri Apr  1 11:42:31 UTC 2022 INFO 0
...
```

If you installed a node-level agent in your cluster, that agent picks up those log
streams