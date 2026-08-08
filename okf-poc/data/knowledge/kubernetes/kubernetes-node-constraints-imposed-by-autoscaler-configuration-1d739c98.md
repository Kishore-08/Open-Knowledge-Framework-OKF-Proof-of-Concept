---
id: kubernetes-node-constraints-imposed-by-autoscaler-configuration-1d739c98
type: concept
title: Node constraints imposed by autoscaler configuration
description: The specifics of the provisioned Nodes (for example the amount of resources,
  the presence of a given
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node constraints imposed by autoscaler configuration

The specifics of the provisioned Nodes (for example the amount of resources, the presence of a given
label) depend on autoscaler configuration. Autoscalers can either choose them from a pre-defined set
of Node configurations, or use [auto-provisioning](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/#autoprovisioning).