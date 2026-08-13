---
id: kubernetes-route-controller-8c98aece
type: concept
title: Route controller
description: The route controller is responsible for configuring routes in the cloud
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Route controller

The route controller is responsible for configuring routes in the cloud
appropriately so that containers on different nodes in your Kubernetes
cluster can communicate with each other.

Depending on the cloud provider, the route controller might also allocate blocks
of IP addresses for the Pod network.