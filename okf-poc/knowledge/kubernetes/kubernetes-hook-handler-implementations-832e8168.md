---
id: kubernetes-hook-handler-implementations-832e8168
type: concept
title: Hook handler implementations
description: Containers can access a hook by implementing and registering a handler
  for that hook.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Hook handler implementations

Containers can access a hook by implementing and registering a handler for that hook.
There are three types of hook handlers that can be implemented for Containers:

- Exec - Executes a specific command, such as `pre-stop.sh`, inside the cgroups and namespaces of the Container.
  Resources consumed by the command are counted against the Container.
- HTTP - Executes an HTTP request against a specific endpoint on the Container.
- Sleep - Pauses the container for a specified duration.