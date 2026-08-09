---
id: kubernetes-tls-d8c8df3b
type: concept
title: TLS
description: You can secure an Ingress by specifying a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/
  "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### TLS

You can secure an Ingress by specifying a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.")
that contains a TLS private key and certificate. The Ingress resource only
supports a single TLS port, 443, and assumes TLS termination at the ingress point
(traffic to the Service and its Pods is in plaintext).
If the TLS configuration section in an Ingress specifies different hosts, they are
multiplexed on the same port according to the hostname specified through the
SNI TLS extension (provided the Ingress controller supports SNI). The TLS secret
must contain keys named `tls.crt` and `tls.key` that contain the certificate
and private key to use for TLS. For example:

```
apiVersion: v1
kind: Secret
metadata:
  name: testsecret-tls
  namespace: default
data:
  tls.crt: base64 encoded cert
  tls.key: base64 encoded key
type: kubernetes.io/tls
```

Referencing this secret in an Ingress tells the Ingress controller to
secure the channel from the client to the load balancer using TLS. You need to make
sure the TLS secret you created came from a certificate that contains a Common
Name (CN), also known as a Fully Qualified Domain Name (FQDN) for `https-example.foo.com`.

#### Note:

Keep in mind that TLS will not work on the default rule because the
certificates would have to be issued for all the possible sub-domains. Therefore,
`hosts` in the `tls` section need to explicitly match the `host` in the `rules`
section.

[`service/networking/tls-example-ingress.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/networking/tls-example-ingress.yaml)![](https://kubernetes.io/images/copycode.svg "Copy service/networking/tls-example-ingress.yaml to clipboard")

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-example-ingress
spec:
  tls:
  - hosts:
      - https-example.foo.com
    secretName: testsecret-tls
  rules:
  - host: https-example.foo.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: service1
            port:
              number: 80
```

#### Note:

There is a gap between TLS features supported by various ingress controllers.
You should refer to the documentation for the ingress controller(s) you've chosen to
understand how TLS works in your environment.