---
id: kubernetes-custom-resource-field-selectors-0f516df7
type: concept
title: Custom resource field selectors
description: '[Field Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Custom resource field selectors

[Field Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/)
let clients select custom resources based on the value of one or more resource
fields.

All custom resources support the `metadata.name` and `metadata.namespace` field
selectors.

Fields declared in a [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.")
may also be used with field selectors when included in the `spec.versions[*].selectableFields` field of the
[CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.").