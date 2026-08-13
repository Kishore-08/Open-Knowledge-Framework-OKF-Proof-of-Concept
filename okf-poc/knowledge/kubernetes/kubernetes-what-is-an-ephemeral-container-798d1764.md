---
id: kubernetes-what-is-an-ephemeral-container-798d1764
type: concept
title: What is an ephemeral container?
description: Ephemeral containers differ from other containers in that they lack guarantees
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### What is an ephemeral container?

Ephemeral containers differ from other containers in that they lack guarantees
for resources or execution, and they will never be automatically restarted, so
they are not appropriate for building applications. Ephemeral containers are
described using the same `ContainerSpec` as regular containers, but many fields
are incompatible and disallowed for ephemeral containers.

- Ephemeral containers may not have ports, so fields such as `ports`,
  `livenessProbe`, `readinessProbe` are disallowed.
- Pod resource allocations are immutable, so setting `resources` is disallowed.
- For a complete list of allowed fields, see the [EphemeralContainer reference
  documentation](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#ephemeralcontainer-v1-core).

Ephemeral containers are created using a special `ephemeralcontainers` handler
in the API rather than by adding them directly to `pod.spec`, so it's not
possible to add an ephemeral container using `kubectl edit`.

Like regular containers, you may not change or remove an ephemeral container
after you have added it to a Pod.

#### Note:

Ephemeral containers are not supported by [static pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/).