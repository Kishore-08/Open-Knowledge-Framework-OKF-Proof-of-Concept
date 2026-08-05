---
id: k8s-service
type: concept
title: Kubernetes Service
description: Stable network endpoint for a set of Pods
category: kubernetes
tags: [service, networking, load-balancing, discovery, selector]
source:
  name: Kubernetes Documentation
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: 2026-08-05
created_at: 2026-08-05
aliases: [Service, Services]
related: [k8s-pod, k8s-deployment]
---

## Service

In Kubernetes, a Service is a method for exposing a network application that is
running as one or more Pods in your cluster. It gives Pods a stable virtual IP and
DNS name so clients do not need to track individual Pod IPs (which change when
Pods are recreated).

## Service Types

- **ClusterIP**: exposes the Service on a cluster-internal IP. Default type.
- **NodePort**: exposes the Service on each node's IP at a static port.
- **LoadBalancer**: provisions an external load balancer that routes to the Service.
- **ExternalName**: maps the Service to the contents of an external DNS name.

## Defining a Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
```

The Service routes traffic to Pods that match the `selector` labels. For the
`port`/`targetPort` pair, `port` is the port this Service exposes, and `targetPort`
is the port on the Pod the traffic is forwarded to.

## Selecting Pods

The Service's `spec.selector` selects Pods by label. If no selector matches, the
Service has no endpoints. You can also use endpoint slices to map a Service to
Pods that do not match a label selector.

## Multi-Port Services

For Services with multiple ports you must give each port a `name` so that
`endpoints` objects map ports unambiguously. Names can contain lowercase
alphanumeric characters and `-`, and must be unique per Service.

## Publishing Services

- **NodePort** allocates a port in the configured `--service-node-port-range`
  (default 30000-32767).
- **LoadBalancer** services build on NodePort and additionally provision an
  external load balancer from the cloud provider.

## Service Discovery

Pods are given their own DNS records. A headless Service (with `clusterIP: None`)
lets clients discover the Pod IPs behind it directly via DNS.
