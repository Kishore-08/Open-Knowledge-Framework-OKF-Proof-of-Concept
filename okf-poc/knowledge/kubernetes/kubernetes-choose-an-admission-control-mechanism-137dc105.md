---
id: kubernetes-choose-an-admission-control-mechanism-137dc105
type: concept
title: Choose an admission control mechanism
description: Kubernetes includes multiple admission control and policy enforcement
  options.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Choose an admission control mechanism

Kubernetes includes multiple admission control and policy enforcement options.
Knowing when to use a specific option can help you to improve latency and
performance, reduce management overhead, and avoid issues during version
upgrades. The following table describes the mechanisms that let you mutate or
validate resources during admission:

Mutating and validating admission control in Kubernetes

| Mechanism | Description | Use cases |
| --- | --- | --- |
| [Mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) | Intercept API requests before admission and modify as needed using custom logic. | - Make critical modifications that must happen before resource   admission. - Make complex modifications that require advanced logic, like calling   external APIs. |
| [Mutating admission policy](https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/) | Intercept API requests before admission and modify as needed using Common Expression Language (CEL) expressions. | - Make critical modifications that must happen before resource   admission. - Make simple modifications, such as adjusting labels or replica   counts. |
| [Validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/) | Intercept API requests before admission and validate against complex policy declarations. | - Validate critical configurations before resource admission. - Enforce complex policy logic before admission. |
| [Validating admission policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) | Intercept API requests before admission and validate against CEL expressions. | - Validate critical configurations before resource admission. - Enforce policy logic using CEL expressions. |

In general, use *webhook* admission control when you want an extensible way to
declare or configure the logic. Use built-in CEL-based admission control when
you want to declare simpler logic without the overhead of running a webhook
server. The Kubernetes project recommends that you use CEL-based admission
control when possible.