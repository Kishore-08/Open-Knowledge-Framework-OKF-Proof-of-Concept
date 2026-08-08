---
id: kubernetes-pre-pulled-images-c440e1a7
type: concept
title: Pre-pulled images
description: This approach is suitable if you can control node configuration. It
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pre-pulled images

#### Note:

This approach is suitable if you can control node configuration. It
will not work reliably if your cloud provider manages nodes and replaces
them automatically.

By default, the kubelet tries to pull each image from the specified registry.
However, if the `imagePullPolicy` property of the container is set to `IfNotPresent` or `Never`,
then a local image is used (preferentially or exclusively, respectively).

If you want to rely on pre-pulled images as a substitute for registry authentication,
you must ensure all nodes in the cluster have the same pre-pulled images.

This can be used to preload certain images for speed or as an alternative to
authenticating to a private registry.

Similar to the usage of the [kubelet credential provider](https://kubernetes.io/docs/concepts/containers/images/#kubelet-credential-provider),
pre-pulled images are also suitable for launching
[static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/ "A pod managed directly by the kubelet daemon on a specific node.") that depend
on images hosted in a private registry.

#### Note:

FEATURE STATE:
`Kubernetes v1.35 [beta]`(enabled by default)

Access to pre-pulled images may be authorized according to [image pull credential verification](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification).