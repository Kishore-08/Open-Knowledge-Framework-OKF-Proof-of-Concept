---
id: kubernetes-parent-group-reference-cabfab21
type: concept
title: Parent group reference
description: Non-root `CompositePodGroup` resources specify their parent group using
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/compositepodgroup-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Parent group reference

Non-root `CompositePodGroup` resources specify their parent group using
`spec.parentCompositePodGroupName`. Root `CompositePodGroup` objects leave this field unset.

```
spec:
  parentCompositePodGroupName: root-group-0
```