---
id: kubernetes-type-loadbalancer-fb91f326
type: concept
title: '`type: LoadBalancer`'
description: On cloud providers which support external load balancers, setting the
  `type`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### `type: LoadBalancer`

On cloud providers which support external load balancers, setting the `type`
field to `LoadBalancer` provisions a load balancer for your Service.
The actual creation of the load balancer happens asynchronously, and
information about the provisioned balancer is published in the Service's
`.status.loadBalancer` field.
For example:

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
  clusterIP: 10.0.171.239
  type: LoadBalancer
status:
  loadBalancer:
    ingress:
    - ip: 192.0.2.127
```

Traffic from the external load balancer is directed at the backend Pods. The cloud
provider decides how it is load balanced.

To implement a Service of `type: LoadBalancer`, Kubernetes typically starts off
by making the changes that are equivalent to you requesting a Service of
`type: NodePort`. The cloud-controller-manager component then configures the external
load balancer to forward traffic to that assigned node port.

You can configure a load balanced Service to
[omit](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation) assigning a node port, provided that the
cloud provider implementation supports this.

Some cloud providers allow you to specify the `loadBalancerIP`. In those cases, the load-balancer is created
with the user-specified `loadBalancerIP`. If the `loadBalancerIP` field is not specified,
the load balancer is set up with an ephemeral IP address. If you specify a `loadBalancerIP`
but your cloud provider does not support the feature, the `loadbalancerIP` field that you
set is ignored.

#### Note:

The`.spec.loadBalancerIP` field for a Service was deprecated in Kubernetes v1.24.

This field was under-specified and its meaning varies across implementations.
It also cannot support dual-stack networking. This field may be removed in a future API version.

If you're integrating with a provider that supports specifying the load balancer IP address(es)
for a Service via a (provider specific) annotation, you should switch to doing that.

If you are writing code for a load balancer integration with Kubernetes, avoid using this field.
You can integrate with [Gateway](https://gateway-api.sigs.k8s.io/) rather than Service, or you
can define your own (provider specific) annotations on the Service that specify the equivalent detail.

#### Node liveness impact on load balancer traffic

Load balancer health checks are critical to modern applications. They are used to
determine which server (virtual machine, or IP address) the load balancer should
dispatch traffic to. The Kubernetes APIs do not define how health checks have to be
implemented for Kubernetes managed load balancers, instead it's the cloud providers
(and the people implementing integration code) who decide on the behavior. Load
balancer health checks are extensively used within the context of supporting the
`externalTrafficPolicy` field for Services.

#### Load balancers with mixed protocol types

FEATURE STATE:
`Kubernetes v1.26 [stable]`(enabled by default)

By default, for LoadBalancer type of Services, when there is more than one port defined, all
ports must have the same protocol, and the protocol must be one which is supported
by the cloud provider.

The feature gate `MixedProtocolLBService` (enabled by default for the kube-apiserver as of v1.24) allows the use of
different protocols for LoadBalancer type of Services, when there is more than one port defined.

#### Note:

The set of protocols that can be used for load balanced Services is defined by your
cloud provider; they may impose restrictions beyond what the Kubernetes API enforces.

#### Disabling load balancer NodePort allocation

FEATURE STATE:
`Kubernetes v1.24 [stable]`

You can optionally disable node port allocation for a Service of `type: LoadBalancer`, by setting
the field `spec.allocateLoadBalancerNodePorts` t