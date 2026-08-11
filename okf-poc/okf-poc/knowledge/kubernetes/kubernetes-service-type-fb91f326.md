---
id: kubernetes-service-type-fb91f326
type: concept
title: Service type
description: For some parts of your application (for example, frontends) you may want
  to expose a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Service type

For some parts of your application (for example, frontends) you may want to expose a
Service onto an external IP address, one that's accessible from outside of your
cluster.

Kubernetes Service types allow you to specify what kind of Service you want.

The available `type` values and their behaviors are:

[`ClusterIP`](https://kubernetes.io/docs/concepts/services-networking/service/#type-clusterip)
:   Exposes the Service on a cluster-internal IP. Choosing this value
    makes the Service only reachable from within the cluster. This is the
    default that is used if you don't explicitly specify a `type` for a Service.
    You can expose the Service to the public internet using an
    [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) or a
    [Gateway](https://gateway-api.sigs.k8s.io/).

[`NodePort`](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport)
:   Exposes the Service on each Node's IP at a static port (the `NodePort`).
    To make the node port available, Kubernetes sets up a cluster IP address,
    the same as if you had requested a Service of `type: ClusterIP`.

[`LoadBalancer`](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)
:   Exposes the Service externally using an external load balancer. Kubernetes
    does not directly offer a load balancing component; you must provide one, or
    you can integrate your Kubernetes cluster with a cloud provider.

[`ExternalName`](https://kubernetes.io/docs/concepts/services-networking/service/#externalname)
:   Maps the Service to the contents of the `externalName` field (for example,
    to the hostname `api.foo.bar.example`). The mapping configures your cluster's
    DNS server to return a `CNAME` record with that external hostname value.
    No proxying of any kind is set up.

The `type` field in the Service API is designed as nested functionality - each level
adds to the previous. However there is an exception to this nested design. You can
define a `LoadBalancer` Service by
[disabling the load balancer `NodePort` allocation](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation).