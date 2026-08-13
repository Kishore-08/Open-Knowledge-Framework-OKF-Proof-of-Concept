---
id: kubernetes-avoid-self-mutations-137dc105
type: concept
title: Avoid self-mutations
description: A webhook running inside the cluster might cause deadlocks for its own
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Avoid self-mutations

A webhook running inside the cluster might cause deadlocks for its own
deployment if it is configured to intercept resources required to start its own
Pods.

For example, a mutating admission webhook is configured to admit **create** Pod
requests only if a certain label is set in the Pod (such as `env: prod`).
The webhook server runs in a Deployment that doesn't set the `env` label.

When a node that runs the webhook server Pods becomes unhealthy, the webhook
Deployment tries to reschedule the Pods to another node. However, the existing
webhook server rejects the requests since the `env` label is unset. As a
result, the migration cannot happen.

Exclude the namespace where your webhook is running with a
[`namespaceSelector`](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-namespaceselector).