---
id: kubernetes-security-c2988c6c
type: concept
title: Security
description: Using generic ephemeral volumes allows users to create PVCs indirectly
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Security

Using generic ephemeral volumes allows users to create PVCs indirectly
if they can create Pods, even if they do not have permission to create PVCs directly.
Cluster administrators must be aware of this. If this does not fit their security model,
they should use an [admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)
that rejects objects like Pods that have a generic ephemeral volume.

The normal [namespace quota for PVCs](https://kubernetes.io/docs/concepts/policy/resource-quotas/#storage-resource-quota)
still applies, so even if users are allowed to use this new mechanism, they cannot use
it to circumvent other policies.

## What's next

### Ephemeral volumes managed by kubelet

See [local ephemeral storage](https://kubernetes.io/docs/concepts/storage/ephemeral-storage/).