---
id: kubernetes-the-ingress-resource-d8c8df3b
type: concept
title: The Ingress resource
description: 'A minimal Ingress resource example:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## The Ingress resource

A minimal Ingress resource example:

[`service/networking/minimal-ingress.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/minimal-ingress.yaml)![](https://kubernetes.io/images/copycode.svg "Copy service/networking/minimal-ingress.yaml to clipboard")

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minimal-ingress
spec:
  ingressClassName: nginx-example
  rules:
  - http:
      paths:
      - path: /testpath
        pathType: Prefix
        backend:
          service:
            name: test
            port:
              number: 80
```

An Ingress needs `apiVersion`, `kind`, `metadata` and `spec` fields.
The name of an Ingress object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).
For general information about working with config files, see
[deploying applications](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/),
[configuring containers](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/),
[managing resources](https://kubernetes.io/docs/concepts/workloads/management/).
Ingress controllers frequently use [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) to configure behavior.
Review the documentation for your choice of ingress controller to learn which annotations are expected and / or supported.

The [Ingress spec](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/ingress-v1/#IngressSpec)
has all the information needed to configure a load balancer or proxy server. Most importantly, it
contains a list of rules matched against all incoming requests. Ingress resource only supports rules
for directing HTTP(S) traffic.

If the `ingressClassName` is omitted, a [default Ingress class](https://kubernetes.io/docs/concepts/services-networking/ingress/#default-ingress-class)
should be defined.

Some ingress controllers work even without the definition of a
default IngressClass. Even if you use an ingress controller that is able
to operate without any IngressClass, the Kubernetes project still recommends
that you define a default IngressClass.