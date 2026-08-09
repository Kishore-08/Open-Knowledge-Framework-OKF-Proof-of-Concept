---
id: kubernetes-customresourcedefinitions-0f516df7
type: concept
title: CustomResourceDefinitions
description: The [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## CustomResourceDefinitions

The [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)
API resource allows you to define custom resources.
Defining a CRD object creates a new custom resource with a name and schema that you specify.
The Kubernetes API serves and handles the storage of your custom resource.
The name of the CRD object itself must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names) derived from the defined resource name and its API group; see [how to create a CRD](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#create-a-customresourcedefinition) for more details.
Further, the name of an object whose kind/resource is defined by a CRD must also be a valid DNS subdomain name.

This frees you from writing your own API server to handle the custom resource,
but the generic nature of the implementation means you have less flexibility than with
[API server aggregation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#api-server-aggregation).

Refer to the [custom controller example](https://github.com/kubernetes/sample-controller)
for an example of how to register a new custom resource, work with instances of your new resource type,
and use a controller to handle events.