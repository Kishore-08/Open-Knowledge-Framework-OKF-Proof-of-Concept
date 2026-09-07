---
id: kubernetes-ensure-that-mutations-don-t-violate-validations-137dc105
type: concept
title: Ensure that mutations don't violate validations
description: Your mutating webhooks shouldn't break any of the validations that apply
  to an
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Ensure that mutations don't violate validations

Your mutating webhooks shouldn't break any of the validations that apply to an
object before admission. For example, consider a mutating webhook that sets the
default CPU request of a Pod to a specific value. If the CPU limit of that Pod
is set to a lower value than the mutated request, the Pod fails admission.

Test every mutating webhook against the validations that run in your cluster.