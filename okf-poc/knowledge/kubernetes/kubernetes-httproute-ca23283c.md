---
id: kubernetes-httproute-ca23283c
type: concept
title: HTTPRoute
description: The HTTPRoute kind specifies routing behavior of HTTP requests from a
  Gateway listener to backend network
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### HTTPRoute

The HTTPRoute kind specifies routing behavior of HTTP requests from a Gateway listener to backend network
endpoints. For a Service backend, an implementation may represent the backend network endpoint as a Service
IP or the backing EndpointSlices of the Service. An HTTPRoute represents configuration that is applied to the
underlying Gateway implementation. For example, defining a new HTTPRoute may result in configuring additional
traffic routes in a cloud load balancer or in-cluster proxy server.

A typical HTTPRoute example:

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: example-httproute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "www.example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /login
    backendRefs:
    - name: example-svc
      port: 8080
```

In this example, HTTP traffic from Gateway `example-gateway` with the Host: header set to `www.example.com`
and the request path specified as `/login` will be routed to Service `example-svc` on port `8080`.

See the [HTTPRoute](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.HTTPRoute)
reference for a full definition of this API kind.