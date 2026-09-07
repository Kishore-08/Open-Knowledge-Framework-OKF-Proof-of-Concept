---
id: kubernetes-persistent-pool-and-restarts-0cecd4eb
type: concept
title: Persistent pool and restarts
description: The Pod's total resource pool (the NUMA alignment and total reserved
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/pod-level-resource-managers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Persistent pool and restarts

The Pod's total resource pool (the NUMA alignment and total reserved
capacity) is persistent. If a container in the Pod's shared pool crashes
and restarts, the Pod's overall resource reservation remains safely
anchored on the Node. The Node releases the resources back to its general
pool only when the entire Pod terminates.