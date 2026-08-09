---
id: kubernetes-capacity-9fac4033
type: concept
title: Capacity
description: Generally, a PV will have a specific storage capacity. This is set using
  the PV's
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Capacity

Generally, a PV will have a specific storage capacity. This is set using the PV's
`capacity` attribute which is a [Quantity](https://kubernetes.io/docs/reference/glossary/?all=true#term-quantity "A whole-number representation of small or large numbers using SI suffixes.") value.

Currently, storage size is the only resource that can be set or requested.
Future attributes may include IOPS, throughput, etc.