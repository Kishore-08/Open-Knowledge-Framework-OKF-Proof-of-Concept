---
id: kubernetes-deploy-lifecycle-phase-4d305e15
type: concept
title: '*Deploy* lifecycle phase'
description: Ensure appropriate restrictions on what can be deployed, who can deploy
  it,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## *Deploy* lifecycle phase

Ensure appropriate restrictions on what can be deployed, who can deploy it,
and where it can be deployed.
You can enforce measures from the *distribute* phase, such as verifying the
cryptographic identity of container image artifacts.

You can deploy different applications and cluster components into different
[namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster."). Containers
and namespaces both provide isolation mechanisms that are relevant to
information security.

When you deploy Kubernetes, you also set the foundation for your
applications' runtime environment: a Kubernetes cluster (or
multiple clusters).
That infrastructure must provide the security guarantees that higher
layers expect.