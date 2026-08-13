---
id: kubernetes-the-kubernetes-api-0b6c673c
type: concept
title: The Kubernetes API
description: The Kubernetes API lets you query and manipulate the state of objects
  in Kubernetes. The core of Kubernetes' control plane is the API server and the HTTP
  API that it exposes. Users, the different part
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

# The Kubernetes API

The Kubernetes API lets you query and manipulate the state of objects in Kubernetes. The core of Kubernetes' control plane is the API server and the HTTP API that it exposes. Users, the different parts of your cluster, and external components all communicate with one another through the API server.

The core of Kubernetes' [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.")
is the [API server](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver "Control plane component that serves the Kubernetes API."). The API server
exposes an HTTP API that lets end users, different parts of your cluster, and
external components communicate with one another.

The Kubernetes API lets you query and manipulate the state of API objects in Kubernetes
(for example: Pods, Namespaces, ConfigMaps, and Events).

Most operations can be performed through the [kubectl](https://kubernetes.io/docs/reference/kubectl/)
command-line interface or other command-line tools, such as
[kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/), which in turn use the API.
However, you can also access the API directly using REST calls. Kubernetes
provides a set of [client libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/)
for those looking to
write applications using the Kubernetes API.

Each Kubernetes cluster publishes the specification of the APIs that the cluster serves.
There are two mechanisms that Kubernetes uses to publish these API specifications; both are useful
to enable automatic interoperability. For example, the `kubectl` tool fetches and caches the API
specification for enabling command-line completion and other features.
The two supported mechanisms are as follows:

- [The Discovery API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#discovery-api) provides information about the Kubernetes APIs:
  API names, resources, versions, and supported operations. This is a Kubernetes
  specific term as it is a separate API from the Kubernetes OpenAPI.
  It is intended to be a brief summary of the available resources and it does not
  detail specific schema for the resources. For reference about resource schemas,
  please refer to the OpenAPI document.
- The [Kubernetes OpenAPI Document](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#openapi-interface-definition) provides (full)
  [OpenAPI v2.0 and 3.0 schemas](https://www.openapis.org/) for all Kubernetes API
  endpoints.
  The OpenAPI v3 is the preferred method for accessing OpenAPI as it
  provides
  a more comprehensive and accurate view of the API. It includes all the available
  API paths, as well as all resources consumed and produced for every operations
  on every endpoints. It also includes any extensibility components that a cluster supports.
  The data is a complete specification and is significantly larger than that from the
  Discovery API.