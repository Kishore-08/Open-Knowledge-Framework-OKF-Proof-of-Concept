---
id: kubernetes-ingress-backed-by-a-single-service-d8c8df3b
type: concept
title: Ingress backed by a single Service
description: There are existing Kubernetes concepts that allow you to expose a single
  Service
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Ingress backed by a single Service

There are existing Kubernetes concepts that allow you to expose a single Service
(see [alternatives](https://kubernetes.io/docs/concepts/services-networking/ingress/#alternatives)). You can also do this with an Ingress by specifying a
*default backend* with no rules.

[`service/networking/test-ingress.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/test-ingress.yaml)![](https://kubernetes.io/images/copycode.svg "Copy service/networking/test-ingress.yaml to clipboard")

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: test-ingress
spec:
  defaultBackend:
    service:
      name: test
      port:
        number: 80
```

If you create it using `kubectl apply -f` you should be able to view the state
of the Ingress you added:

```
kubectl get ingress test-ingress
```

```
NAME           CLASS         HOSTS   ADDRESS         PORTS   AGE
test-ingress   external-lb   *       203.0.113.123   80      59s
```

Where `203.0.113.123` is the IP allocated by the Ingress controller to satisfy
this Ingress.

#### Note:

Ingress controllers and load balancers may take a minute or two to allocate an IP address.
Until that time, you often see the address listed as `<pending>`.