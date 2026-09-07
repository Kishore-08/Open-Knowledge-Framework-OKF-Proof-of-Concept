---
id: kubernetes-what-you-can-do-with-kubectl-76dc59f1
type: concept
title: What you can do with kubectl
description: 'The `kubectl` tool supports many operations, which fall into these broad
  categories:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubectl/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## What you can do with kubectl

The `kubectl` tool supports many operations, which fall into these broad categories:

- **Manage resources** – Create, update, and delete objects such as Pods, Deployments, and Services.
  Use `kubectl apply` for declarative management from configuration files.
- **Inspect cluster state** – List and describe objects, view events, and check resource usage.
- **Debug** – View logs from containers, execute commands inside a running container, or port-forward to a Pod.
- **Cluster operations** – Drain nodes for maintenance, cordon nodes to prevent new workloads, and manage cluster configuration.
- **Script and automate** – Format output as JSON, YAML, or custom columns using [JSONPath](https://kubernetes.io/docs/reference/kubectl/jsonpath/) for use in scripts and pipelines.

For syntax, command reference, and examples, see the [kubectl reference documentation](https://kubernetes.io/docs/reference/kubectl/).