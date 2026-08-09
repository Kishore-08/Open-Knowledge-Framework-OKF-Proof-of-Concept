---
id: kubernetes-volumes-4142258a
type: concept
title: Volumes
description: Kubernetes *volumes* provide a way for containers in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/
  "A Pod represents a set of running containers in your cluster.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Volumes

Kubernetes *volumes* provide a way for containers in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.")
to access and share data via the filesystem. There are different kinds of volume that you can use for different purposes,
such as:

- populating a configuration file based on a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/ "An API object used to store non-confidential data in key-value pairs. Can be consumed as environment variables, command-line arguments, or configuration files in a volume.")
  or a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.")
- providing some temporary scratch space for a Pod
- sharing a filesystem between two different containers in the same Pod
- sharing a filesystem between two different Pods (even if those Pods run on different nodes)
- durably storing data so that it stays available even if the Pod restarts or is replaced
- passing configuration information to an app running in a container, based on details of the Pod
  the container is in
  (for example: telling a [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/ "An auxilliary container that stays running throughout the lifecycle of a Pod.")
  what namespace the Pod is running in)
- providing read-only access to data in a different container image

Data sharing can be between different local processes within a container, or between different containers,
or between Pods.