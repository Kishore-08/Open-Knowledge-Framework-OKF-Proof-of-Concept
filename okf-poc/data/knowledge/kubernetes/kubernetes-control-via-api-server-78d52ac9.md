---
id: kubernetes-control-via-api-server-78d52ac9
type: concept
title: Control via API server
description: The [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/
  "A finite or batch task that runs to completion.") controller is an example of a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/controller/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Control via API server

The [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/ "A finite or batch task that runs to completion.") controller is an example of a
Kubernetes built-in controller. Built-in controllers manage state by
interacting with the cluster API server.

Job is a Kubernetes resource that runs a
[Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."), or perhaps several Pods, to carry out
a task and then stop.

(Once [scheduled](https://kubernetes.io/docs/concepts/scheduling-eviction/), Pod objects become part of the
desired state for a kubelet).

When the Job controller sees a new task it makes sure that, somewhere
in your cluster, the kubelets on a set of Nodes are running the right
number of Pods to get the work done.
The Job controller does not run any Pods or containers
itself. Instead, the Job controller tells the API server to create or remove
Pods.
Other components in the
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.")
act on the new information (there are new Pods to schedule and run),
and eventually the work is done.

After you create a new Job, the desired state is for that Job to be completed.
The Job controller makes the current state for that Job be nearer to your
desired state: creating Pods that do the work you wanted for that Job, so that
the Job is closer to completion.

Controllers also update the objects that configure them.
For example: once the work is done for a Job, the Job controller
updates that Job object to mark it `Finished`.

(This is a bit like how some thermostats turn a light off to
indicate that your room is now at the temperature you set).