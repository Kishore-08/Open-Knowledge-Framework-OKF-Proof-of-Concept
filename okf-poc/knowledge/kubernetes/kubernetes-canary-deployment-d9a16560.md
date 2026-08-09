---
id: kubernetes-canary-deployment-d9a16560
type: concept
title: Canary Deployment
description: If you want to roll out releases to a subset of users or servers using
  the Deployment, you
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Canary Deployment

If you want to roll out releases to a subset of users or servers using the Deployment, you
can create multiple Deployments, one for each release, following the canary pattern described in
[managing resources](https://kubernetes.io/docs/concepts/workloads/management/#canary-deployments).