---
id: kubernetes-secret-4142258a
type: concept
title: secret
description: A `secret` volume is used to pass sensitive information, such as passwords,
  to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### secret

A `secret` volume is used to pass sensitive information, such as passwords, to
Pods. You can store secrets in the Kubernetes API and mount them as files for
use by Pods without coupling to Kubernetes directly. `secret` volumes are
backed by tmpfs (a RAM-backed filesystem), so they are never written to
non-volatile storage.

#### Note:

- You must create a Secret in the Kubernetes API before you can use it.
- A Secret is always mounted as `readOnly`.
- A container using a Secret as a [`subPath`](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath) volume mount will not
  receive Secret updates.

For more details, see [Configuring Secrets](https://kubernetes.io/docs/concepts/configuration/secret/).