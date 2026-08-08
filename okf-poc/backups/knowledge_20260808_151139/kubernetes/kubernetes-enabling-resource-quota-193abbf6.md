---
id: kubernetes-enabling-resource-quota-193abbf6
type: concept
title: Enabling Resource Quota
description: ResourceQuota support is enabled by default for many Kubernetes distributions.
  It is
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Enabling Resource Quota

ResourceQuota support is enabled by default for many Kubernetes distributions. It is
enabled when the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API.")
`--enable-admission-plugins=` flag has `ResourceQuota` as
one of its arguments.

A resource quota is enforced in a particular namespace when there is a
ResourceQuota in that namespace.

## Types of resource quota

The ResourceQuota mechanism lets you enforce different kinds of limits. This
section describes the types of limit that you can enforce.