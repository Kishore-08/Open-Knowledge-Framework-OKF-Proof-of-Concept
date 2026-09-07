---
id: kubernetes-bind-mount-options-4142258a
type: concept
title: Bind mount options
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Bind mount options

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

The `.spec.containers[*].volumeMounts[*].bindMountOptions` field lets you apply security-related
Linux bind mount flags to any volume mount. The allowed values are:

- `noexec` - prevents execution of binaries on the mounted volume
- `nodev` - ignores device special files on the mounted volume
- `nosuid` - ignores set-user-identifier or set-group-identifier bits on the mounted volume

These options apply per container, so different containers in the same Pod can mount
the same volume with different bind mount options. The field is not supported with
[image volumes](https://kubernetes.io/docs/concepts/storage/volumes/#image).

#### Note:

The container runtime (such as containerd or CRI-O) must support the `mount_options`
field in the CRI `Mount` message. If the runtime does not advertise support, the kubelet
rejects Pods that use `bindMountOptions`. This field has no effect on Windows nodes.

## What's next

Follow an example of [deploying WordPress and MySQL with Persistent Volumes](https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/).