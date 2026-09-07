---
id: kubernetes-limit-the-scope-of-each-webhook-137dc105
type: concept
title: Limit the scope of each webhook
description: Admission webhooks are only called when an API request matches the corresponding
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Limit the scope of each webhook

Admission webhooks are only called when an API request matches the corresponding
webhook configuration. Limit the scope of each webhook to reduce unnecessary
calls to the webhook server. Consider the following scope limitations:

- Avoid matching objects in the `kube-system` namespace. If you run your own
  Pods in the `kube-system` namespace, use an
  [`objectSelector`](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-objectselector)
  to avoid mutating a critical workload.
- Don't mutate node leases, which exist as Lease objects in the
  `kube-node-lease` system namespace. Mutating node leases might result in
  failed node upgrades. Only apply validation controls to Lease objects in this
  namespace if you're confident that the controls won't put your cluster at
  risk.
- Don't match TokenReview, SubjectAccessReview, or other
  [virtual authentication and authorization resources](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#excluded-virtual-resources).
  These are always read-only requests, and intercepting them might break your
  cluster. Starting with Kubernetes v1.37, admission webhooks are not called
  for these resources by default.
- Limit each webhook to a specific namespace by using a
  [`namespaceSelector`](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-namespaceselector).