---
id: kubernetes-reclaim-policy-9fac4033
type: concept
title: Reclaim Policy
description: 'Current reclaim policies are:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Reclaim Policy

Current reclaim policies are:

- Retain -- manual reclamation
- Recycle -- basic scrub (`rm -rf /thevolume/*`)
- Delete -- delete the volume

For Kubernetes 1.36, only `nfs` and `hostPath` volume types support recycling.