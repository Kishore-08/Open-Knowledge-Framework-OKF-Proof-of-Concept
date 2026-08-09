---
id: kubernetes-choosing-a-method-for-adding-custom-resources-0f516df7
type: concept
title: Choosing a method for adding custom resources
description: CRDs are easier to use. Aggregated APIs are more flexible. Choose the
  method that best meets your needs.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Choosing a method for adding custom resources

CRDs are easier to use. Aggregated APIs are more flexible. Choose the method that best meets your needs.

Typically, CRDs are a good fit if:

- You have a handful of fields
- You are using the resource within your company, or as part of a small open-source project (as
  opposed to a commercial product)