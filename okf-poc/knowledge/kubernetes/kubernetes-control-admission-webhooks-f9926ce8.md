---
id: kubernetes-control-admission-webhooks-f9926ce8
type: concept
title: Control admission webhooks
description: Users with control over `validatingwebhookconfigurations` or `mutatingwebhookconfigurations`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Control admission webhooks

Users with control over `validatingwebhookconfigurations` or `mutatingwebhookconfigurations`
can control webhooks that can read any object admitted to the cluster, and in the case of
mutating webhooks, also mutate admitted objects.