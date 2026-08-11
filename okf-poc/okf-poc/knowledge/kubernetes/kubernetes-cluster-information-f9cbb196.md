---
id: kubernetes-cluster-information-f9cbb196
type: concept
title: Cluster information
description: A list of all services that were running when a Container was created
  is available to that Container as environment variables.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/container-environment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Cluster information

A list of all services that were running when a Container was created is available to that Container as environment variables.
This list is limited to services within the same namespace as the new Container's Pod and Kubernetes control plane services.

For a service named *foo* that exposes a set of Pods, each running a container named *bar*,
the following variables are defined:

```
FOO_SERVICE_HOST=<the host the service is running on>
FOO_SERVICE_PORT=<the port the service is running on>
```

Services have dedicated IP addresses and are available to the Container via DNS,
if [DNS addon](https://releases.k8s.io/v1.36.0/cluster/addons/dns/) is enabled.