---
id: kubernetes-selecting-storage-for-optimal-performance-9edb5061
type: concept
title: Selecting storage for optimal performance
description: The storage device designated for swap space is critical to maintaining
  system responsiveness
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Selecting storage for optimal performance

The storage device designated for swap space is critical to maintaining system responsiveness
during high memory usage.
Rotational hard disk drives (HDDs) are ill-suited for this task as their mechanical nature introduces significant latency,
leading to severe performance degradation and system thrashing.
For modern performance needs, a device such as a Solid State Drive (SSD) is probably the appropriate choice for swap,
as its low-latency electronic access minimizes the slowdown.

## Swap behavior details