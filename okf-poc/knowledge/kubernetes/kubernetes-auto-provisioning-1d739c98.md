---
id: kubernetes-auto-provisioning-1d739c98
type: concept
title: Auto-provisioning
description: Node auto-provisioning is a mode of provisioning in which a user doesn't
  have to fully configure the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Auto-provisioning

Node auto-provisioning is a mode of provisioning in which a user doesn't have to fully configure the
specifics of the Nodes that can be provisioned. Instead, the autoscaler dynamically chooses the Node
configuration based on the pending Pods it's reacting to, as well as pre-configured constraints (for
example, the minimum amount of resources or the need for a given label).