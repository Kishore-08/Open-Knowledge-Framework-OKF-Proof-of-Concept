---
id: kubernetes-others-8c98aece
type: concept
title: Others
description: The implementation of the core of the cloud controller manager requires
  access to create Event
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Others

The implementation of the core of the cloud controller manager requires access to create Event
objects, and to ensure secure operation, it requires access to create ServiceAccounts.

`v1/Event`:

- create
- patch
- update

`v1/ServiceAccount`:

- create

The [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/ "Manages authorization decisions, allowing admins to dynamically configure access policies through the Kubernetes API.") ClusterRole for the cloud
controller manager looks like:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cloud-controller-manager
rules:
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - '*'
- apiGroups:
  - ""
  resources:
  - nodes/status
  verbs:
  - patch
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - services/status
  verbs:
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - persistentvolumes
  verbs:
  - get
  - list
  - update
  - watch
```