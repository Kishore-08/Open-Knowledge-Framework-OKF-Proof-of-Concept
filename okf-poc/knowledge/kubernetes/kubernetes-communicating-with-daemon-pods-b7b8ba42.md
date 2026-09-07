---
id: kubernetes-communicating-with-daemon-pods-b7b8ba42
type: concept
title: Communicating with Daemon Pods
description: 'Some possible patterns for communicating with Pods in a DaemonSet are:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Communicating with Daemon Pods

Some possible patterns for communicating with Pods in a DaemonSet are:

- **Push**: Pods in the DaemonSet are configured to send updates to another service, such
  as a stats database. They do not have clients.
- **NodeIP and Known Port**: Pods in the DaemonSet can use a `hostPort`, so that the pods
  are reachable via the node IPs.
  Clients know the list of node IPs somehow, and know the port by convention.
- **DNS**: Create a [headless service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services)
  with the same pod selector, and then discover DaemonSets using the `endpoints`
  resource or retrieve multiple A records from DNS.
- **Service**: Create a service with the same Pod selector, and use the service to reach a
  daemon on a random node. Use [Service Internal Traffic Policy](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/)
  to limit to pods on the same node.