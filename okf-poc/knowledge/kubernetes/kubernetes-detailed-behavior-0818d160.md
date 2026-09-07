---
id: kubernetes-detailed-behavior-0818d160
type: concept
title: Detailed behavior
description: During Pod startup, the kubelet delays running init containers until
  the networking
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Detailed behavior

During Pod startup, the kubelet delays running init containers until the networking
and storage are ready. Then the kubelet runs the Pod's init containers in the order
they appear in the Pod's spec.

Each init container must exit successfully before
the next container starts. If a container fails to start due to the runtime or
exits with failure, it is retried according to the Pod `restartPolicy`. However,
if the Pod `restartPolicy` is set to Always, the init containers use
`restartPolicy` OnFailure.

A Pod cannot be `Ready` until all init containers have succeeded. The ports on an
init container are not aggregated under a Service. A Pod that is initializing
is in the `Pending` state but should have a condition `Initialized` set to false.

If the Pod [restarts](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/#pod-restart-reasons), or is restarted, all init containers
must execute again.

Changes to the init container spec are limited to the container image field.
Directly altering the `image` field of an init container does *not* restart the
Pod or trigger its recreation. If the Pod has yet to start, that change may
have an effect on how the Pod boots up.

For a [pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates)
you can typically change any field for an init container; the impact of making
that change depends on where the pod template is used.

Because init containers can be restarted, retried, or re-executed, init container
code should be idempotent. In particular, code that writes into any `emptyDir` volume
should be prepared for the possibility that an output file already exists.

Init containers have all of the fields of an app container. However, Kubernetes
prohibits `readinessProbe` from being used because init containers cannot
define readiness distinct from completion. This is enforced during validation.

Use `activeDeadlineSeconds` on the Pod to prevent init containers from failing forever.
The active deadline includes init containers.
However it is recommended to use `activeDeadlineSeconds` only if teams deploy their application
as a Job, because `activeDeadlineSeconds` has an effect even after initContainer finished.
The Pod which is already running correctly would be killed by `activeDeadlineSeconds` if you set.

The name of each app and init container in a Pod must be unique; a
validation error is thrown for any container sharing a name with another.