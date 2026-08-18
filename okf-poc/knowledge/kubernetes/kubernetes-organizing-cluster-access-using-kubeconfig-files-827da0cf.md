---
id: kubernetes-organizing-cluster-access-using-kubeconfig-files-827da0cf
type: concept
title: Organizing Cluster Access Using kubeconfig Files
description: Use kubeconfig files to organize information about clusters, users, namespaces,
  and
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

# Organizing Cluster Access Using kubeconfig Files

Use kubeconfig files to organize information about clusters, users, namespaces, and
authentication mechanisms. The `kubectl` command-line tool uses kubeconfig files to
find the information it needs to choose a cluster and communicate with the API server
of a cluster.

#### Note:

A file that is used to configure access to clusters is called
a *kubeconfig file*. This is a generic way of referring to configuration files.
It does not mean that there is a file named `kubeconfig`.

#### Warning:

Only use kubeconfig files from trusted sources. Using a specially-crafted kubeconfig file could result in malicious code execution or file exposure.
If you must use an untrusted kubeconfig file, inspect it carefully first, much as you would a shell script.

By default, `kubectl` looks for a file named `config` in the `$HOME/.kube` directory.
You can specify other kubeconfig files by setting the `KUBECONFIG` environment
variable or by setting the
[`--kubeconfig`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/) flag.

For step-by-step instructions on creating and specifying kubeconfig files, see
[Configure Access to Multiple Clusters](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/).