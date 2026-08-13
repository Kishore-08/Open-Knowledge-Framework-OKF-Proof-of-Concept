---
id: kubernetes-resource-model-ca23283c
type: concept
title: Resource model
description: 'Gateway API has four stable API kinds:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Resource model

Gateway API has four stable API kinds:

- **GatewayClass:** Defines a set of gateways with common configuration and managed by a controller
  that implements the class.
- **Gateway:** Defines an instance of traffic handling infrastructure, such as cloud load balancer.
- **HTTPRoute:** Defines HTTP-specific rules for mapping traffic from a Gateway listener to a
  representation of backend network endpoints. These endpoints are often represented as a
  [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.").
- **GRPCRoute:** Defines gRPC-specific rules for mapping traffic from a Gateway listener to a
  representation of backend network endpoints. These endpoints are often represented as a
  [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.").

Gateway API is organized into different API kinds that have interdependent relationships to support
the role-oriented nature of organizations. A Gateway object is associated with exactly one GatewayClass;
the GatewayClass describes the gateway controller responsible for managing Gateways of this class.
One or more route kinds such as HTTPRoute, are then associated to Gateways. A Gateway can filter the routes
that may be attached to its `listeners`, forming a bidirectional trust model with routes.

The following figure illustrates the relationships of the three stable Gateway API kinds:

![A figure illustrating the relationships of the three stable Gateway API kinds](https://kubernetes.io/docs/images/gateway-kind-relationships.svg)