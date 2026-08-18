---
id: kubernetes-the-kubeconfig-environment-variable-827da0cf
type: concept
title: The KUBECONFIG environment variable
description: The `KUBECONFIG` environment variable holds a list of kubeconfig files.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## The KUBECONFIG environment variable

The `KUBECONFIG` environment variable holds a list of kubeconfig files.
For Linux and Mac, the list is colon-delimited. For Windows, the list
is semicolon-delimited. The `KUBECONFIG` environment variable is not
required. If the `KUBECONFIG` environment variable doesn't exist,
`kubectl` uses the default kubeconfig file, `$HOME/.kube/config`.

If the `KUBECONFIG` environment variable does exist, `kubectl` uses
an effective configuration that is the result of merging the files
listed in the `KUBECONFIG` environment variable.