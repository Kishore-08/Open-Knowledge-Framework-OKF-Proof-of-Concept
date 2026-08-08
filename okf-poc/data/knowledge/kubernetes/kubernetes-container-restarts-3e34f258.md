---
id: kubernetes-container-restarts-3e34f258
type: concept
title: Container restarts
description: When a container in your Pod stops, or experiences failure, Kubernetes
  can restart it.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Container restarts

When a container in your Pod stops, or experiences failure, Kubernetes can restart it.
A restart isn't always appropriate; for example,
[init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ "One or more initialization containers that must run to completion before any app containers run.") run only once (if successful),
during Pod startup.
You can configure restarts as a policy that applies to all Pods, or using container-level configuration (for example: when you define a
[sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/ "An auxilliary container that stays running throughout the lifecycle of a Pod.")) or define container-level override.

#### Container restarts and resilience

The Kubernetes project recommends following cloud-native principles, including resilient
design that accounts for unannounced or arbitrary restarts. You can achieve this either
by failing the Pod and relying on automatic
[replacement](https://kubernetes.io/docs/concepts/workloads/controllers/), or you can design for container-level resilience.
Either approach helps to ensure that your overall workload remains available despite
partial failure.

#### Pod-level container restart policy

The `spec` of a Pod has a `restartPolicy` field with possible values Always, OnFailure,
and Never. The default value is Always.

The `restartPolicy` for a Pod applies to [app containers](https://kubernetes.io/docs/reference/glossary/?all=true#term-app-container "A container used to run part of a workload. Compare with init container.")
in the Pod and to regular [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/).
[Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/)
ignore the Pod-level `restartPolicy` field: in Kubernetes, a sidecar is defined as an
entry inside `initContainers` that has its container-level `restartPolicy` set to `Always`.
For init containers that exit with an error, the kubelet restarts the init container if
the Pod level `restartPolicy` is either `OnFailure` or `Always`:

- `Always`: Automatically restarts the container after any termination.
- `OnFailure`: Only restarts the container if it exits with an error (non-zero exit status).
- `Never`: Does not automatically restart the terminated container.

##### Restart behavior comparison

The following table shows how containers behave under different restart policies and exit codes:

| Exit Code | `restartPolicy: Always` | `restartPolicy: OnFailure` | `restartPolicy: Never` | Sidecar Containers |
| --- | --- | --- | --- | --- |
| 0 (Success) | Restarts | Does not restart | Does not restart | Always restarts |
| Non-zero (Failure) | Restarts | Restarts | Does not restart | Always restarts |

#### Note:

The restart behavior is particularly important when choosing between Deployments and Jobs:

- **Deployments** typically use `restartPolicy: Always` (the only allowed value) to keep applications running continuously
- **Jobs** commonly use `restartPolicy: OnFailure` or `restartPolicy: Never` to handle batch processing tasks appropriately
- **Sidecar containers** are init containers that always restart regardless of the Pod's `restartPolicy` because they have their own container-level `restartPolicy: Always`

##### Example scenarios

Here are concrete examples demonstrating the different restart behaviors:

**Example 1: Web server with `restartPolicy: Always` (typical for Deployments)**

```
apiVersion: v1
kind: Pod
metadata:
  name: web-server
spec:
  restartPolicy: Always  # Container restarts regardless of exit code
  containers:
  - name: nginx
    image: nginx:1.14.2
    # If this container crashes or exits for any reason, it will be restarted
```

**Example 2: Batch job with `restartPolicy: OnFailure`**

```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-processor
spec:
  template:
    spec:
      restartPolicy: OnFailure  # Only