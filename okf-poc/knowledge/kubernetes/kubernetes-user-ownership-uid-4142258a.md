---
id: kubernetes-user-ownership-uid-4142258a
type: concept
title: User ownership (UID)
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### User ownership (UID)

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

Setting the `AtomicWriteVolumeUserFields` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
enables file user ownership (UID) fields of `configMap`, `secret`, `downwardAPI` and `projected` volumes.

When `defaultUser` is specified at the volume level, it sets the owner UID for all its data files at creation time.
At the item level, the `user` field controls owner UID of an individual file and takes precedence over `defaultUser`.

Example:

```
apiVersion: v1
kind: Pod
metadata:
  name: volume-user-fields-example
spec:
  containers:
  - name: test
    image: busybox:1.28
    command: ['sh', '-c', 'echo "The app is running!" && tail -f /dev/null']
    volumeMounts:
    - name: volA
      mountPath: /mnt/volA
    - name: volB
      mountPath: /mnt/volB
    - name: volC
      mountPath: /mnt/volC
  volumes:
  - name: volA
    configMap:
      defaultUser: 1000
      name: cm1
      items:
      - key: foo # Owner=defaultUser
        path: foo
      - key: bar # Owner=user
        path: bar
        user: 1001
  - name: volB
    secret: # Owner=defaultUser
      defaultUser: 1000
      secretName: secret1
  - name: volC
    projected:
      sources:
      - secret:
          name: secret2
          items:
          - key: moo # Owner=root
            path: moo
          - key: baa # Owner=user
            path: baa
            user: 1000
```

#### Implementations

**Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/storage/volumes/#third-party-content-disclaimer)

The following container runtimes are known to support recursive read-only mounts.

CRI-level:

- [containerd](https://containerd.io/), since v2.0
- [CRI-O](https://cri-o.io/), since v1.30

OCI-level:

- [runc](https://runc.io/), since v1.1
- [crun](https://github.com/containers/crun), since v1.8.6