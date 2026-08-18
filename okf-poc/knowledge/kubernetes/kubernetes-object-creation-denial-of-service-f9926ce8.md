---
id: kubernetes-object-creation-denial-of-service-f9926ce8
type: concept
title: Object creation denial-of-service
description: Users who have rights to create objects in a cluster may be able to create
  sufficient large
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Object creation denial-of-service

Users who have rights to create objects in a cluster may be able to create sufficient large
objects to create a denial of service condition either based on the size or number of objects, as discussed in
[etcd used by Kubernetes is vulnerable to OOM attack](https://github.com/kubernetes/kubernetes/issues/107325). This may be
specifically relevant in multi-tenant clusters if semi-trusted or untrusted users
are allowed limited access to a system.

One option for mitigation of this issue would be to use
[resource quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/#object-count-quota)
to limit the quantity of objects which can be created.

## What's next

- To learn more about RBAC, see the [RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/).