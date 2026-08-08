---
id: kubernetes-traffic-policies-fb91f326
type: concept
title: Traffic policies
description: You can set the `.spec.internalTrafficPolicy` and `.spec.externalTrafficPolicy`
  fields
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Traffic policies

You can set the `.spec.internalTrafficPolicy` and `.spec.externalTrafficPolicy` fields
to control how Kubernetes routes traffic to healthy (“ready”) backends.

See [Traffic Policies](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-policies) for more details.