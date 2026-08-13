---
id: kubernetes-avoid-side-effects-137dc105
type: concept
title: Avoid side effects
description: Ensure that your webhooks operate only on the content of the AdmissionReview
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Avoid side effects

Ensure that your webhooks operate only on the content of the AdmissionReview
that's sent to them, and do not make out-of-band changes. These additional
changes, called *side effects*, might cause conflicts during admission if they
aren't reconciled properly. The `.webhooks[].sideEffects` field should
be set to `None` if a webhook doesn't have any side effect.

If side effects are required during the admission evaluation, they must be
suppressed when processing an AdmissionReview object with `dryRun` set to
`true`, and the `.webhooks[].sideEffects` field should be set to `NoneOnDryRun`.

For details, see
[Side effects](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#side-effects).