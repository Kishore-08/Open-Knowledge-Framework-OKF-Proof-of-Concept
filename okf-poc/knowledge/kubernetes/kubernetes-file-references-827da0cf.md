---
id: kubernetes-file-references-827da0cf
type: concept
title: File references
description: File and path references in a kubeconfig file are relative to the location
  of the kubeconfig file.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## File references

File and path references in a kubeconfig file are relative to the location of the kubeconfig file.
File references on the command line are relative to the current working directory.
In `$HOME/.kube/config`, relative paths are stored relatively, and absolute paths
are stored absolutely.