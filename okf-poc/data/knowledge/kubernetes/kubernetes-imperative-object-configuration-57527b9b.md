---
id: kubernetes-imperative-object-configuration-57527b9b
type: concept
title: Imperative object configuration
description: In imperative object configuration, the kubectl command specifies the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Imperative object configuration

In imperative object configuration, the kubectl command specifies the
operation (create, replace, etc.), optional flags and at least one file
name. The file specified must contain a full definition of the object
in YAML or JSON format.

See the [API reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/)
for more details on object definitions.

#### Warning:

The imperative `replace` command replaces the existing
spec with the newly provided one, dropping all changes to the object missing from
the configuration file. This approach should not be used with resource
types whose specs are updated independently of the configuration file.
Services of type `LoadBalancer`, for example, have their `externalIPs` field updated
independently from the configuration by the cluster.