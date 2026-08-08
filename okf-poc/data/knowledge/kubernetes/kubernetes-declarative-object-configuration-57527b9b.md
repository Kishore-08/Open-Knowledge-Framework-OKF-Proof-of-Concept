---
id: kubernetes-declarative-object-configuration-57527b9b
type: concept
title: Declarative object configuration
description: When using declarative object configuration, a user operates on object
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Declarative object configuration

When using declarative object configuration, a user operates on object
configuration files stored locally, however the user does not define the
operations to be taken on the files. Create, update, and delete operations
are automatically detected per-object by `kubectl`. This enables working on
directories, where different operations might be needed for different objects.

#### Note:

Declarative object configuration retains changes made by other
writers, even if the changes are not merged back to the object configuration file.
This is possible by using the `patch` API operation to write only
observed differences, instead of using the `replace`
API operation to replace the entire object configuration.