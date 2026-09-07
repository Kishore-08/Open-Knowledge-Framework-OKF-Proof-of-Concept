---
id: kubernetes-use-case-dotfiles-in-a-secret-volume-38cc788d
type: concept
title: 'Use case: dotfiles in a secret volume'
description: You can make your data "hidden" by defining a key that begins with a
  dot.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Use case: dotfiles in a secret volume

You can make your data "hidden" by defining a key that begins with a dot.
This key represents a dotfile or "hidden" file. For example, when the following Secret
is mounted into a volume, `secret-volume`, the volume will contain a single file,
called `.secret-file`, and the `dotfile-test-container` will have this file
present at the path `/etc/secret-volume/.secret-file`.

#### Note:

Files beginning with dot characters are hidden from the output of `ls -l`;
you must use `ls -la` to see them when listing directory contents.

[`secret/dotfile-secret.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/secret/dotfile-secret.yaml)![](https://kubernetes.io/images/copycode.svg "Copy secret/dotfile-secret.yaml to clipboard")

```
apiVersion: v1
kind: Secret
metadata:
  name: dotfile-secret
data:
  .secret-file: dmFsdWUtMg0KDQo=
---
apiVersion: v1
kind: Pod
metadata:
  name: secret-dotfiles-pod
spec:
  volumes:
    - name: secret-volume
      secret:
        secretName: dotfile-secret
  containers:
    - name: dotfile-test-container
      image: registry.k8s.io/busybox
      command:
        - ls
        - "-l"
        - "/etc/secret-volume"
      volumeMounts:
        - name: secret-volume
          readOnly: true
          mountPath: "/etc/secret-volume"
```