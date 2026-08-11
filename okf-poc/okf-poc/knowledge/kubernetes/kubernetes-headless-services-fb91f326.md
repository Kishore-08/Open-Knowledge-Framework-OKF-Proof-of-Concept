---
id: kubernetes-headless-services-fb91f326
type: concept
title: Headless Services
description: Sometimes you don't need load-balancing and a single Service IP. In
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Headless Services

Sometimes you don't need load-balancing and a single Service IP. In
this case, you can create what are termed *headless Services*, by explicitly
specifying `"None"` for the cluster IP address (`.spec.clusterIP`).

You can use a headless Service to interface with other service discovery mechanisms,
without being tied to Kubernetes' implementation.

For headless Services, a cluster IP is not allocated, kube-proxy does not handle
these Services, and there is no load balancing or proxying done by the platform for them.

A headless Service allows a client to connect to whichever Pod it prefers, directly. Services that are headless don't
configure routes and packet forwarding using
[virtual IP addresses and proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/); instead, headless Services report the
endpoint IP addresses of the individual pods via internal DNS records, served through the cluster's
[DNS service](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).
To define a headless Service, you make a Service with `.spec.type` set to ClusterIP (which is also the default for `type`),
and you additionally set `.spec.clusterIP` to None.

The string value None is a special case and is not the same as leaving the `.spec.clusterIP` field unset.

How DNS is automatically configured depends on whether the Service has selectors defined: