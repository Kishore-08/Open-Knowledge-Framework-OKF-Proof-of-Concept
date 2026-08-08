---
id: kubernetes-selectable-fields-for-custom-resources-0f516df7
type: concept
title: Selectable fields for custom resources
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Selectable fields for custom resources

FEATURE STATE:
`Kubernetes v1.32 [stable]`(enabled by default)

The `spec.versions[*].selectableFields` field of a [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.") may be used to
declare which other fields in a custom resource may be used in field selectors.

The following example adds the `.spec.color` and `.spec.size` fields as
selectable fields.

[`customresourcedefinition/shirt-resource-definition.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/customresourcedefinition/shirt-resource-definition.yaml)![](https://kubernetes.io/images/copycode.svg "Copy customresourcedefinition/shirt-resource-definition.yaml to clipboard")

```
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: shirts.stable.example.com
spec:
  group: stable.example.com
  scope: Namespaced
  names:
    plural: shirts
    singular: shirt
    kind: Shirt
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              color:
                type: string
              size:
                type: string
    selectableFields:
    - jsonPath: .spec.color
    - jsonPath: .spec.size
    additionalPrinterColumns:
    - jsonPath: .spec.color
      name: Color
      type: string
    - jsonPath: .spec.size
      name: Size
      type: string
```

Field selectors can then be used to get only resources with a `color` of `blue`:

```
kubectl get shirts.stable.example.com --field-selector spec.color=blue
```

The output should be:

```
NAME       COLOR  SIZE
example1   blue   S
example2   blue   M
```