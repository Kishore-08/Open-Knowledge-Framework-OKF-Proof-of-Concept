---
id: kubernetes-editing-a-secret-38cc788d
type: concept
title: Editing a Secret
description: You can edit an existing Secret unless it is [immutable](https://kubernetes.io/docs/concepts/configuration/secret/#secret-immutable).
  To
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Editing a Secret

You can edit an existing Secret unless it is [immutable](https://kubernetes.io/docs/concepts/configuration/secret/#secret-immutable). To
edit a Secret, use one of the following methods:

- [Use `kubectl`](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/#edit-secret)
- [Use a configuration file](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/#edit-secret)

You can also edit the data in a Secret using the [Kustomize tool](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/#edit-secret). However, this
method creates a new `Secret` object with the edited data.

Depending on how you created the Secret, as well as how the Secret is used in
your Pods, updates to existing `Secret` objects are propagated automatically to
Pods that use the data. For more information, refer to [Using Secrets as files from a Pod](https://kubernetes.io/docs/concepts/configuration/secret/#using-secrets-as-files-from-a-pod) section.