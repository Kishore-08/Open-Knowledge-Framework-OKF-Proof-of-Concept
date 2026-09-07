---
id: kubernetes-namespaces-and-dns-0663647e
type: concept
title: Namespaces and DNS
description: When you create a [Service](https://kubernetes.io/docs/concepts/services-networking/service/),
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Namespaces and DNS

When you create a [Service](https://kubernetes.io/docs/concepts/services-networking/service/),
it creates a corresponding [DNS entry](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).
This entry is of the form `<service-name>.<namespace-name>.svc.cluster.local`, which means
that if a container only uses `<service-name>`, it will resolve to the service which
is local to a namespace. This is useful for using the same configuration across
multiple namespaces such as Development, Staging and Production. If you want to reach
across namespaces, you need to use the fully qualified domain name (FQDN).

As a result, all namespace names must be valid
[RFC 1123 DNS labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).

#### Warning:

By creating namespaces with the same name as [public top-level
domains](https://data.iana.org/TLD/tlds-alpha-by-domain.txt), Services in these
namespaces can have short DNS names that overlap with public DNS records.
Workloads from any namespace performing a DNS lookup without a [trailing dot](https://datatracker.ietf.org/doc/html/rfc1034#page-8) will
be redirected to those services, taking precedence over public DNS.

To mitigate this, limit privileges for creating namespaces to trusted users. If
required, you could additionally configure third-party security controls, such
as [admission
webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/),
to block creating any namespace with the name of [public
TLDs](https://data.iana.org/TLD/tlds-alpha-by-domain.txt).