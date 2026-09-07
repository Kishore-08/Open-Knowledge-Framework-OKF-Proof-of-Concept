---
id: kubernetes-how-kubectl-works-76dc59f1
type: concept
title: How kubectl works
description: The `kubectl` tool connects to the API server and authenticates using
  the cluster, user, and context defined in your
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubectl/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## How kubectl works

The `kubectl` tool connects to the API server and authenticates using the cluster, user, and context defined in your
[kubeconfig](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) file.
When you run `kubectl` from outside a cluster, it uses the kubeconfig file to find the API server address and credentials.
When `kubectl` runs inside a Pod (for example, in a CI/CD pipeline), it can use in-cluster authentication
based on the ServiceAccount token mounted in the Pod.

When you run a command, `kubectl` translates your intent into one or more HTTP requests to the
[Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/). The API server validates each request,
applies it to the cluster state stored in [etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/ "Consistent and highly-available key value store used as backing store of Kubernetes for all cluster data."), and
returns the result. This means every `kubectl` action, whether creating a Deployment or reading logs,
follows the same API-driven path.

Because your kubeconfig can define multiple clusters, users, and contexts, you can use `kubectl` to
switch between clusters without reconfiguring your environment. Run `kubectl config use-context` to
change the active context.