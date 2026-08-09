---
id: kubernetes-what-is-ingress-d8c8df3b
type: concept
title: What is Ingress?
description: '[Ingress](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#ingress-v1-networking-k8s-io)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## What is Ingress?

[Ingress](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#ingress-v1-networking-k8s-io)
exposes HTTP and HTTPS routes from outside the cluster to
[services](https://kubernetes.io/docs/concepts/services-networking/service/) within the cluster.
Traffic routing is controlled by rules defined on the Ingress resource.

Here is a simple example where an Ingress sends all its traffic to one Service:

[![ingress-diagram](https://kubernetes.io/docs/images/ingress.svg)](https://mermaid.live/edit#pako:eNqNkstuwyAQRX8F4U0r2VHqPlSRKqt0UamLqlnaWWAYJygYLB59KMm_Fxcix-qmGwbuXA7DwAEzzQETXKutof0Ovb4vaoUQkwKUu6pi3FwXM_QSHGBt0VFFt8DRU2OWSGrKUUMlVQwMmhVLEV1Vcm9-aUksiuXRaO_CEhkv4WjBfAgG1TrGaLa-iaUw6a0DcwGI-WgOsF7zm-pN881fvRx1UDzeiFq7ghb1kgqFWiElyTjnuXVG74FkbdumefEpuNuRu_4rZ1pqQ7L5fL6YQPaPNiFuywcG9_-ihNyUkm6YSONWkjVNM8WUIyaeOJLO3clTB_KhL8NQDmVe-OJjxgZM5FhFiiFTK5zjDkxHBQ9_4zB4a-x20EGNSZhyaKmXrg7f5hSsvufUwTMXThtMWiot5Jh6p9ffimHijIezaSVoeN0uiqcfMJvf7w)

Figure. Ingress

An Ingress may be configured to give Services externally-reachable URLs,
load balance traffic, terminate SSL / TLS, and offer name-based virtual hosting.
An [Ingress controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/)
is responsible for fulfilling the Ingress, usually with a load balancer, though
it may also configure your edge router or additional frontends to help handle the traffic.

An Ingress does not expose arbitrary ports or protocols. Exposing services other than HTTP and HTTPS to the internet typically
uses a service of type [Service.Type=NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport) or
[Service.Type=LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer).