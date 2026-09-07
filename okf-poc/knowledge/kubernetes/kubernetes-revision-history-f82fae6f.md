---
id: kubernetes-revision-history-f82fae6f
type: concept
title: Revision history
description: ControllerRevision is a Kubernetes API resource used by controllers,
  such as the StatefulSet controller, to track historical configuration changes.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Revision history

ControllerRevision is a Kubernetes API resource used by controllers, such as the StatefulSet controller, to track historical configuration changes.

StatefulSets use ControllerRevisions to maintain a revision history, enabling rollbacks and version tracking.