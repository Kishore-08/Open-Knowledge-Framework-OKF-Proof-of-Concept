---
id: kubernetes-the-kubectl-command-line-tool-76dc59f1
type: concept
title: The kubectl command-line tool
description: kubectl is the primary command-line tool for communicating with a Kubernetes
  cluster. This page provides an overview of kubectl and its role in the Kubernetes
  ecosystem.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubectl/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# The kubectl command-line tool

kubectl is the primary command-line tool for communicating with a Kubernetes cluster. This page provides an overview of kubectl and its role in the Kubernetes ecosystem.

Kubernetes provides a command line tool for communicating with a Kubernetes cluster's
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers."),
using the Kubernetes API.

The `kubectl` tool communicates with your cluster through the [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/).
For configuration, `kubectl` looks for a file named `config` in the `$HOME/.kube` directory.
You can specify other [kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
files by setting the `KUBECONFIG` environment variable or by setting the
[`--kubeconfig`](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) flag.