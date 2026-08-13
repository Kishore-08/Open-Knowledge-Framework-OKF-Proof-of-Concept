---
id: kubernetes-external-tools-47e6546b
type: concept
title: External tools
description: This section lists only the most common tools used for managing workloads
  on Kubernetes. To see a larger list, view
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### External tools

This section lists only the most common tools used for managing workloads on Kubernetes. To see a larger list, view
[Application definition and image build](https://landscape.cncf.io/guide#app-definition-and-development--application-definition-image-build)
in the [CNCF](https://cncf.io/ "Cloud Native Computing Foundation") Landscape.

#### Helm

🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](https://kubernetes.io/docs/concepts/workloads/management/#third-party-content-disclaimer)

[Helm](https://helm.sh/) is a tool for managing packages of pre-configured
Kubernetes resources. These packages are known as *Helm charts*.

#### Kustomize

[Kustomize](https://kustomize.io/) traverses a Kubernetes manifest to add, remove or update configuration options.
It is available both as a standalone binary and as a [native feature](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)
of kubectl.