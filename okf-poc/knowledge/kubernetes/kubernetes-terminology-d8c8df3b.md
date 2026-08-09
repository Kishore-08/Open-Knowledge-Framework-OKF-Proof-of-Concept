---
id: kubernetes-terminology-d8c8df3b
type: concept
title: Terminology
description: 'For clarity, this guide defines the following terms:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Terminology

For clarity, this guide defines the following terms:

- Node: A worker machine in Kubernetes, part of a cluster.
- Cluster: A set of Nodes that run containerized applications managed by Kubernetes.
  For this example, and in most common Kubernetes deployments, nodes in the cluster
  are not part of the public internet.
- Edge router: A router that enforces the firewall policy for your cluster. This
  could be a gateway managed by a cloud provider or a physical piece of hardware.
- Cluster network: A set of links, logical or physical, that facilitate communication
  within a cluster according to the Kubernetes [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/).
- Service: A Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") that identifies
  a set of Pods using [label](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") selectors.
  Unless mentioned otherwise, Services are assumed to have virtual IPs only routable within the cluster network.