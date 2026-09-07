---
id: kubernetes-what-s-next-3e9846ed
type: concept
title: What's next
description: As well as reading about each API kind for workload management, you can
  read how to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## What's next

As well as reading about each API kind for workload management, you can read how to
do specific tasks:

- [Run a stateless application using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)
- Run a stateful application either as a [single instance](https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/)
  or as a [replicated set](https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/)
- [Run automated tasks with a CronJob](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/)

To learn about Kubernetes' mechanisms for separating code from configuration,
visit [Configuration](https://kubernetes.io/docs/concepts/configuration/).

There are two supporting concepts that provide backgrounds about how Kubernetes manages pods
for applications:

- [Garbage collection](https://kubernetes.io/docs/concepts/architecture/garbage-collection/) tidies up objects
  from your cluster after their *owning resource* has been removed.
- The [*time-to-live after finished* controller](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/)
  removes Jobs once a defined time has passed since they completed.

Once your application is running, you might want to make it available on the internet as
a [Service](https://kubernetes.io/docs/concepts/services-networking/service/) or, for web application only,
using an [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/).