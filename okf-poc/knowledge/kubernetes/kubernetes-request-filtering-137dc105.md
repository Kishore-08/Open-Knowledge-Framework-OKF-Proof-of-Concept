---
id: kubernetes-request-filtering-137dc105
type: concept
title: Request filtering
description: This section provides recommendations for filtering which requests trigger
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Request filtering

This section provides recommendations for filtering which requests trigger
specific webhooks. In summary, these are as follows:

- Limit the webhook scope to avoid system components and read-only requests.
- Limit webhooks to specific namespaces.
- Use match conditions to perform fine-grained request filtering.
- Match all versions of an object.