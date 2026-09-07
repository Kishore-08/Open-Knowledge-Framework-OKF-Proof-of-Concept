---
id: kubernetes-don-t-rely-on-mutating-webhook-invocation-order-137dc105
type: concept
title: Don't rely on mutating webhook invocation order
description: Mutating admission webhooks don't run in a consistent order. Various
  factors
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Don't rely on mutating webhook invocation order

Mutating admission webhooks don't run in a consistent order. Various factors
might change when a specific webhook is called. Don't rely on your webhook
running at a specific point in the admission process. Other webhooks could still
mutate your modified object.

The following recommendations might help to minimize the risk of unintended
changes:

- [Validate mutations before admission](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/#validate-mutations)
- Use a reinvocation policy to observe changes to an object by other plugins
  and re-run the webhook as needed. For details, see
  [Reinvocation policy](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#reinvocation-policy).