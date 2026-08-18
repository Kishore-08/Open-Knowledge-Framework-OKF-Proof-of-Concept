---
id: kubernetes-persistent-volume-creation-f9926ce8
type: concept
title: Persistent volume creation
description: If someone - or some application - is allowed to create arbitrary PersistentVolumes,
  that access
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Persistent volume creation

If someone - or some application - is allowed to create arbitrary PersistentVolumes, that access
includes the creation of `hostPath` volumes, which then means that a Pod would get access
to the underlying host filesystem(s) on the associated node. Granting that ability is a security risk.

There are many ways a container with unrestricted access to the host filesystem can escalate privileges, including
reading data from other containers, and abusing the credentials of system services, such as Kubelet.

You should only allow access to create PersistentVolume objects for:

- Users (cluster operators) that need this access for their work, and who you trust.
- The Kubernetes control plane components which creates PersistentVolumes based on PersistentVolumeClaims
  that are configured for automatic provisioning.
  This is usually setup by the Kubernetes provider or by the operator when installing a CSI driver.

Where access to persistent storage is required trusted administrators should create
PersistentVolumes, and constrained users should use PersistentVolumeClaims to access that storage.