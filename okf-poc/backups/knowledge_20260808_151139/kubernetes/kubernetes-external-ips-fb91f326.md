---
id: kubernetes-external-ips-fb91f326
type: concept
title: External IPs
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## External IPs

FEATURE STATE:
`Kubernetes v1.36 [deprecated]`

All users should begin migrating away from `externalIPs`.
Consider using an external load balancer controller or a Gateway API
implementation instead.

If there are external IPs that route to one or more cluster nodes, Kubernetes Services
can be exposed on those `externalIPs`. When network traffic arrives into the cluster, with
the external IP (as destination IP) and the port matching that Service, rules and routes
that Kubernetes has configured ensure that the traffic is routed to one of the endpoints
for that Service.

When you define a Service, you can specify `externalIPs` for any
[service type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types).
In the example below, the Service named `"my-service"` can be accessed by clients using TCP,
on `"198.51.100.32:80"` (calculated from `.spec.externalIPs[]` and `.spec.ports[].port`).

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 49152
  externalIPs:
    - 198.51.100.32
```

#### Note:

Kubernetes does not manage allocation of `externalIPs`; these are the responsibility
of the cluster administrator.