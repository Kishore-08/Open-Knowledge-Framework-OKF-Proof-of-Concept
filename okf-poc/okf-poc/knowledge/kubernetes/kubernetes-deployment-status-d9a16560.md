---
id: kubernetes-deployment-status-d9a16560
type: concept
title: Deployment status
description: A Deployment enters various states during its lifecycle. It can be [progressing](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#progressing-deployment)
  while
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Deployment status

A Deployment enters various states during its lifecycle. It can be [progressing](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#progressing-deployment) while
rolling out a new ReplicaSet, it can be [complete](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#complete-deployment), or it can [fail to progress](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#failed-deployment).