---
id: kubernetes-raw-block-volume-support-9fac4033
type: concept
title: Raw Block Volume Support
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Raw Block Volume Support

FEATURE STATE:
`Kubernetes v1.18 [stable]`

The following volume plugins support raw block volumes, including dynamic provisioning where
applicable:

- CSI (including some CSI migrated volume types)
- FC (Fibre Channel)
- iSCSI
- Local volume