---
id: kubernetes-prevent-your-webhook-from-triggering-itself-137dc105
type: concept
title: Prevent your webhook from triggering itself
description: Mutating webhooks that respond to a broad range of API requests might
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Prevent your webhook from triggering itself

Mutating webhooks that respond to a broad range of API requests might
unintentionally trigger themselves. For example, consider a webhook that
responds to all requests in the cluster. If you configure the webhook to create
Event objects for every mutation, it'll respond to its own Event object
creation requests.

To avoid this, consider setting a unique label in any resources that your
webhook creates. Exclude this label from your webhook match conditions.