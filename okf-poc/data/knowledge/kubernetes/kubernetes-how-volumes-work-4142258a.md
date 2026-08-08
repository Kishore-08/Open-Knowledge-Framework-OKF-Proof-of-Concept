---
id: kubernetes-how-volumes-work-4142258a
type: concept
title: How volumes work
description: Kubernetes supports many types of volumes. A [Pod](https://kubernetes.io/docs/concepts/workloads/pods/
  "A Pod represents a set of running containers in your cluster.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## How volumes work

Kubernetes supports many types of volumes. A [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.")
can use any number of volume types simultaneously.
[Ephemeral volume](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/) types have a lifetime linked to a specific Pod,
but [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) exist beyond
the lifetime of any individual Pod. When a Pod ceases to exist, Kubernetes destroys ephemeral volumes;
however, Kubernetes does not destroy persistent volumes.
For any kind of volume in a given Pod, data is preserved across container restarts.

At its core, a volume is a directory, possibly with some data in it, which
is accessible to the containers in a pod. How that directory comes to be, the
medium that backs it, and the contents of it are determined by the particular
volume type used.

To use a volume, specify the volumes to provide for the Pod in `.spec.volumes`
and declare where to mount those volumes into containers in `.spec.containers[*].volumeMounts`.

When a Pod is launched, a process in the container sees a filesystem view composed from the initial contents of
the [container image](https://kubernetes.io/docs/reference/glossary/?all=true#term-image "Stored instance of a container that holds a set of software needed to run an application."), plus volumes
(if defined) mounted inside the container.
The process sees a root filesystem that initially matches the contents of the container image.
Any writes to within that filesystem hierarchy, if allowed, affect what that process views
when it performs a subsequent filesystem access.
Volumes are mounted at [specified paths](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) within the container filesystem.
For each container defined within a Pod, you must independently specify where
to mount each volume that the container uses.

Volumes cannot mount within other volumes (but see [Using subPath](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath)
for a related mechanism). Also, a volume cannot contain a hard link to anything in
a different volume.

## Types of volumes

Kubernetes supports several types of volumes.