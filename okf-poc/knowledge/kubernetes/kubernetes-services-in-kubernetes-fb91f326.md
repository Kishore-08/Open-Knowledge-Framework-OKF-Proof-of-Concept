---
id: kubernetes-services-in-kubernetes-fb91f326
type: concept
title: Services in Kubernetes
description: The Service API, part of Kubernetes, is an abstraction to help you expose
  groups of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Services in Kubernetes

The Service API, part of Kubernetes, is an abstraction to help you expose groups of
Pods over a network. Each Service object defines a logical set of endpoints (usually
these endpoints are Pods) along with a policy about how to make those pods accessible.

For example, consider a stateless image-processing backend which is running with
3 replicas. Those replicas are fungible—frontends do not care which backend
they use. While the actual Pods that compose the backend set may change, the
frontend clients should not need to be aware of that, nor should they need to keep
track of the set of backends themselves.

The Service abstraction enables this decoupling.

The set of Pods targeted by a Service is usually determined
by a [selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels.") that you
define.
To learn about other ways to define Service endpoints,
see [Services *without* selectors](https://kubernetes.io/docs/concepts/services-networking/service/#services-without-selectors).

If your workload speaks HTTP, you might choose to use an
[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) to control how web traffic
reaches that workload.
Ingress is not a Service type, but it acts as the entry point for your
cluster. An Ingress lets you consolidate your routing rules into a single resource, so
that you can expose multiple components of your workload, running separately in your
cluster, behind a single listener.

The [Gateway](https://gateway-api.sigs.k8s.io/#what-is-the-gateway-api) API for Kubernetes
provides extra capabilities beyond Ingress and Service. You can add Gateway to your cluster -
it is a family of extension APIs, implemented using
[CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/ "Custom code that defines a resource to add to your Kubernetes API server without building a complete custom server.") -
and then use these to configure access to network services that are running in your cluster.