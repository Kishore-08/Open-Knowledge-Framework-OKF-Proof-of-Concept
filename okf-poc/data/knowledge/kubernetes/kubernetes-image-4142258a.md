---
id: kubernetes-image-4142258a
type: concept
title: image
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### image

FEATURE STATE:
`Kubernetes v1.36 [stable]`(enabled by default)

An `image` volume source represents an OCI object (a container image or
artifact) which is available on the kubelet's host machine.

An example of using the `image` volume source is:

[`pods/image-volumes.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/image-volumes.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/image-volumes.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: image-volume
spec:
  containers:
  - name: shell
    command: ["sleep", "infinity"]
    image: debian
    volumeMounts:
    - name: volume
      mountPath: /volume
  volumes:
  - name: volume
    image:
      reference: quay.io/crio/artifact:v2
      pullPolicy: IfNotPresent
```

The volume is resolved at Pod startup, depending on which `pullPolicy` value is
provided:

`Always`
:   The kubelet always attempts to pull the reference. If the pull fails,
    the kubelet sets the Pod to `Failed`.

`Never`
:   The kubelet never pulls the reference and only uses a local image or artifact.
    The Pod becomes `Failed` if any layers of the image aren't already present locally,
    or if the manifest for that image isn't already cached.

`IfNotPresent`
:   The kubelet pulls if the reference isn't already present on disk. The Pod becomes
    `Failed` if the reference isn't present and the pull fails.

The volume gets re-resolved if the Pod gets deleted and recreated, which means
that new remote content will become available on Pod recreation. A failure to
resolve or pull the image during Pod startup will block containers from starting
and may add significant latency. Failures will be retried using normal volume
backoff and will be reported on the Pod reason and message.

The types of objects that may be mounted by this volume are defined by the
container runtime implementation on a host machine. At a minimum, they must include
all valid types supported by the container image field. The OCI object gets
mounted in a single directory (`spec.containers[*].volumeMounts[*].mountPath`)
and will be mounted read-only.

Besides that:

- [`subPath`](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) or
  [`subPathExpr`](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath-expanded-environment)
  mounts for containers (`spec.containers[*].volumeMounts[*].subPath`, `spec.containers[*].volumeMounts[*].subPathExpr`)
  are only supported from Kubernetes v1.33.
- The field `spec.securityContext.fsGroupChangePolicy` has no effect on this
  volume type.
- The [`AlwaysPullImages` Admission Controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#alwayspullimages)
  does also work for this volume source like for container images.

The following fields are available for the `image` type:

`reference`
:   Artifact reference to be used. For example, you could specify
    `registry.k8s.io/conformance:v1.36.0` to load the
    files from the Kubernetes conformance test image. Behaves in the same way as
    `pod.spec.containers[*].image`. Pull secrets will be assembled in the same way
    as for the container image by looking up node credentials, service account image
    pull secrets, and Pod spec image pull secrets. This field is optional to allow
    higher level config management to default or override container images in
    workload controllers like Deployments and StatefulSets.
    [More info about container images](https://kubernetes.io/docs/concepts/containers/images/).

`pullPolicy`
:   Policy for pulling OCI objects. Possible values are: `Always`, `Never`, or
    `IfNotPresent`. Defaults to `Always` if `:latest` tag is specified, or
    `IfNotPresent` otherwise.

See the [*Use an Image Volume With a Pod*](https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/)
example for more details on how to use the volume source.

#### Pod status and `image` volumes

F