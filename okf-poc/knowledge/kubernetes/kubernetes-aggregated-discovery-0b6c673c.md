---
id: kubernetes-aggregated-discovery-0b6c673c
type: concept
title: Aggregated discovery
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Aggregated discovery

FEATURE STATE:
`Kubernetes v1.30 [stable]`(enabled by default)

Kubernetes offers stable support for *aggregated discovery*, publishing
all resources supported by a cluster through two endpoints (`/api` and
`/apis`). Requesting this
endpoint drastically reduces the number of requests sent to fetch the
discovery data from the cluster. You can access the data by
requesting the respective endpoints with an `Accept` header indicating
the aggregated discovery resource:
`Accept: application/json;v=v2;g=apidiscovery.k8s.io;as=APIGroupDiscoveryList`.

Without indicating the resource type using the `Accept` header, the default
response for the `/api` and `/apis` endpoint is an unaggregated discovery
document.

The [discovery document](https://github.com/kubernetes/kubernetes/blob/release-1.36/api/discovery/aggregated_v2.json)
for the built-in resources can be found in the Kubernetes GitHub repository.
This Github document can be used as a reference of the base set of the available resources
if a Kubernetes cluster is not available to query.

The endpoint also supports ETag and protobuf encoding.