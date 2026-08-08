---
id: kubernetes-runtime-protection-storage-4d305e15
type: concept
title: 'Runtime protection: storage'
description: 'To protect storage for your cluster and the applications that run there,
  you can:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Runtime protection: storage

To protect storage for your cluster and the applications that run there, you can:

1. Integrate your cluster with an external storage plugin that provides encryption at
   rest for volumes.
2. Enable [encryption at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) for
   API objects.
3. Protect data durability using backups, and verify that you can restore them whenever needed.
4. Authenticate connections between cluster nodes and any network storage they rely
   upon.
5. Implement data encryption within your own application.

For encryption keys, generating these within specialized hardware provides
the best protection against disclosure risks. A *hardware security module*
can let you perform cryptographic operations without allowing the security
key to be copied elsewhere.