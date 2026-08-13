---
id: kubernetes-openapi-v3-0b6c673c
type: concept
title: OpenAPI V3
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### OpenAPI V3

FEATURE STATE:
`Kubernetes v1.27 [stable]`(enabled by default)

Kubernetes supports publishing a description of its APIs as OpenAPI v3.

A discovery endpoint `/openapi/v3` is provided to see a list of all
group/versions available. This endpoint only returns JSON. These
group/versions are provided in the following format:

```
{
    "paths": {
        ...,
        "api/v1": {
            "serverRelativeURL": "/openapi/v3/api/v1?hash=CC0E9BFD992D8C59AEC98A1E2336F899E8318D3CF4C68944C3DEC640AF5AB52D864AC50DAA8D145B3494F75FA3CFF939FCBDDA431DAD3CA79738B297795818CF"
        },
        "apis/admissionregistration.k8s.io/v1": {
            "serverRelativeURL": "/openapi/v3/apis/admissionregistration.k8s.io/v1?hash=E19CC93A116982CE5422FC42B590A8AFAD92CDE9AE4D59B5CAAD568F083AD07946E6CB5817531680BCE6E215C16973CD39003B0425F3477CFD854E89A9DB6597"
        },
        ....
    }
}
```

The relative URLs are pointing to immutable OpenAPI descriptions, in
order to improve client-side caching. The proper HTTP caching headers
are also set by the API server for that purpose (`Expires` to 1 year in
the future, and `Cache-Control` to `immutable`). When an obsolete URL is
used, the API server returns a redirect to the newest URL.

The Kubernetes API server publishes an OpenAPI v3 spec per Kubernetes
group version at the `/openapi/v3/apis/<group>/<version>?hash=<hash>`
endpoint.

Refer to the table below for accepted request headers.

Valid request header values for OpenAPI v3 queries

| Header | Possible values | Notes |
| --- | --- | --- |
| `Accept-Encoding` | `gzip` | *not supplying this header is also acceptable* |
| `Accept` | `application/com.github.proto-openapi.spec.v3@v1.0+protobuf` | *mainly for intra-cluster use* |
| `application/json` | *default* |
| `*` | *serves* `application/json` |

A Golang implementation to fetch the OpenAPI V3 is provided in the package
[`k8s.io/client-go/openapi3`](https://pkg.go.dev/k8s.io/client-go/openapi3).

Kubernetes 1.36 publishes
OpenAPI v2.0 and v3.0; there are no plans to support 3.1 in the near future.