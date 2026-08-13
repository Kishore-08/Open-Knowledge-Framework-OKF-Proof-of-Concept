---
id: kubernetes-bind-085106f9
type: concept
title: Bind
description: These plugins are used to bind a Pod to a Node. Bind plugins will not
  be called
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Bind

These plugins are used to bind a Pod to a Node. Bind plugins will not be called
until all PreBind plugins have completed. Each bind plugin is called in the
configured order. A bind plugin may choose whether or not to handle the given
Pod. If a bind plugin chooses to handle a Pod, **the remaining bind plugins are
skipped**.

### PostBind

This is an informational interface. Post-bind plugins are called after a
Pod is successfully bound. This is the end of a binding cycle, and can be used
to clean up associated resources.