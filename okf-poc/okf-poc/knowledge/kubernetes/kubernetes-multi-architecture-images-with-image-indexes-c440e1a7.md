---
id: kubernetes-multi-architecture-images-with-image-indexes-c440e1a7
type: concept
title: Multi-architecture images with image indexes
description: As well as providing binary images, a container registry can also serve
  a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Multi-architecture images with image indexes

As well as providing binary images, a container registry can also serve a
[container image index](https://github.com/opencontainers/image-spec/blob/master/image-index.md).
An image index can point to multiple [image manifests](https://github.com/opencontainers/image-spec/blob/master/manifest.md)
for architecture-specific versions of a container. The idea is that you can have
a name for an image (for example: `pause`, `example/mycontainer`, `kube-apiserver`)
and allow different systems to fetch the right binary image for the machine
architecture they are using.

The Kubernetes project typically creates container images for its releases with
names that include the suffix `-$(ARCH)`. For backward compatibility, generate
older images with suffixes. For instance, an image named as `pause` would be a
multi-architecture image containing manifests for all supported architectures,
while `pause-amd64` would be a backward-compatible version for older configurations,
or for YAML files with hardcoded image names containing suffixes.