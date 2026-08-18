---
id: kubernetes-gateway-ca23283c
type: concept
title: Gateway
description: A Gateway describes an instance of traffic handling infrastructure. It
  defines a network endpoint
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Gateway

A Gateway describes an instance of traffic handling infrastructure. It defines a network endpoint
that can be used for processing traffic, i.e. filtering, balancing, splitting, etc. for backends
such as a Service. For example, a Gateway may represent a cloud load balancer or an in-cluster proxy
server that is configured to accept HTTP traffic.

A typical Gateway resource example:

```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
  namespace: example-namespace
spec:
  gatewayClassName: example-class
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    hostname: "www.example.com"
    allowedRoutes:
      namespaces:
        from: Same
```

In this example, an instance of traffic handling infrastructure is programmed to listen for HTTP
traffic on port 80. Since the `addresses` field is unspecified, an address or hostname is assigned
to the Gateway by the implementation's controller. This address is used as a network endpoint for
processing traffic of backend network endpoints defined in routes.

See the [Gateway](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.Gateway)
reference for a full definition of this API kind. For guidance on configuring HTTPS/TLS listeners, see the
[Gateway API TLS Guide](https://gateway-api.sigs.k8s.io/guides/tls/).

#### Note:

By default, a Gateway only accepts Routes from the same namespace. Cross-namespace Routes require configuring `allowedRoutes`.