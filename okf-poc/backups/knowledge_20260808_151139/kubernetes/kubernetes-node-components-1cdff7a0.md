---
id: kubernetes-node-components-1cdff7a0
type: concept
title: Node Components
description: 'Run on every node, maintaining running pods and providing the Kubernetes
  runtime environment:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/components/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Node Components

Run on every node, maintaining running pods and providing the Kubernetes runtime environment:

[kubelet](https://kubernetes.io/docs/concepts/architecture/#kubelet)
:   Ensures that Pods are running, including their containers.

[kube-proxy](https://kubernetes.io/docs/concepts/architecture/#kube-proxy) (optional)
:   Maintains network rules on nodes to implement [Services](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.").

[Container runtime](https://kubernetes.io/docs/concepts/architecture/#container-runtime)
:   Software responsible for running containers. Read
    [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) to learn more.

🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](https://kubernetes.io/docs/concepts/overview/components/#third-party-content-disclaimer)

Your cluster may require additional software on each node; for example, you might also
run [systemd](https://systemd.io/) on a Linux node to supervise local components.