---
id: kubernetes-dns-10267ad8
type: concept
title: DNS
description: While the other addons are not strictly required, all Kubernetes clusters
  should have
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### DNS

While the other addons are not strictly required, all Kubernetes clusters should have
[cluster DNS](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/), as many examples rely on it.

Cluster DNS is a DNS server, in addition to the other DNS server(s) in your environment,
which serves DNS records for Kubernetes services.

Containers started by Kubernetes automatically include this DNS server in their DNS searches.