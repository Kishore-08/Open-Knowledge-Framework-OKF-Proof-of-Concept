---
id: kubernetes-downwardapi-4142258a
type: concept
title: downwardAPI
description: A `downwardAPI` volume makes [downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/
  "A mechanism to expose Pod and container field values to code running in a container.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### downwardAPI

A `downwardAPI` volume makes [downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/ "A mechanism to expose Pod and container field values to code running in a container.")
data available to applications. Within the volume, you can find the exposed
data as read-only files in plain text format.

#### Note:

A container using the downward API as a [`subPath`](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) volume mount does not
receive updates when field values change.

See [Expose Pod Information to Containers Through Files](https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)
to learn more.