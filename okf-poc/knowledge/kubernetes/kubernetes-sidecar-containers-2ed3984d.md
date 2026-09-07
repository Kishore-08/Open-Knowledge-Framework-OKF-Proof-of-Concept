---
id: kubernetes-sidecar-containers-2ed3984d
type: concept
title: Sidecar Containers
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Sidecar Containers

FEATURE STATE:
`Kubernetes v1.33 [stable]`(enabled by default)

Sidecar containers are the secondary containers that run along with the main
application container within the same [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").
These containers are used to enhance or to extend the functionality of the primary *app
container* by providing additional services, or functionality such as logging, monitoring,
security, or data synchronization, without directly altering the primary application code.

Typically, you only have one app container in a Pod. For example, if you have a web
application that requires a local webserver, the local webserver is a sidecar and the
web application itself is the app container.