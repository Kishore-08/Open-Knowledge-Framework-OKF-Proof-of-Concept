---
id: kubernetes-management-778be919
type: concept
title: Management
description: Most often, the control plane (specifically, the endpoint slice
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Management

Most often, the control plane (specifically, the endpoint slice
[controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")) creates and
manages EndpointSlice objects. There are a variety of other use cases for
EndpointSlices, such as service mesh implementations, that could result in other
entities or controllers managing additional sets of EndpointSlices.

To ensure that multiple entities can manage EndpointSlices without interfering
with each other, Kubernetes defines the
[label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.")
`endpointslice.kubernetes.io/managed-by`, which indicates the entity managing
an EndpointSlice.
The endpoint slice controller sets `endpointslice-controller.k8s.io` as the value
for this label on all EndpointSlices it manages. Other entities managing
EndpointSlices should also set a unique value for this label.