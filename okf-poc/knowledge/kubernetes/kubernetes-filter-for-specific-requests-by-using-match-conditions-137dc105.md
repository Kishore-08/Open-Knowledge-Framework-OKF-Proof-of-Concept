---
id: kubernetes-filter-for-specific-requests-by-using-match-conditions-137dc105
type: concept
title: Filter for specific requests by using match conditions
description: Admission controllers support multiple fields that you can use to match
  requests
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Filter for specific requests by using match conditions

Admission controllers support multiple fields that you can use to match requests
that meet specific criteria. For example, you can use a `namespaceSelector` to
filter for requests that target a specific namespace.

For more fine-grained request filtering, use the `matchConditions` field in your
webhook configuration. This field lets you write multiple CEL expressions that
must evaluate to `true` for a request to trigger your admission webhook. Using
`matchConditions` might significantly reduce the number of calls to your webhook
server.

For details, see
[Matching requests: `matchConditions`](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-matchconditions).