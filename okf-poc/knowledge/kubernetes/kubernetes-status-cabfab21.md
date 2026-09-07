---
id: kubernetes-status-cabfab21
type: concept
title: Status
description: The `CompositePodGroup` API schema includes a `status` subresource. In
  the alpha release,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Status

The `CompositePodGroup` API schema includes a `status` subresource. In the alpha release,
the `status` field is present in the API type, but `kube-scheduler` does not update or
populate status conditions for `CompositePodGroup` objects. Status tracking for composite
groups will be implemented in future releases.