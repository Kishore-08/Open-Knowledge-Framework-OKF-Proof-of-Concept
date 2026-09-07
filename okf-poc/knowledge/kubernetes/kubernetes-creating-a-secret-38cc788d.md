---
id: kubernetes-creating-a-secret-38cc788d
type: concept
title: Creating a Secret
description: 'There are several options to create a Secret:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Creating a Secret

There are several options to create a Secret:

- [Use `kubectl`](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/)
- [Use a configuration file](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/)
- [Use the Kustomize tool](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/)

#### Constraints on Secret names and data

The name of a Secret object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

You can specify the `data` and/or the `stringData` field when creating a
configuration file for a Secret. The `data` and the `stringData` fields are optional.
The values for all keys in the `data` field have to be base64-encoded strings.
If the conversion to base64 string is not desirable, you can choose to specify
the `stringData` field instead, which accepts arbitrary strings as values.

The keys of `data` and `stringData` must consist of alphanumeric characters,
`-`, `_` or `.`. All key-value pairs in the `stringData` field are internally
merged into the `data` field. If a key appears in both the `data` and the
`stringData` field, the value specified in the `stringData` field takes
precedence.

#### Size limit

Individual Secrets are limited to 1MiB in size. This is to discourage creation
of very large Secrets that could exhaust the API server and kubelet memory.
However, creation of many smaller Secrets could also exhaust memory. You can
use a [resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) to limit the
number of Secrets (or other resources) in a namespace.