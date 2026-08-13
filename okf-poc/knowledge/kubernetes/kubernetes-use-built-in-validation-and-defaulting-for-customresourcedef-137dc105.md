---
id: kubernetes-use-built-in-validation-and-defaulting-for-customresourcedef-137dc105
type: concept
title: Use built-in validation and defaulting for CustomResourceDefinitions
description: If you use
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Use built-in validation and defaulting for CustomResourceDefinitions

If you use
[CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server."),
don't use admission webhooks to validate values in CustomResource specifications
or to set default values for fields. Kubernetes lets you define validation rules
and default field values when you create CustomResourceDefinitions.

To learn more, see the following resources:

- [Validation rules](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#validation-rules)
- [Defaulting](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#defaulting)