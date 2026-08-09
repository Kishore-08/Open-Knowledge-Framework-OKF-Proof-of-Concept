---
id: kubernetes-type-externalname-fb91f326
type: concept
title: '`type: ExternalName`'
description: Services of type ExternalName map a Service to a DNS name, not to a typical
  selector such as
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### `type: ExternalName`

Services of type ExternalName map a Service to a DNS name, not to a typical selector such as
`my-service` or `cassandra`. You specify these Services with the `spec.externalName` parameter.

This Service definition, for example, maps
the `my-service` Service in the `prod` namespace to `my.database.example.com`:

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
  namespace: prod
spec:
  type: ExternalName
  externalName: my.database.example.com
```

#### Note:

A Service of `type: ExternalName` accepts an IPv4 address string,
but treats that string as a DNS name comprised of digits,
not as an IP address (the internet does not however allow such names in DNS).
Services with external names that resemble IPv4
addresses are not resolved by DNS servers.

If you want to map a Service directly to a specific IP address, consider using
[headless Services](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services).

When looking up the host `my-service.prod.svc.cluster.local`, the cluster DNS Service
returns a `CNAME` record with the value `my.database.example.com`. Accessing
`my-service` works in the same way as other Services but with the crucial
difference that redirection happens at the DNS level rather than via proxying or
forwarding. Should you later decide to move your database into your cluster, you
can start its Pods, add appropriate selectors or endpoints, and change the
Service's `type`.

#### Caution:

You may have trouble using ExternalName for some common protocols, including HTTP and HTTPS.
If you use ExternalName then the hostname used by clients inside your cluster is different from
the name that the ExternalName references.

For protocols that use hostnames this difference may lead to errors or unexpected responses.
HTTP requests will have a `Host:` header that the origin server does not recognize;
TLS servers will not be able to provide a certificate matching the hostname that the client connected to.