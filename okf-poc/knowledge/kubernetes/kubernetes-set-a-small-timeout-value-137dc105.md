---
id: kubernetes-set-a-small-timeout-value-137dc105
type: concept
title: Set a small timeout value
description: Admission webhooks should evaluate as quickly as possible (typically
  in
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Set a small timeout value

Admission webhooks should evaluate as quickly as possible (typically in
milliseconds), since they add to API request latency. Use a small timeout for
webhooks.

For details, see
[Timeouts](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#timeouts).