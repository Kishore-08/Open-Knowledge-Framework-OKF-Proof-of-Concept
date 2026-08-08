---
id: kubernetes-operating-on-a-failed-deployment-d9a16560
type: concept
title: Operating on a failed deployment
description: All actions that apply to a complete Deployment also apply to a failed
  Deployment. You can scale it up/down, roll back
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Operating on a failed deployment

All actions that apply to a complete Deployment also apply to a failed Deployment. You can scale it up/down, roll back
to a previous revision, or even pause it if you need to apply multiple tweaks in the Deployment Pod template.