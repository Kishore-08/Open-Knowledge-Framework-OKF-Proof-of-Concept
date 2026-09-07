---
id: kubernetes-when-to-use-multiple-namespaces-0663647e
type: concept
title: When to Use Multiple Namespaces
description: Namespaces are intended for use in environments with many users spread
  across multiple
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## When to Use Multiple Namespaces

Namespaces are intended for use in environments with many users spread across multiple
teams, or projects. For clusters with a few to tens of users, you should not
need to create or think about namespaces at all. Start using namespaces when you
need the features they provide.

Namespaces provide a scope for names. Names of resources need to be unique within a namespace,
but not across namespaces. Namespaces cannot be nested inside one another and each Kubernetes
resource can only be in one namespace.

Namespaces are a way to divide cluster resources between multiple users (via [resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/)).

It is not necessary to use multiple namespaces to separate slightly different
resources, such as different versions of the same software: use
[labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") to distinguish
resources within the same namespace.

#### Note:

For a production cluster, consider *not* using the `default` namespace. Instead, make other namespaces and use those.