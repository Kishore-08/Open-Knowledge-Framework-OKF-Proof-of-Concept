---
id: kubernetes-container-image-pull-secrets-38cc788d
type: concept
title: Container image pull Secrets
description: If you want to fetch container images from a private repository, you
  need a way for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Container image pull Secrets

If you want to fetch container images from a private repository, you need a way for
the kubelet on each node to authenticate to that repository. You can configure
*image pull Secrets* to make this possible. These Secrets are configured at the Pod
level.

#### Using imagePullSecrets

The `imagePullSecrets` field is a list of references to Secrets in the same namespace.
You can use an `imagePullSecrets` to pass a Secret that contains a Docker (or other) image registry
password to the kubelet. The kubelet uses this information to pull a private image on behalf of your Pod.
See the [PodSpec API](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#podspec-v1-core)
for more information about the `imagePullSecrets` field.

##### Manually specifying an imagePullSecret

You can learn how to specify `imagePullSecrets` from the
[container images](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod)
documentation.

##### Arranging for imagePullSecrets to be automatically attached

You can manually create `imagePullSecrets`, and reference these from a ServiceAccount. Any Pods
created with that ServiceAccount or created with that ServiceAccount by default, will get their
`imagePullSecrets` field set to that of the service account.
See [Add ImagePullSecrets to a service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account)
for a detailed explanation of that process.