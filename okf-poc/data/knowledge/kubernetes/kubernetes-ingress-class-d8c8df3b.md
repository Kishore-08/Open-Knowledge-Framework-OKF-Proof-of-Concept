---
id: kubernetes-ingress-class-d8c8df3b
type: concept
title: Ingress class
description: Ingresses can be implemented by different controllers, often with different
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Ingress class

Ingresses can be implemented by different controllers, often with different
configuration. Each Ingress should specify a class, a reference to an
IngressClass resource that contains additional configuration including the name
of the controller that should implement the class.

[`service/networking/external-lb.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/external-lb.yaml)![](https://kubernetes.io/images/copycode.svg "Copy service/networking/external-lb.yaml to clipboard")

```
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb
spec:
  controller: example.com/ingress-controller
  parameters:
    apiGroup: k8s.example.com
    kind: IngressParameters
    name: external-lb
```

The `.spec.parameters` field of an IngressClass lets you reference another
resource that provides configuration related to that IngressClass.

The specific type of parameters to use depends on the ingress controller
that you specify in the `.spec.controller` field of the IngressClass.