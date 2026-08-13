---
id: kubernetes-match-all-versions-of-an-api-137dc105
type: concept
title: Match all versions of an API
description: By default, admission webhooks run on any API versions that affect a
  specified
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Match all versions of an API

By default, admission webhooks run on any API versions that affect a specified
resource. The `matchPolicy` field in the webhook configuration controls this
behavior. Specify a value of `Equivalent` in the `matchPolicy` field or omit
the field to allow the webhook to run on any API version.

For details, see
[Matching requests: `matchPolicy`](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-matchpolicy).