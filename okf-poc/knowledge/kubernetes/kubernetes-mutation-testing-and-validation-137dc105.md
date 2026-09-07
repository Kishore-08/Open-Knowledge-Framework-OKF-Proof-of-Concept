---
id: kubernetes-mutation-testing-and-validation-137dc105
type: concept
title: Mutation testing and validation
description: This section provides recommendations for testing your mutating webhooks
  and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Mutation testing and validation

This section provides recommendations for testing your mutating webhooks and
validating mutated objects. In summary, these are as follows:

- Test webhooks in staging environments.
- Avoid mutations that violate validations.
- Test minor version upgrades for regressions and conflicts.
- Validate mutated objects before admission.