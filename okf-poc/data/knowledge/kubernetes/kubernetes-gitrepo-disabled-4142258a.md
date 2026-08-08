---
id: kubernetes-gitrepo-disabled-4142258a
type: concept
title: gitRepo (disabled)
description: Kubernetes 1.36 does *not* include the `gitRepo` volume
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### gitRepo (disabled)

#### Warning:

Kubernetes 1.36 does *not* include the `gitRepo` volume
driver. The last version that provided a way to use this driver was Kubernetes
v1.35, and it has been deprecated since the [v1.11](https://kubernetes.io/releases/1.11/) minor
release.

To provision a Pod that has a Git repository mounted, you can mount an
[`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) volume into an [init container](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
that clones the repo using Git, then mount the [EmptyDir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) into the Pod's container.

---

You can restrict the use of `gitRepo` volumes in your cluster using
[policies](https://kubernetes.io/docs/concepts/policy/), such as
[ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/).
You can use the following Common Expression Language (CEL) expression as
part of a policy to reject use of `gitRepo` volumes:

```
!has(object.spec.volumes) || !object.spec.volumes.exists(v, has(v.gitRepo))
```