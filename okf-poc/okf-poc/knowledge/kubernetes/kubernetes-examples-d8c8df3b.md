---
id: kubernetes-examples-d8c8df3b
type: concept
title: Examples
description: '| Kind | Path(s) | Request path(s) | Matches? |'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Examples

| Kind | Path(s) | Request path(s) | Matches? |
| --- | --- | --- | --- |
| Prefix | `/` | (all paths) | Yes |
| Exact | `/foo` | `/foo` | Yes |
| Exact | `/foo` | `/bar` | No |
| Exact | `/foo` | `/foo/` | No |
| Exact | `/foo/` | `/foo` | No |
| Prefix | `/foo` | `/foo`, `/foo/` | Yes |
| Prefix | `/foo/` | `/foo`, `/foo/` | Yes |
| Prefix | `/aaa/bb` | `/aaa/bbb` | No |
| Prefix | `/aaa/bbb` | `/aaa/bbb` | Yes |
| Prefix | `/aaa/bbb/` | `/aaa/bbb` | Yes, ignores trailing slash |
| Prefix | `/aaa/bbb` | `/aaa/bbb/` | Yes, matches trailing slash |
| Prefix | `/aaa/bbb` | `/aaa/bbb/ccc` | Yes, matches subpath |
| Prefix | `/aaa/bbb` | `/aaa/bbbxyz` | No, does not match string prefix |
| Prefix | `/`, `/aaa` | `/aaa/ccc` | Yes, matches `/aaa` prefix |
| Prefix | `/`, `/aaa`, `/aaa/bbb` | `/aaa/bbb` | Yes, matches `/aaa/bbb` prefix |
| Prefix | `/`, `/aaa`, `/aaa/bbb` | `/ccc` | Yes, matches `/` prefix |
| Prefix | `/aaa` | `/ccc` | No, uses default backend |
| Mixed | `/foo` (Prefix), `/foo` (Exact) | `/foo` | Yes, prefers Exact |

#### Multiple matches

In some cases, multiple paths within an Ingress will match a request. In those
cases precedence will be given first to the longest matching path. If two paths
are still equally matched, precedence will be given to paths with an exact path
type over prefix path type.