---
id: kubernetes-default-ingressclass-d8c8df3b
type: concept
title: Default IngressClass
description: You can mark a particular IngressClass as default for your cluster. Setting
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Default IngressClass

You can mark a particular IngressClass as default for your cluster. Setting the
`ingressclass.kubernetes.io/is-default-class` annotation to `true` on an
IngressClass resource will ensure that new Ingresses without an
`ingressClassName` field specified will be assigned this default IngressClass.

#### Caution:

If you have more than one IngressClass marked as the default for your cluster,
the admission controller prevents creating new Ingress objects that don't have
an `ingressClassName` specified. You can resolve this by ensuring that at most 1
IngressClass is marked as default in your cluster.

Start by defining a
default IngressClass. It is recommended though, to specify the default
IngressClass:

[`service/networking/default-ingressclass.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/default-ingressclass.yaml)![](https://kubernetes.io/images/copycode.svg "Copy service/networking/default-ingressclass.yaml to clipboard")

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  labels:
    app.kubernetes.io/component: controller
  name: example-class
  annotations:
    ingressclass.kubernetes.io/is-default-class: "true"
spec:
  controller: k8s.io/example-class
```

## Types of Ingress