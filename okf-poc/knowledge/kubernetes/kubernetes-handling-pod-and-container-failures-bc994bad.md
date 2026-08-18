---
id: kubernetes-handling-pod-and-container-failures-bc994bad
type: concept
title: Handling Pod and container failures
description: A container in a Pod may fail for a number of reasons, such as because
  the process in it exited with
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Handling Pod and container failures

A container in a Pod may fail for a number of reasons, such as because the process in it exited with
a non-zero exit code, or the container was killed for exceeding a memory limit, etc. If this
happens, and the `.spec.template.spec.restartPolicy = "OnFailure"`, then the Pod stays
on the node, but the container is re-run. Therefore, your program needs to handle the case when it is
restarted locally, or else specify `.spec.template.spec.restartPolicy = "Never"`.
See [pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) for more information on `restartPolicy`.

An entire Pod can also fail, for a number of reasons, such as when the pod is kicked off the node
(node is upgraded, rebooted, deleted, etc.), or if a container of the Pod fails and the
`.spec.template.spec.restartPolicy = "Never"`. When a Pod fails, then the Job controller
starts a new Pod. This means that your application needs to handle the case when it is restarted in a new
pod. In particular, it needs to handle temporary files, locks, incomplete output and the like
caused by previous runs.

By default, each pod failure is counted towards the `.spec.backoffLimit` limit,
see [pod backoff failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy). However, you can
customize handling of pod failures by setting the Job's [pod failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-failure-policy).

Additionally, you can choose to count the pod failures independently for each
index of an [Indexed](https://kubernetes.io/docs/concepts/workloads/controllers/job/#completion-mode) Job by setting the `.spec.backoffLimitPerIndex` field
(for more information, see [backoff limit per index](https://kubernetes.io/docs/concepts/workloads/controllers/job/#backoff-limit-per-index)).

Note that even if you specify `.spec.parallelism = 1` and `.spec.completions = 1` and
`.spec.template.spec.restartPolicy = "Never"`, the same program may
sometimes be started twice.

If you do specify `.spec.parallelism` and `.spec.completions` both greater than 1, then there may be
multiple pods running at once. Therefore, your pods must also be tolerant of concurrency.

If you specify the `.spec.podFailurePolicy` field, the Job controller does not consider a terminating
Pod (a pod that has a `.metadata.deletionTimestamp` field set) as a failure until that Pod is
terminal (its `.status.phase` is `Failed` or `Succeeded`). However, the Job controller
creates a replacement Pod as soon as the termination becomes apparent. Once the
pod terminates, the Job controller evaluates `.backoffLimit` and `.podFailurePolicy`
for the relevant Job, taking this now-terminated Pod into consideration.

If either of these requirements is not satisfied, the Job controller counts
a terminating Pod as an immediate failure, even if that Pod later terminates
with `phase: "Succeeded"`.