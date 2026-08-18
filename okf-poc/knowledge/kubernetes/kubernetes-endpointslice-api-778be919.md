---
id: kubernetes-endpointslice-api-778be919
type: concept
title: EndpointSlice API
description: In Kubernetes, an EndpointSlice contains references to a set of network
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## EndpointSlice API

In Kubernetes, an EndpointSlice contains references to a set of network
endpoints. The control plane automatically creates EndpointSlices
for any Kubernetes Service that has a [selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.") specified. These EndpointSlices include
references to all the Pods that match the Service selector. EndpointSlices group
network endpoints together by unique combinations of IP family, protocol,
port number, and Service name.
The name of a EndpointSlice object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

As an example, here's a sample EndpointSlice object, that's owned by the `example`
Kubernetes Service.

```
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: example-abc
  labels:
    kubernetes.io/service-name: example
addressType: IPv4
ports:
  - name: http
    protocol: TCP
    port: 80
endpoints:
  - addresses:
      - "10.1.2.3"
    conditions:
      ready: true
    hostname: pod-1
    nodeName: node-1
    zone: us-west2-a
```

By default, the control plane creates and manages EndpointSlices to have no
more than 100 endpoints each. You can configure this with the
`--max-endpoints-per-slice`
[kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/ "Control Plane component that runs controller processes.")
flag, up to a maximum of 1000.

EndpointSlices act as the source of truth for
[kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.") when it comes to
how to route internal traffic.