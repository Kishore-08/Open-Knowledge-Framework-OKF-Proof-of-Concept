---
id: kubernetes-lifecycle-of-a-volume-and-claim-9fac4033
type: concept
title: Lifecycle of a volume and claim
description: PVs are resources in the cluster. PVCs are requests for those resources
  and also act
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Lifecycle of a volume and claim

PVs are resources in the cluster. PVCs are requests for those resources and also act
as claim checks to the resource. The interaction between PVs and PVCs follows this lifecycle: