---
id: kubernetes-services-without-selectors-fb91f326
type: concept
title: Services without selectors
description: Services most commonly abstract access to Kubernetes Pods thanks to the
  selector,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Services without selectors

Services most commonly abstract access to Kubernetes Pods thanks to the selector,
but when used with a corresponding set of
[EndpointSlices](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/ "EndpointSlices track the IP addresses of Pods for Services.")
objects and without a selector, the Service can abstract other kinds of backends,
including ones that run outside the cluster.

For example:

- You want to have an external database cluster in production, but in your
  test environment you use your own databases.
- You want to point your Service to a Service in a different
  [Namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces "An abstraction used by Kubernetes to support isolation of groups of resources within a single cluster.") or on another cluster.
- You are migrating a workload to Kubernetes. While evaluating the approach,
  you run only a portion of your backends in Kubernetes.

In any of these scenarios you can define a Service *without* specifying a
selector to match Pods. For example:

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
```

Because this Service has no selector, the corresponding EndpointSlice
objects are not created automatically. You can map the Service
to the network address and port where it's running, by adding an EndpointSlice
object manually. For example:

```
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: my-service-1 # by convention, use the name of the Service
                     # as a prefix for the name of the EndpointSlice
  labels:
    # You should set the "kubernetes.io/service-name" label.
    # Set its value to match the name of the Service
    kubernetes.io/service-name: my-service
addressType: IPv4
ports:
  - name: http # should match with the name of the service port defined above
    appProtocol: http
    protocol: TCP
    port: 9376
endpoints:
  - addresses:
      - "10.4.5.6"
  - addresses:
      - "10.1.2.3"
```

#### Custom EndpointSlices

When you create an [EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/service/#endpointslices) object for a Service, you can
use any name for the EndpointSlice. Each EndpointSlice in a namespace must have a
unique name. You link an EndpointSlice to a Service by setting the
`kubernetes.io/service-name` [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.")
on that EndpointSlice.

#### Note:

The endpoint IPs *must not* be: loopback (127.0.0.0/8 for IPv4, ::1/128 for IPv6), or
link-local (169.254.0.0/16 and 224.0.0.0/24 for IPv4, fe80::/64 for IPv6).

The endpoint IP addresses cannot be the cluster IPs of other Kubernetes Services,
because [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.") doesn't support virtual IPs
as a destination.

For an EndpointSlice that you create yourself, or in your own code,
you should also pick a value to use for the label
[`endpointslice.kubernetes.io/managed-by`](https://kubernetes.io/docs/reference/labels-annotations-taints/#endpointslicekubernetesiomanaged-by).
If you create your own controller code to manage EndpointSlices, consider using a
value similar to `"my-domain.example/name-of-controller"`. If you are using a third
party tool, use the name of the tool in all-lowercase and change spaces and other
punctuation to dashes (`-`).
If people are directly using a tool such as `kubectl` to manage EndpointSlices,
use a name that describes this manual management, such as `"staff"` or
`"cluster-admins"`. You should
avoid using the reserved value `"controller"`, which identifies EndpointSlices
managed by Kubernetes' own control plane.

#### Accessing a Service wi