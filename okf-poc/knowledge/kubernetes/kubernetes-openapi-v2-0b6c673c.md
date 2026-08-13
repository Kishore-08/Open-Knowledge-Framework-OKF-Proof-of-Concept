---
id: kubernetes-openapi-v2-0b6c673c
type: concept
title: OpenAPI V2
description: The Kubernetes API server serves an aggregated OpenAPI v2 spec via the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### OpenAPI V2

The Kubernetes API server serves an aggregated OpenAPI v2 spec via the
`/openapi/v2` endpoint. You can request the response format using
request headers as follows:

Valid request header values for OpenAPI v2 queries

| Header | Possible values | Notes |
| --- | --- | --- |
| `Accept-Encoding` | `gzip` | *not supplying this header is also acceptable* |
| `Accept` | `application/com.github.proto-openapi.spec.v2@v1.0+protobuf` | *mainly for intra-cluster use* |
| `application/json` | *default* |
| `*` | *serves* `application/json` |

#### Warning:

The validation rules published as part of OpenAPI schemas may not be complete, and usually aren't.
Additional validation occurs within the API server. If you want precise and complete verification,
a `kubectl apply --dry-run=server` runs all the applicable validation (and also activates admission-time
checks).