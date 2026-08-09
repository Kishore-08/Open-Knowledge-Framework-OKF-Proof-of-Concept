---
id: kubernetes-custom-resources-0f516df7
type: concept
title: Custom resources
description: A *resource* is an endpoint in the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
  that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Custom resources

A *resource* is an endpoint in the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) that
stores a collection of [API objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.")
of a certain kind; for example, the built-in *pods* resource contains a collection of Pod objects.

A *custom resource* is an extension of the Kubernetes API that is not necessarily available in a default
Kubernetes installation. It represents a customization of a particular Kubernetes installation. However,
many core Kubernetes functions are now built using custom resources, making Kubernetes more modular.

Custom resources can appear and disappear in a running cluster through dynamic registration,
and cluster admins can update custom resources independently of the cluster itself.
Once a custom resource is installed, users can create and access its objects using
[kubectl](https://kubernetes.io/docs/reference/kubectl/ "A command line tool for communicating with a Kubernetes cluster."), just as they do for built-in resources
like *Pods*.