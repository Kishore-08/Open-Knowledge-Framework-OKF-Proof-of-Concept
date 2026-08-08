---
id: kubernetes-ensure-image-pull-credential-verification-c440e1a7
type: concept
title: Ensure image pull credential verification
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Ensure image pull credential verification

FEATURE STATE:
`Kubernetes v1.35 [beta]`(enabled by default)

If the `KubeletEnsureSecretPulledImages` feature gate is enabled for your cluster,
Kubernetes will validate image credentials for every image that requires credentials
to be pulled, even if that image is already present on the node. This validation
ensures that images in a Pod request which have not been successfully pulled
with the provided credentials must re-pull the images from the registry.
Additionally, image pulls that re-use the same credentials
which previously resulted in a successful image pull will not need to re-pull from
the registry and are instead validated locally without accessing the registry
(provided the image is available locally).
This is controlled by the`imagePullCredentialsVerificationPolicy` field in the
[Kubelet configuration](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/#kubelet-config-k8s-io-v1beta1-ImagePullCredentialsVerificationPolicy).

This configuration controls when image pull credentials must be verified if the
image is already present on the node:

- `NeverVerify`: Mimics the behavior of having this feature gate disabled.
  If the image is present locally, image pull credentials are not verified.
- `NeverVerifyPreloadedImages`: Images pulled outside the kubelet are not verified,
  but all other images will have their credentials verified. This is the default behavior.
- `NeverVerifyAllowListedImages`: Images pulled outside the kubelet and mentioned within the
  `preloadedImagesVerificationAllowlist` specified in the kubelet config are not verified.
- `AlwaysVerify`: All images will have their credentials verified
  before they can be used.

This verification applies to [pre-pulled images](https://kubernetes.io/docs/concepts/containers/images/#pre-pulled-images),
images pulled using node-wide secrets, and images pulled using Pod-level secrets.

#### Note:

In the case of credential rotation, the credentials previously used to pull the image
will continue to verify without the need to access the registry. New or rotated credentials
will require the image to be re-pulled from the registry.

#### Enabling `KubeletEnsureSecretPulledImages` for the first time

When the `KubeletEnsureSecretPulledImages` gets enabled for the first time, either
by a kubelet upgrade or by explicitly enabling the feature, if a kubelet is able to
access any images at that time, these will all be considered pre-pulled. This happens
because in this case the kubelet has no records about the images being pulled.
The kubelet will only be able to start making image pull records as any image gets
pulled for the first time.

If this is a concern, it is advised to clean up nodes of all images that should not
be considered pre-pulled before enabling the feature.

Note that removing the directory holding the image pulled records will have the same
effect on kubelet restart, particularly the images currently cached in the nodes by
the container runtime will all be considered pre-pulled.