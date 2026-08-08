---
id: kubernetes-object-spec-and-status-65511bde
type: concept
title: Object spec and status
description: Almost every Kubernetes object includes two nested object fields that
  govern
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Object spec and status

Almost every Kubernetes object includes two nested object fields that govern
the object's configuration: the object *`spec`* and the object *`status`*.
For objects that have a `spec`, you have to set this when you create the object,
providing a description of the characteristics you want the resource to have:
its *desired state*.

The `status` describes the *current state* of the object, supplied and updated
by the Kubernetes system and its components. The Kubernetes
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") continually
and actively manages every object's actual state to match the desired state you
supplied.

For example: in Kubernetes, a Deployment is an object that can represent an
application running on your cluster. When you create the Deployment, you
might set the Deployment `spec` to specify that you want three replicas of
the application to be running. The Kubernetes system reads the Deployment
spec and starts three instances of your desired application--updating
the status to match your spec. If any of those instances should fail
(a status change), the Kubernetes system responds to the difference
between spec and status by making a correction--in this case, starting
a replacement instance.

For more information on the object spec, status, and metadata, see the
[Kubernetes API Conventions](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md).