---
id: kubernetes-image-names-c440e1a7
type: concept
title: Image names
description: Container images are usually given a name such as `pause`, `example/mycontainer`,
  or `kube-apiserver`.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Image names

Container images are usually given a name such as `pause`, `example/mycontainer`, or `kube-apiserver`.
Images can also include a registry hostname; for example: `fictional.registry.example/imagename`,
and possibly a port number as well; for example: `fictional.registry.example:10443/imagename`.

If you don't specify a registry hostname, Kubernetes assumes that you mean the [Docker public registry](https://hub.docker.com/).
You can change this behavior by setting a default image registry in the
[container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) configuration.

After the image name part you can add a *tag* or *digest* (in the same way you would when using with commands
like `docker` or `podman`). Tags let you identify different versions of the same series of images.
Digests are a unique identifier for a specific version of an image. Digests are hashes of the image's content,
and are immutable. Tags can be moved to point to different images, but digests are fixed.

Image tags consist of lowercase and uppercase letters, digits, underscores (`_`),
periods (`.`), and dashes (`-`). A tag can be up to 128 characters long, and must
conform to the following regex pattern: `[a-zA-Z0-9_][a-zA-Z0-9._-]{0,127}`.
You can read more about it and find the validation regex in the
[OCI Distribution Specification](https://github.com/opencontainers/distribution-spec/blob/master/spec.md#workflow-categories).
If you don't specify a tag, Kubernetes assumes you mean the tag `latest`.

Image digests consists of a hash algorithm (such as `sha256`) and a hash value. For example:
`sha256:1ff6c18fbef2045af6b9c16bf034cc421a29027b800e4f9b68ae9b1cb3e9ae07`.
You can find more information about the digest format in the
[OCI Image Specification](https://github.com/opencontainers/image-spec/blob/master/descriptor.md#digests).

Some image name examples that Kubernetes can use are:

- `busybox` — Image name only, no tag or digest. Kubernetes will use the Docker
  public registry and latest tag. Equivalent to `docker.io/library/busybox:latest`.
- `busybox:1.32.0` — Image name with tag. Kubernetes will use the Docker
  public registry. Equivalent to `docker.io/library/busybox:1.32.0`.
- `registry.k8s.io/pause:latest` — Image name with a custom registry and latest tag.
- `registry.k8s.io/pause:3.5` — Image name with a custom registry and non-latest tag.
- `registry.k8s.io/pause@sha256:1ff6c18fbef2045af6b9c16bf034cc421a29027b800e4f9b68ae9b1cb3e9ae07` —
  Image name with digest.
- `registry.k8s.io/pause:3.5@sha256:1ff6c18fbef2045af6b9c16bf034cc421a29027b800e4f9b68ae9b1cb3e9ae07` —
  Image name with tag and digest. Only the digest will be used for pulling.