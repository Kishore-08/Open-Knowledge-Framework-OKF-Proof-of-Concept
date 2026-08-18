---
id: kubernetes-endpointslice-mirroring-778be919
type: concept
title: EndpointSlice mirroring
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### EndpointSlice mirroring

FEATURE STATE:
`Kubernetes v1.33 [deprecated]`

The EndpointSlice API is a replacement for the older Endpoints API. To
preserve compatibility with older controllers and user workloads that
expect [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ "kube-proxy is a network proxy that runs on each node in the cluster.")
to route traffic based on Endpoints resources, the cluster's control
plane mirrors most user-created Endpoints resources to corresponding
EndpointSlices.

(However, this feature, like the rest of the Endpoints API, is
deprecated. Users who manually specify endpoints for selectorless
Services should do so by creating EndpointSlice resources directly,
rather than by creating Endpoints resources and allowing them to be
mirrored.)

The control plane mirrors Endpoints resources unless:

- the Endpoints resource has a `endpointslice.kubernetes.io/skip-mirror` label
  set to `true`.
- the Endpoints resource has a `control-plane.alpha.kubernetes.io/leader`
  annotation.
- the corresponding Service resource does not exist.
- the corresponding Service resource has a non-nil selector.

Individual Endpoints resources may translate into multiple EndpointSlices. This
will occur if an Endpoints resource has multiple subsets or includes endpoints
with multiple IP families (IPv4 and IPv6). A maximum of 1000 addresses per
subset will be mirrored to EndpointSlices.