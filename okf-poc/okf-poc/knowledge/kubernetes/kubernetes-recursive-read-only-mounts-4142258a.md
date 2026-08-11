---
id: kubernetes-recursive-read-only-mounts-4142258a
type: concept
title: Recursive read-only mounts
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Recursive read-only mounts

FEATURE STATE:
`Kubernetes v1.33 [stable]`(enabled by default)

Recursive read-only mounts can be enabled by setting the
`RecursiveReadOnlyMounts` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
for kubelet and kube-apiserver, and setting the `.spec.containers[*].volumeMounts[*].recursiveReadOnly`
field for a Pod.

The allowed values are:

- `Disabled` (default): no effect.
- `Enabled`: makes the mount recursively read-only.
  Needs all the following requirements to be satisfied:

  - `readOnly` is set to `true`
  - `mountPropagation` is unset, or set to `None`
  - The host is running with Linux kernel v5.12 or later
  - The [CRI-level](https://kubernetes.io/docs/concepts/architecture/cri) container runtime supports recursive read-only mounts
  - The OCI-level container runtime supports recursive read-only mounts.

  It will fail if any of these is not true.
- `IfPossible`: attempts to apply `Enabled`, and falls back to `Disabled`
  if the feature is not supported by the kernel or the runtime class.

Example:

[`storage/rro.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/storage/rro.yaml)![](https://kubernetes.io/images/copycode.svg "Copy storage/rro.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: rro
spec:
  volumes:
    - name: mnt
      hostPath:
        # tmpfs is mounted on /mnt/tmpfs
        path: /mnt
  containers:
    - name: busybox
      image: busybox
      args: ["sleep", "infinity"]
      volumeMounts:
        # /mnt-rro/tmpfs is not writable
        - name: mnt
          mountPath: /mnt-rro
          readOnly: true
          mountPropagation: None
          recursiveReadOnly: Enabled
        # /mnt-ro/tmpfs is writable
        - name: mnt
          mountPath: /mnt-ro
          readOnly: true
        # /mnt-rw/tmpfs is writable
        - name: mnt
          mountPath: /mnt-rw
```

When this property is recognized by kubelet and kube-apiserver,
the `.status.containerStatuses[*].volumeMounts[*].recursiveReadOnly` field is set to either
`Enabled` or `Disabled`.

#### Implementations

**Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/storage/volumes/#third-party-content-disclaimer)

The following container runtimes are known to support recursive read-only mounts.

CRI-level:

- [containerd](https://containerd.io/), since v2.0
- [CRI-O](https://cri-o.io/), since v1.30

OCI-level:

- [runc](https://runc.io/), since v1.1
- [crun](https://github.com/containers/crun), since v1.8.6

## What's next

Follow an example of [deploying WordPress and MySQL with Persistent Volumes](https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/).