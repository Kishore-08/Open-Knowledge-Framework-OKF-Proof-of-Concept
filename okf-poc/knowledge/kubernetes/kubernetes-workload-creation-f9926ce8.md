---
id: kubernetes-workload-creation-f9926ce8
type: concept
title: Workload creation
description: Permission to create workloads (either Pods, or
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Workload creation

Permission to create workloads (either Pods, or
[workload resources](https://kubernetes.io/docs/concepts/workloads/controllers/) that manage Pods) in a namespace
implicitly grants access to many other resources in that namespace, such as Secrets, ConfigMaps, and
PersistentVolumes that can be mounted in Pods. Additionally, since Pods can run as any
[ServiceAccount](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/), granting permission
to create workloads also implicitly grants the API access levels of any service account in that
namespace.

Users who can run privileged Pods can use that access to gain node access and potentially to
further elevate their privileges. Where you do not fully trust a user or other principal
with the ability to create suitably secure and isolated Pods, you should enforce either the
**Baseline** or **Restricted** Pod Security Standard.
You can use [Pod Security admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
or other (third party) mechanisms to implement that enforcement.

For these reasons, namespaces should be used to separate resources requiring different levels of
trust or tenancy. It is still considered best practice to follow [least privilege](https://kubernetes.io/docs/concepts/security/rbac-good-practices/#least-privilege)
principles and assign the minimum set of permissions, but boundaries within a namespace should be
considered weak.