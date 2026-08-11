---
id: kubernetes-using-a-private-registry-c440e1a7
type: concept
title: Using a private registry
description: Private registries may require authentication to be able to discover
  and/or pull
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Using a private registry

Private registries may require authentication to be able to discover and/or pull
images from them.
Credentials can be provided in several ways:

- [Specifying `imagePullSecrets` when you define a Pod](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod)

  Only Pods which provide their own keys can access the private registry.
- [Configuring Nodes to Authenticate to a Private Registry](https://kubernetes.io/docs/concepts/containers/images/#configuring-nodes-to-authenticate-to-a-private-registry)

  - All Pods can read any configured private registries.
  - Requires node configuration by cluster administrator.
- Using a *kubelet credential provider* plugin to [dynamically fetch credentials for private registries](https://kubernetes.io/docs/concepts/containers/images/#kubelet-credential-provider)

  The kubelet can be configured to use credential provider exec plugin for the
  respective private registry.
- [Pre-pulled Images](https://kubernetes.io/docs/concepts/containers/images/#pre-pulled-images)

  - All Pods can use any images cached on a node.
  - Requires root access to all nodes to set up.
- Vendor-specific or local extensions

  If you're using a custom node configuration, you (or your cloud provider) can
  implement your mechanism for authenticating the node to the container registry.

These options are explained in more detail below.