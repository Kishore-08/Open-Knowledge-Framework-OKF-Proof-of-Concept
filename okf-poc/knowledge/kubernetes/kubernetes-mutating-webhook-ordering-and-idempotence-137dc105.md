---
id: kubernetes-mutating-webhook-ordering-and-idempotence-137dc105
type: concept
title: Mutating webhook ordering and idempotence
description: This section provides recommendations for webhook order and designing
  idempotent
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Mutating webhook ordering and idempotence

This section provides recommendations for webhook order and designing idempotent
webhooks. In summary, these are as follows:

- Don't rely on a specific order of execution.
- Validate mutations before admission.
- Check for mutations being overwritten by other controllers.
- Ensure that the set of mutating webhooks is idempotent, not just the
  individual webhooks.