---
id: kubernetes-grpcroute-ca23283c
type: concept
title: GRPCRoute
description: The GRPCRoute kind specifies routing behavior of gRPC requests from a
  Gateway listener to backend network
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### GRPCRoute

The GRPCRoute kind specifies routing behavior of gRPC requests from a Gateway listener to backend network
endpoints. For a Service backend, an implementation may represent the backend network endpoint as a Service
IP or the backing EndpointSlices of the Service. A GRPCRoute represents configuration that is applied to the
underlying Gateway implementation. For example, defining a new GRPCRoute may result in configuring additional
traffic routes in a cloud load balancer or in-cluster proxy server.

Gateways supporting GRPCRoute are required to support HTTP/2 without an initial upgrade from HTTP/1,
so gRPC traffic is guaranteed to flow properly.

A typical GRPCRoute example:

```
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: example-grpcroute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "svc.example.com"
  rules:
  - backendRefs:
    - name: example-svc
      port: 50051
```

In this example, gRPC traffic from Gateway `example-gateway` with the host set to `svc.example.com`
will be directed to the service `example-svc` on port `50051` from the same namespace.

GRPCRoute allows matching specific gRPC services, as per the following example:

```
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: example-grpcroute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "svc.example.com"
  rules:
  - matches:
    - method:
        service: com.example
        method: Login
    backendRefs:
    - name: foo-svc
      port: 50051
```

In this case, the GRPCRoute will match any traffic for svc.example.com and apply its routing rules
to forward the traffic to the correct backend. Since there is only one match specified,only requests
for the com.example.User.Login method to svc.example.com will be forwarded.
RPCs of any other method` will not be matched by this Route.

See the [GRPCRoute](https://gateway-api.sigs.k8s.io/references/spec/#grpcroute)
reference for a full definition of this API kind.