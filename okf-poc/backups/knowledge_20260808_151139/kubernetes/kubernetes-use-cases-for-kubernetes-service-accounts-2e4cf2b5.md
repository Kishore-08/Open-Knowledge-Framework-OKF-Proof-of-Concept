---
id: kubernetes-use-cases-for-kubernetes-service-accounts-2e4cf2b5
type: concept
title: Use cases for Kubernetes service accounts
description: As a general guideline, you can use service accounts to provide identities
  in
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/service-accounts/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Use cases for Kubernetes service accounts

As a general guideline, you can use service accounts to provide identities in
the following scenarios:

- Your Pods need to communicate with the Kubernetes API server, for example in
  situations such as the following:
  - Providing read-only access to sensitive information stored in Secrets.
  - Granting [cross-namespace access](https://kubernetes.io/docs/concepts/security/service-accounts/#cross-namespace), such as allowing a
    Pod in namespace `example` to read, list, and watch for Lease objects in
    the `kube-node-lease` namespace.
- Your Pods need to communicate with an external service. For example, a
  workload Pod requires an identity for a commercially available cloud API,
  and the commercial provider allows configuring a suitable trust relationship.
- [Authenticating to a private image registry using an `imagePullSecret`](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account).
- An external service needs to communicate with the Kubernetes API server. For
  example, authenticating to the cluster as part of a CI/CD pipeline.
- You use third-party security software in your cluster that relies on the
  ServiceAccount identity of different Pods to group those Pods into different
  contexts.