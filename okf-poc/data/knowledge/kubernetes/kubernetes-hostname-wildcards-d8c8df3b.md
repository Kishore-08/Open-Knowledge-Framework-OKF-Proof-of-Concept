---
id: kubernetes-hostname-wildcards-d8c8df3b
type: concept
title: Hostname wildcards
description: Hosts can be precise matches (for example “`foo.bar.com`”) or a wildcard
  (for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Hostname wildcards

Hosts can be precise matches (for example “`foo.bar.com`”) or a wildcard (for
example “`*.foo.com`”). Precise matches require that the HTTP `host` header
matches the `host` field. Wildcard matches require the HTTP `host` header is
equal to the suffix of the wildcard rule.

| Host | Host header | Match? |
| --- | --- | --- |
| `*.foo.com` | `bar.foo.com` | Matches based on shared suffix |
| `*.foo.com` | `baz.bar.foo.com` | No match, wildcard only covers a single DNS label |
| `*.foo.com` | `foo.com` | No match, wildcard only covers a single DNS label |

[`service/networking/ingress-wildcard-host.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/ingress-wildcard-host.yaml)![](https://kubernetes.io/images/copycode.svg "Copy service/networking/ingress-wildcard-host.yaml to clipboard")

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-wildcard-host
spec:
  rules:
  - host: "foo.bar.com"
    http:
      paths:
      - pathType: Prefix
        path: "/bar"
        backend:
          service:
            name: service1
            port:
              number: 80
  - host: "*.foo.com"
    http:
      paths:
      - pathType: Prefix
        path: "/foo"
        backend:
          service:
            name: service2
            port:
              number: 80
```