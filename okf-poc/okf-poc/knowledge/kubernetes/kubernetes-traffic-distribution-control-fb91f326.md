---
id: kubernetes-traffic-distribution-control-fb91f326
type: concept
title: Traffic distribution control
description: The `.spec.trafficDistribution` field provides another way to influence
  traffic
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Traffic distribution control

The `.spec.trafficDistribution` field provides another way to influence traffic
routing within a Kubernetes Service. While traffic policies focus on strict
semantic guarantees, traffic distribution allows you to express *preferences*
(such as routing to topologically closer endpoints). This can help optimize for
performance, cost, or reliability. In Kubernetes 1.36, the
following values are supported:

`PreferSameZone`
:   Indicates a preference for routing traffic to endpoints that are in the same
    zone as the client.

`PreferSameNode`
:   Indicates a preference for routing traffic to endpoints that are on the same
    node as the client.

`PreferClose` (deprecated)
:   This is an older alias for `PreferSameZone` that is less clear about
    the semantics.

If the field is not set, the implementation will apply its default routing strategy.

See [Traffic
Distribution](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution) for
more details