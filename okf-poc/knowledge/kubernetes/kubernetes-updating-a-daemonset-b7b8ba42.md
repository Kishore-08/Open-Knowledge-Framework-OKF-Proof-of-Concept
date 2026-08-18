---
id: kubernetes-updating-a-daemonset-b7b8ba42
type: concept
title: Updating a DaemonSet
description: If node labels are changed, the DaemonSet will promptly add Pods to newly
  matching nodes and delete
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Updating a DaemonSet

If node labels are changed, the DaemonSet will promptly add Pods to newly matching nodes and delete
Pods from newly not-matching nodes.

You can modify the Pods that a DaemonSet creates. However, Pods do not allow all
fields to be updated. Also, the DaemonSet controller will use the original template the next
time a node (even with the same name) is created.

You can delete a DaemonSet. If you specify `--cascade=orphan` with `kubectl`, then the Pods
will be left on the nodes. If you subsequently create a new DaemonSet with the same selector,
the new DaemonSet adopts the existing Pods. If any Pods need replacing the DaemonSet replaces
them according to its `updateStrategy`.

You can [perform a rolling update](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/) on a DaemonSet.

## Alternatives to DaemonSet