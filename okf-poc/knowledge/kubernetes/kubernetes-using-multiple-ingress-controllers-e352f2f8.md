---
id: kubernetes-using-multiple-ingress-controllers-e352f2f8
type: concept
title: Using multiple Ingress controllers
description: You may deploy any number of ingress controllers using [ingress class](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-class)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Using multiple Ingress controllers

You may deploy any number of ingress controllers using [ingress class](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-class)
within a cluster. Note the `.metadata.name` of your ingress class resource. When you create an ingress you would need that name to specify the `ingressClassName` field on your Ingress object (refer to [IngressSpec v1 reference](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/#IngressSpec)). `ingressClassName` is a replacement of the older [annotation method](https://kubernetes.io/docs/concepts/services-networking/ingress/#deprecated-annotation).

If you do not specify an IngressClass for an Ingress, and your cluster has exactly one IngressClass marked as default, then Kubernetes [applies](https://kubernetes.io/docs/concepts/services-networking/ingress/#default-ingress-class) the cluster's default IngressClass to the Ingress.
You mark an IngressClass as default by setting the [`ingressclass.kubernetes.io/is-default-class` annotation](https://kubernetes.io/docs/reference/labels-annotations-taints/#ingressclass-kubernetes-io-is-default-class) on that IngressClass, with the string value `"true"`.

Ideally, all ingress controllers should fulfill this specification, but the various ingress
controllers operate slightly differently.

#### Note:

Make sure you review your ingress controller's documentation to understand the caveats of choosing it.

## What's next

- Learn more about [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/).