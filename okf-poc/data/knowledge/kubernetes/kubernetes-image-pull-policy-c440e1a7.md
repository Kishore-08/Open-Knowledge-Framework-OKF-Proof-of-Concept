---
id: kubernetes-image-pull-policy-c440e1a7
type: concept
title: Image pull policy
description: The `imagePullPolicy` for a container and the tag of the image both affect
  *when* the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Image pull policy

The `imagePullPolicy` for a container and the tag of the image both affect *when* the
[kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) attempts to pull
(download) the specified image.

Here's a list of the values you can set for `imagePullPolicy` and the effects
these values have:

`IfNotPresent`
:   the image is pulled only if it is not already present locally.

`Always`
:   every time the kubelet launches a container, the kubelet requests the
    [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers.")
    to pull the image. The container runtime contacts the registry, resolves
    the image tag or name to a
    [digest](https://docs.docker.com/engine/reference/commandline/pull/#pull-an-image-by-digest-immutable-identifier),
    and downloads any layers that are not already cached locally.
    If all layers are already present, the container runtime uses the cached
    image without downloading it again. The kubelet itself does not check
    whether the image is cached locally; it always delegates to the container
    runtime.

`Never`
:   the kubelet does not try fetching the image. If the image is somehow already present
    locally, the kubelet attempts to start the container; otherwise, startup fails.
    See [pre-pulled images](https://kubernetes.io/docs/concepts/containers/images/#pre-pulled-images) for more details.

The caching semantics of the container runtime make even
`imagePullPolicy: Always` efficient, as long as the registry is reliably accessible.
The container runtime can notice that the image layers already exist on the node
so that they don't need to be downloaded again.

#### Note:

You should avoid using the `:latest` tag when deploying containers in production as
it is harder to track which version of the image is running and more difficult to
roll back properly.

Instead, specify a meaningful tag such as `v1.42.0` and/or a digest.

To make sure the Pod always uses the same version of a container image, you can specify
the image's digest;
replace `<image-name>:<tag>` with `<image-name>@<digest>`
(for example, `image@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`).

When using image tags, if the image registry were to change the code that the tag on that image
represents, you might end up with a mix of Pods running the old and new code. An image digest
uniquely identifies a specific version of the image, so Kubernetes runs the same code every time
it starts a container with that image name and digest specified. Specifying an image by digest
pins the code that you run so that a change at the registry cannot lead to that mix of versions.

There are third-party [admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
that mutate Pods (and PodTemplates) when they are created, so that the
running workload is defined based on an image digest rather than a tag.
That might be useful if you want to make sure that your entire workload is
running the same code no matter what tag changes happen at the registry.

#### Default image pull policy

When you (or a controller) submit a new Pod to the API server, your cluster sets the
`imagePullPolicy` field when specific conditions are met:

- if you omit the `imagePullPolicy` field, and you specify the digest for the
  container image, the `imagePullPolicy` is automatically set to `IfNotPresent`.
- if you omit the `imagePullPolicy` field, and the tag for the container image is
  `:latest`, `imagePullPolicy` is automatically set to `Always`.
- if you omit the `imagePullPolicy` field, and you don't specify the tag for the
  container image, `imagePullPolicy` is automatically set to `Always`.
- if you omit the `imagePullPolicy` field, and you specify a tag for the container
  image that isn't `:latest`, the `imagePullPolicy