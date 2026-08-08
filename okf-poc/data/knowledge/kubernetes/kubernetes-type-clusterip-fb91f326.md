---
id: kubernetes-type-clusterip-fb91f326
type: concept
title: '`type: ClusterIP`'
description: This default Service type assigns an IP address from a pool of IP addresses
  that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### `type: ClusterIP`

This default Service type assigns an IP address from a pool of IP addresses that
your cluster has reserved for that purpose.

Several of the other types for Service build on the `ClusterIP` type as a
foundation.

If you define a Service that has the `.spec.clusterIP` set to `"None"` then
Kubernetes does not assign an IP address. See [headless Services](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services)
for more information.

#### Choosing your own IP address

You can specify your own cluster IP address as part of a `Service` creation
request. To do this, set the `.spec.clusterIP` field. For example, if you
already have an existing DNS entry that you wish to reuse, or legacy systems
that are configured for a specific IP address and difficult to re-configure.

The IP address that you choose must be a valid IPv4 or IPv6 address from within the
`service-cluster-ip-range` CIDR range that is configured for the API server.
If you try to create a Service with an invalid `clusterIP` address value, the API
server will return a 422 HTTP status code to indicate that there's a problem.

Read [avoiding collisions](https://kubernetes.io/docs/reference/networking/virtual-ips/#avoiding-collisions)
to learn how Kubernetes helps reduce the risk and impact of two different Services
both trying to use the same IP address.