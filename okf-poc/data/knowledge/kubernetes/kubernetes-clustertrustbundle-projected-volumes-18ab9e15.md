---
id: kubernetes-clustertrustbundle-projected-volumes-18ab9e15
type: concept
title: clusterTrustBundle projected volumes
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## clusterTrustBundle projected volumes

FEATURE STATE:
`Kubernetes v1.33 [beta]`(disabled by default)

#### Note:

To use this feature in Kubernetes 1.36, you must enable support for ClusterTrustBundle objects
with the `ClusterTrustBundle` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) and
`--runtime-config=certificates.k8s.io/v1beta1/clustertrustbundles=true` kube-apiserver flag,
then enable the `ClusterTrustBundleProjection` feature gate.

The `clusterTrustBundle` projected volume source injects the contents of one or more
[ClusterTrustBundle](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#cluster-trust-bundles)
objects as an automatically-updating file in the container filesystem.

ClusterTrustBundles can be selected either by [name](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#ctb-signer-unlinked)
or by [signer name](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#ctb-signer-linked).

To select by name, use the `name` field to designate a single ClusterTrustBundle object.

To select by signer name, use the `signerName` field (and optionally the
`labelSelector` field) to designate a set of ClusterTrustBundle objects that use
the given signer name. If `labelSelector` is not present, then all
ClusterTrustBundles for that signer are selected.

The kubelet deduplicates the certificates in the selected ClusterTrustBundle objects,
normalizes the PEM representations (discarding comments and headers), reorders the certificates,
and writes them into the file named by `path`.
As the set of selected ClusterTrustBundles or their content changes, kubelet keeps the file up-to-date.

By default, the kubelet will prevent the pod from starting if the named ClusterTrustBundle is not found,
or if `signerName` / `labelSelector` do not match any ClusterTrustBundles.
If this behavior is not what you want, then set the `optional` field to `true`,
and the pod will start up with an empty file at `path`.

[`pods/storage/projected-clustertrustbundle.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/storage/projected-clustertrustbundle.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/storage/projected-clustertrustbundle.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: sa-ctb-name-test
spec:
  containers:
  - name: container-test
    image: busybox
    command: ["sleep", "3600"]
    volumeMounts:
    - name: token-vol
      mountPath: "/root-certificates"
      readOnly: true
  serviceAccountName: default
  volumes:
  - name: token-vol
    projected:
      sources:
      - clusterTrustBundle:
          name: example
          path: example-roots.pem
      - clusterTrustBundle:
          signerName: "example.com/mysigner"
          labelSelector:
            matchLabels:
              version: live
          path: mysigner-roots.pem
          optional: true
```