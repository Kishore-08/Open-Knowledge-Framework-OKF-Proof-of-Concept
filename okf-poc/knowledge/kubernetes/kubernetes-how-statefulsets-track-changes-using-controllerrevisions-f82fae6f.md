---
id: kubernetes-how-statefulsets-track-changes-using-controllerrevisions-f82fae6f
type: concept
title: How StatefulSets track changes using ControllerRevisions
description: 'When you update a StatefulSet''s Pod template (`spec.template`), the
  StatefulSet controller:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### How StatefulSets track changes using ControllerRevisions

When you update a StatefulSet's Pod template (`spec.template`), the StatefulSet controller:

1. Prepares a new ControllerRevision object
2. Stores a snapshot of the Pod template and metadata
3. Assigns an incremental revision number

#### Key Properties

See [ControllerRevision](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/controller-revision-v1/) to learn more about key properties and other details.

---