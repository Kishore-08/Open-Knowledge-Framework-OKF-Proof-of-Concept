---
id: kubernetes-constraints-e72e225b
type: concept
title: Constraints
description: '- Each `consumesCounters[]` entry may declare at most **2** group names.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Constraints

- Each `consumesCounters[]` entry may declare at most **2** group names.
- Group names must be unique within a single entry.
- Group names are opaque to Kubernetes; they are meaningful only within the
  publishing driver's pool.
- Groups are compared per counter set: groups on one counter set have no effect
  on co-allocation decisions for a different counter set.