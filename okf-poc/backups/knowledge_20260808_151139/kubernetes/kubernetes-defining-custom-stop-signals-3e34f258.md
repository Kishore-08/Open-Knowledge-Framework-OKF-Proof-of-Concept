---
id: kubernetes-defining-custom-stop-signals-3e34f258
type: concept
title: Defining custom stop signals
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Defining custom stop signals

FEATURE STATE:
`Kubernetes v1.33 [alpha]`(disabled by default)

If the `ContainerStopSignals` feature gate is enabled, you can configure a custom stop signal
for your containers from the container Lifecycle. We require the Pod's `spec.os.name` field
to be present as a requirement for defining stop signals in the container lifecycle.
The list of signals that are valid depends on the OS the Pod is scheduled to.
For Pods scheduled to Windows nodes, we only support SIGTERM and SIGKILL as valid signals.

Here is an example Pod spec defining a custom stop signal:

```
spec:
  os:
    name: linux
  containers:
    - name: my-container
      image: container-image:latest
      lifecycle:
        stopSignal: SIGUSR1
```

If a stop signal is defined in the lifecycle, this will override the signal defined in the container image.
If no stop signal is defined in the container spec, the container would fall back to the default behavior.