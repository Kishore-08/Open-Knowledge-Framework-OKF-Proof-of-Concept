---
id: kubernetes-path-types-d8c8df3b
type: concept
title: Path types
description: Each path in an Ingress is required to have a corresponding path type.
  Paths
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Path types

Each path in an Ingress is required to have a corresponding path type. Paths
that do not include an explicit `pathType` will fail validation. There are three
supported path types:

- `ImplementationSpecific`: With this path type, matching is up to the
  IngressClass. Implementations can treat this as a separate `pathType` or treat
  it identically to `Prefix` or `Exact` path types.
- `Exact`: Matches the URL path exactly and with case sensitivity.
- `Prefix`: Matches based on a URL path prefix split by `/`. Matching is case
  sensitive and done on a path element by element basis. A path element refers
  to the list of labels in the path split by the `/` separator. A request is a
  match for path *p* if every *p* is an element-wise prefix of *p* of the
  request path.

  #### Note:

  If the last element of the path is a substring of the last
  element in request path, it is not a match (for example: `/foo/bar`
  matches `/foo/bar/baz`, but does not match `/foo/barbaz`).