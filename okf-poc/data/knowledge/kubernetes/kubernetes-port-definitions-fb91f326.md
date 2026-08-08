---
id: kubernetes-port-definitions-fb91f326
type: concept
title: Port definitions
description: Port definitions in Pods have names, and you can reference these names
  in the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Port definitions

Port definitions in Pods have names, and you can reference these names in the
`targetPort` attribute of a Service. For example, we can bind the `targetPort`
of the Service to the Pod port in the following way:

```
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app.kubernetes.io/name: proxy
  ports:
  - name: name-of-service-port
    protocol: TCP
    port: 80
    targetPort: http-web-svc

---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/name: proxy
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
      - containerPort: 80
        name: http-web-svc
```

This works even if there is a mixture of Pods in the Service using a single
configured name, with the same network protocol available via different
port numbers. This offers a lot of flexibility for deploying and evolving
your Services. For example, you can change the port numbers that Pods expose
in the next version of your backend software, without breaking clients.

The default protocol for Services is
[TCP](https://kubernetes.io/docs/reference/networking/service-protocols/#protocol-tcp); you can also
use any other [supported protocol](https://kubernetes.io/docs/reference/networking/service-protocols/).

Because many Services need to expose more than one port, Kubernetes supports
[multiple port definitions](https://kubernetes.io/docs/concepts/services-networking/service/#multi-port-services) for a single Service.
Each port definition can have the same `protocol`, or a different one.