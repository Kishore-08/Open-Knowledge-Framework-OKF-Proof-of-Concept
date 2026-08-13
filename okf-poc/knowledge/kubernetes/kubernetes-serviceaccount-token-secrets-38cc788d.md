---
id: kubernetes-serviceaccount-token-secrets-38cc788d
type: concept
title: ServiceAccount token Secrets
description: A `kubernetes.io/service-account-token` type of Secret is used to store
  a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### ServiceAccount token Secrets

A `kubernetes.io/service-account-token` type of Secret is used to store a
token credential that identifies a
[ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/ "Provides an identity for processes that run in a Pod."). This
is a legacy mechanism that provides long-lived ServiceAccount credentials to
Pods.

In Kubernetes v1.22 and later, the recommended approach is to obtain a
short-lived, automatically rotating ServiceAccount token by using the
[`TokenRequest`](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
API instead. You can get these short-lived tokens using the following methods:

- Call the `TokenRequest` API either directly or by using an API client like
  `kubectl`. For example, you can use the
  [`kubectl create token`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-token-em-)
  command.
- Request a mounted token in a
  [projected volume](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume)
  in your Pod manifest. Kubernetes creates the token and mounts it in the Pod.
  The token is automatically invalidated when the Pod that it's mounted in is
  deleted. For details, see
  [Launch a Pod using service account token projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#launch-a-pod-using-service-account-token-projection).

#### Note:

You should only create a ServiceAccount token Secret
if you can't use the `TokenRequest` API to obtain a token,
and the security exposure of persisting a non-expiring token credential
in a readable API object is acceptable to you. For instructions, see
[Manually create a long-lived API token for a ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount).

When using this Secret type, you need to ensure that the
`kubernetes.io/service-account.name` annotation is set to an existing
ServiceAccount name. If you are creating both the ServiceAccount and
the Secret objects, you should create the ServiceAccount object first.

After the Secret is created, a Kubernetes [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.")
fills in some other fields such as the `kubernetes.io/service-account.uid` annotation, and the
`token` key in the `data` field, which is populated with an authentication token.

The following example configuration declares a ServiceAccount token Secret:

[`secret/serviceaccount-token-secret.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/secret/serviceaccount-token-secret.yaml)![](https://kubernetes.io/images/copycode.svg "Copy secret/serviceaccount-token-secret.yaml to clipboard")

```
apiVersion: v1
kind: Secret
metadata:
  name: secret-sa-sample
  annotations:
    kubernetes.io/service-account.name: "sa-name"
type: kubernetes.io/service-account-token
data:
  extra: YmFyCg==
```

After creating the Secret, wait for Kubernetes to populate the `token` key in the `data` field.

See the [ServiceAccount](https://kubernetes.io/docs/concepts/security/service-accounts/)
documentation for more information on how ServiceAccounts work.
You can also check the `automountServiceAccountToken` field and the
`serviceAccountName` field of the
[`Pod`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.36/#pod-v1-core)
for information on referencing ServiceAccount credentials from within Pods.