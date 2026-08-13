---
id: kubernetes-huge-pages-d3611dbe
type: concept
title: Huge pages
description: For Linux workloads, you can specify *huge page* resources.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Huge pages

For Linux workloads, you can specify *huge page* resources.
Huge pages are a Linux-specific feature where the node kernel allocates blocks of memory
that are much larger than the default page size.

For example, on a system where the default page size is 4KiB, you could specify a limit,
`hugepages-2Mi: 80Mi`. If the container tries allocating over 40 2MiB huge pages (a
total of 80 MiB), that allocation fails.

#### Note:

You cannot overcommit `hugepages-*` resources.
This is different from the `memory` and `cpu` resources.

CPU and memory are collectively referred to as *compute resources*, or *resources*. Compute
resources are measurable quantities that can be requested, allocated, and
consumed. They are distinct from
[API resources](https://kubernetes.io/docs/concepts/overview/kubernetes-api/). API resources, such as Pods and
[Services](https://kubernetes.io/docs/concepts/services-networking/service/) are objects that can be read and modified
through the Kubernetes API server.