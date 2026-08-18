---
id: kubernetes-version-compatibility-76dc59f1
type: concept
title: Version compatibility
description: The `kubectl` tool supports a version skew of plus-or-minus one minor
  version relative to the cluster's
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubectl/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Version compatibility

The `kubectl` tool supports a version skew of plus-or-minus one minor version relative to the cluster's
control plane. For example, `kubectl` v1.32 works with control planes at v1.31, v1.32, and v1.33.
Using a compatible version avoids unexpected behavior. See the
[version skew policy](https://kubernetes.io/releases/version-skew-policy/) for details.