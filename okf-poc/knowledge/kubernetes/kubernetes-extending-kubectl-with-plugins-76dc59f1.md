---
id: kubernetes-extending-kubectl-with-plugins-76dc59f1
type: concept
title: Extending kubectl with plugins
description: You can extend `kubectl` with [plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)
  that add new
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubectl/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Extending kubectl with plugins

You can extend `kubectl` with [plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/) that add new
sub-commands. Plugins are standalone binaries that follow the `kubectl-<plugin-name>` naming convention.
The Kubernetes community maintains many plugins, and you can manage them with the
[Krew](https://krew.sigs.k8s.io/) plugin manager.