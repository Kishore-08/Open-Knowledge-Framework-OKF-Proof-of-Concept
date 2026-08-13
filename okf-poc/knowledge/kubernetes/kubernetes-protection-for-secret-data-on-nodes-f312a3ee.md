---
id: kubernetes-protection-for-secret-data-on-nodes-f312a3ee
type: concept
title: Protection for Secret data on nodes
description: On Windows, data from Secrets are written out in clear text onto the
  node's local
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/windows-security/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Protection for Secret data on nodes

On Windows, data from Secrets are written out in clear text onto the node's local
storage (as compared to using tmpfs / in-memory filesystems on Linux). As a cluster
operator, you should take both of the following additional measures:

1. Use file ACLs to secure the Secrets' file location.
2. Apply volume-level encryption using
   [BitLocker](https://docs.microsoft.com/windows/security/information-protection/bitlocker/bitlocker-how-to-deploy-on-windows-server).