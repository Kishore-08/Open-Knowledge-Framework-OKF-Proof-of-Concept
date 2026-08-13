---
id: kubernetes-avoid-dependency-loops-137dc105
type: concept
title: Avoid dependency loops
description: 'Dependency loops can occur in scenarios like the following:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Avoid dependency loops

Dependency loops can occur in scenarios like the following:

- Two webhooks check each other's Pods. If both webhooks become unavailable
  at the same time, neither webhook can start.
- Your webhook intercepts cluster add-on components, such as networking plugins
  or storage plugins, that your webhook depends on. If both the webhook and the
  dependent add-on become unavailable, neither component can function.

To avoid these dependency loops, try the following:

- Use
  [ValidatingAdmissionPolicies](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
  to avoid introducing dependencies.
- Prevent webhooks from validating or mutating other webhooks. Consider
  [excluding specific namespaces](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-namespaceselector)
  from triggering your webhook.
- Prevent your webhooks from acting on dependent add-ons by using an
  [`objectSelector`](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-objectselector).