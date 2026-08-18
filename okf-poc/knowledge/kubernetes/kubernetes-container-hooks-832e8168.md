---
id: kubernetes-container-hooks-832e8168
type: concept
title: Container hooks
description: 'There are two hooks that are exposed to Containers:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Container hooks

There are two hooks that are exposed to Containers:

`PostStart`

This hook is executed immediately after a container is created.
It runs **concurrently** with the container's `ENTRYPOINT` (main process),
meaning the hook may run before, during, or after the main process starts.

No parameters are passed to the handler.

#### Note:

While the hook runs concurrently with the container process,
it can delay container status updates;
the container may not transition to `Running` until the hook completes.

`PreStop`

This hook is called immediately before a container is terminated due to an API request or management
event such as a liveness/startup probe failure, preemption, resource contention and others. A call
to the `PreStop` hook fails if the container is already in a terminated or completed state and the
hook must complete before the TERM signal to stop the container can be sent. The Pod's termination
grace period countdown begins before the `PreStop` hook is executed, so regardless of the outcome of
the handler, the container will eventually terminate within the Pod's termination grace period. No
parameters are passed to the handler.

A more detailed description of the termination behavior can be found in
[Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination).

`StopSignal`

The StopSignal lifecycle can be used to define a stop signal which would be sent to the container when it is
stopped. If you set this, it overrides any `STOPSIGNAL` instruction defined within the container image.

A more detailed description of termination behaviour with custom stop signals can be found in
[Stop Signals](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-stop-signals).