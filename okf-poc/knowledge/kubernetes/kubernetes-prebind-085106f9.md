---
id: kubernetes-prebind-085106f9
type: concept
title: PreBind
description: These plugins are used to perform any work required before a Pod is bound.
  For
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### PreBind

These plugins are used to perform any work required before a Pod is bound. For
example, a pre-bind plugin may provision a network volume and mount it on the
target node before allowing the Pod to run there.

If any PreBind plugin returns an error, the Pod is [rejected](https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/#reserve) and
returned to the scheduling queue.