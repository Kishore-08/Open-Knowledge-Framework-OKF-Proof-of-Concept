---
id: kubernetes-supporting-multiple-clusters-users-and-authentication-mechan-827da0cf
type: concept
title: Supporting multiple clusters, users, and authentication mechanisms
description: Suppose you have several clusters, and your users and components authenticate
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Supporting multiple clusters, users, and authentication mechanisms

Suppose you have several clusters, and your users and components authenticate
in a variety of ways. For example:

- A running kubelet might authenticate using certificates.
- A user might authenticate using tokens.
- Administrators might have sets of certificates that they provide to individual users.

With kubeconfig files, you can organize your clusters, users, and namespaces.
You can also define contexts to quickly and easily switch between
clusters and namespaces.