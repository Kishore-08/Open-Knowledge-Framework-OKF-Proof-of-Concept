---
id: kubernetes-with-selectors-fb91f326
type: concept
title: With selectors
description: For headless Services that define selectors, the endpoints controller
  creates
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### With selectors

For headless Services that define selectors, the endpoints controller creates
EndpointSlices in the Kubernetes API, and modifies the DNS configuration to return
A or AAAA records (IPv4 or IPv6 addresses) that point directly to the Pods backing the Service.