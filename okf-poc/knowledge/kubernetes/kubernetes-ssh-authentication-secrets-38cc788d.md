---
id: kubernetes-ssh-authentication-secrets-38cc788d
type: concept
title: SSH authentication Secrets
description: The builtin type `kubernetes.io/ssh-auth` is provided for storing data
  used in
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### SSH authentication Secrets

The builtin type `kubernetes.io/ssh-auth` is provided for storing data used in
SSH authentication. When using this Secret type, you will have to specify a
`ssh-privatekey` key-value pair in the `data` (or `stringData`) field
as the SSH credential to use.

The following manifest is an example of a Secret used for SSH public/private
key authentication:

[`secret/ssh-auth-secret.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/secret/ssh-auth-secret.yaml)![](https://kubernetes.io/images/copycode.svg "Copy secret/ssh-auth-secret.yaml to clipboard")

```
apiVersion: v1
kind: Secret
metadata:
  name: secret-ssh-auth
type: kubernetes.io/ssh-auth
data:
  # the data is abbreviated in this example
  ssh-privatekey: |
    UG91cmluZzYlRW1vdGljb24lU2N1YmE=
```

The SSH authentication Secret type is provided only for convenience.
You can create an `Opaque` type for credentials used for SSH authentication.
However, using the defined and public Secret type (`kubernetes.io/ssh-auth`) helps other
people to understand the purpose of your Secret, and sets a convention for what key names
to expect.
The Kubernetes API verifies that the required keys are set for a Secret of this type.

#### Caution:

SSH private keys do not establish trusted communication between an SSH client and
host server on their own. A secondary means of establishing trust is needed to
mitigate "man in the middle" attacks, such as a `known_hosts` file added to a ConfigMap.