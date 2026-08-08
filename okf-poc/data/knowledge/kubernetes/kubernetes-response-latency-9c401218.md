---
id: kubernetes-response-latency-9c401218
type: concept
title: Response latency
description: Extension API servers should have low latency networking to and from
  the kube-apiserver.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Response latency

Extension API servers should have low latency networking to and from the kube-apiserver.
Discovery requests are required to round-trip from the kube-apiserver in five seconds or less.

If your extension API server cannot achieve that latency requirement, consider making changes that
let you meet it.