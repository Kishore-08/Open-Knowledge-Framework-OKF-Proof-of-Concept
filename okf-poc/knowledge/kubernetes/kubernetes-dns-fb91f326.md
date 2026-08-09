---
id: kubernetes-dns-fb91f326
type: concept
title: DNS
description: You can (and almost always should) set up a DNS service for your Kubernetes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### DNS

You can (and almost always should) set up a DNS service for your Kubernetes
cluster using an [add-on](https://kubernetes.io/docs/concepts/cluster-administration/addons/).

A cluster-aware DNS server, such as CoreDNS, watches the Kubernetes API for new
Services and creates a set of DNS records for each one. If DNS has been enabled
throughout your cluster then all Pods should automatically be able to resolve
Services by their DNS name.

For example, if you have a Service called `my-service` in a Kubernetes
namespace `my-ns`, the control plane and the DNS Service acting together
create a DNS record for `my-service.my-ns`. Pods in the `my-ns` namespace
should be able to find the service by doing a name lookup for `my-service`
(`my-service.my-ns` would also work).

Pods in other namespaces must qualify the name as `my-service.my-ns`. These names
will resolve to the cluster IP assigned for the Service.

Kubernetes also supports DNS SRV (Service) records for named ports. If the
`my-service.my-ns` Service has a port named `http` with the protocol set to
`TCP`, you can do a DNS SRV query for `_http._tcp.my-service.my-ns` to discover
the port number for `http`, as well as the IP address.

The Kubernetes DNS server is the only way to access `ExternalName` Services.
You can find more information about `ExternalName` resolution in
[DNS for Services and Pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/).