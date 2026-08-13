---
id: kubernetes-framework-workflow-085106f9
type: concept
title: Framework workflow
description: The Scheduling Framework defines a few extension points. Scheduler plugins
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Framework workflow

The Scheduling Framework defines a few extension points. Scheduler plugins
register to be invoked at one or more extension points. Some of these plugins
can change the scheduling decisions and some are informational only.

Each attempt to schedule one Pod is split into two phases, the
**scheduling cycle** and the **binding cycle**.