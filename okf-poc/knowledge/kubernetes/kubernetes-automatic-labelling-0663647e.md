---
id: kubernetes-automatic-labelling-0663647e
type: concept
title: Automatic labelling
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Automatic labelling

FEATURE STATE:
`Kubernetes 1.22 [stable]`

The Kubernetes control plane sets an immutable [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.")
`kubernetes.io/metadata.name` on all namespaces.
The value of the label is the namespace name.