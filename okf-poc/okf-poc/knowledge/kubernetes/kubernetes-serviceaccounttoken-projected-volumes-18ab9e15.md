---
id: kubernetes-serviceaccounttoken-projected-volumes-18ab9e15
type: concept
title: serviceAccountToken projected volumes
description: You can inject the token for the current [service account](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## serviceAccountToken projected volumes

You can inject the token for the current [service account](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens)
into a Pod at a specified path. For example:

[`pods/storage/projected-service-account-token.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/pods/storage/projected-service-account-token.yaml)![](https://kubernetes.io/images/copycode.svg "Copy pods/storage/projected-service-account-token.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: sa-token-test
spec:
  containers:
  - name: container-test
    image: busybox:1.28
    command: ["sleep", "3600"]
    volumeMounts:
    - name: token-vol
      mountPath: "/service-account"
      readOnly: true
  serviceAccountName: default
  volumes:
  - name: token-vol
    projected:
      sources:
      - serviceAccountToken:
          audience: api
          expirationSeconds: 3600
          path: token
```

The example Pod has a projected volume containing the injected service account
token. Containers in this Pod can use that token to access the Kubernetes API
server, authenticating with the identity of [the pod's ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/).
The `audience` field contains the intended audience of the
token. A recipient of the token must identify itself with an identifier specified
in the audience of the token, and otherwise should reject the token. This field
is optional and it defaults to the identifier of the API server.

The `expirationSeconds` is the expected duration of validity of the service account
token. It defaults to 1 hour and must be at least 10 minutes (600 seconds). An administrator
can also limit its maximum value by specifying the `--service-account-max-token-expiration`
option for the API server. The `path` field specifies a relative path to the mount point
of the projected volume.

#### Note:

A container using a projected volume source as a [`subPath`](https://kubernetes.io/docs/concepts/storage/volumes/#using-subpath)
volume mount will not receive updates for those volume sources.