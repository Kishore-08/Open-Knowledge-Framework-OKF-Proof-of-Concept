---
id: kubernetes-don-t-overwrite-array-values-137dc105
type: concept
title: Don't overwrite array values
description: Fields in Kubernetes object specifications might include arrays. Some
  arrays
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Don't overwrite array values

Fields in Kubernetes object specifications might include arrays. Some arrays
contain key:value pairs (like the `envVar` field in a container specification),
while other arrays are unkeyed (like the `readinessGates` field in a Pod
specification). The order of values in an array field might matter in some
situations. For example, the order of arguments in the `args` field of a
container specification might affect the container.

Consider the following when modifying arrays:

- Whenever possible, use the `add` JSONPatch operation instead of `replace` to
  avoid accidentally replacing a required value.
- Treat arrays that don't use key:value pairs as sets.
- Ensure that the values in the field that you modify aren't required to be
  in a specific order.
- Don't overwrite existing key:value pairs unless absolutely necessary.
- Use caution when modifying label fields. An accidental modification might
  cause label selectors to break, resulting in unintended behavior.