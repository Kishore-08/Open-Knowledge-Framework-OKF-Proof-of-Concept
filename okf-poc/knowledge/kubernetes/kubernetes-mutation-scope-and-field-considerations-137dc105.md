---
id: kubernetes-mutation-scope-and-field-considerations-137dc105
type: concept
title: Mutation scope and field considerations
description: This section provides recommendations for the scope of mutations and
  any special
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Mutation scope and field considerations

This section provides recommendations for the scope of mutations and any special
considerations for object fields. In summary, these are as follows:

- Patch only the fields that you need to patch.
- Don't overwrite array values.
- Avoid side effects in mutations when possible.
- Avoid self-mutations.
- Fail open and validate the final state.
- Plan for future field updates in later versions.
- Prevent webhooks from self-triggering.
- Don't change immutable objects.