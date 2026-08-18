---
id: kubernetes-gatewayclass-ca23283c
type: concept
title: GatewayClass
description: Gateways can be implemented by different controllers, often with different
  configurations. A Gateway
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### GatewayClass

Gateways can be implemented by different controllers, often with different configurations. A Gateway
must reference a GatewayClass that contains the name of the controller that implements the
class.

A minimal GatewayClass example:

```
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: example-class
spec:
  controllerName: example.com/gateway-controller
```

In this example, a controller that has implemented Gateway API is configured to manage GatewayClasses
with the controller name `example.com/gateway-controller`. Gateways of this class will be managed by
the implementation's controller.

See the [GatewayClass](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.GatewayClass)
reference for a full definition of this API kind.