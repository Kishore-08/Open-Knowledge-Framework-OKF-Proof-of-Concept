---
id: kubernetes-assign-a-serviceaccount-to-a-pod-2e4cf2b5
type: concept
title: Assign a ServiceAccount to a Pod
description: To assign a ServiceAccount to a Pod, you set the `spec.serviceAccountName`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/service-accounts/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Assign a ServiceAccount to a Pod

To assign a ServiceAccount to a Pod, you set the `spec.serviceAccountName`
field in the Pod specification. Kubernetes then automatically provides the
credentials for that ServiceAccount to the Pod. In v1.22 and later, Kubernetes
gets a short-lived, **automatically rotating** token using the `TokenRequest`
API and mounts the token as a
[projected volume](https://kubernetes.io/docs/concepts/storage/projected-volumes/#serviceaccounttoken).

By default, Kubernetes provides the Pod
with the credentials for an assigned ServiceAccount, whether that is the
`default` ServiceAccount or a custom ServiceAccount that you specify.

To prevent Kubernetes from automatically injecting
credentials for a specified ServiceAccount or the `default` ServiceAccount, set the
`automountServiceAccountToken` field in your Pod specification to `false`.

In versions earlier than 1.22, Kubernetes provides a long-lived, static token
to the Pod as a Secret.

#### Manually retrieve ServiceAccount credentials

If you need the credentials for a ServiceAccount to mount in a non-standard
location, or for an audience that isn't the API server, use one of the
following methods:

- [TokenRequest API](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-request-v1/)
  (recommended): Request a short-lived service account token from within
  your own *application code*. The token expires automatically and can rotate
  upon expiration.
  If you have a legacy application that is not aware of Kubernetes, you
  could use a sidecar container within the same pod to fetch these tokens
  and make them available to the application workload.
- [Token Volume Projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection)
  (also recommended): In Kubernetes v1.20 and later, use the Pod specification to
  tell the kubelet to add the service account token to the Pod as a
  *projected volume*. Projected tokens expire automatically, and the kubelet
  rotates the token before it expires.
- [Service Account Token Secrets](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#manually-create-an-api-token-for-a-serviceaccount)
  (not recommended): You can mount service account tokens as Kubernetes
  Secrets in Pods. These tokens don't expire and don't rotate. In versions prior to v1.24, a permanent token was automatically created for each service account.
  This method is not recommended anymore, especially at scale, because of the risks associated
  with static, long-lived credentials. The [LegacyServiceAccountTokenNoAutoGeneration feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates-removed/)
  (which was enabled by default from Kubernetes v1.24 to v1.26), prevented Kubernetes from automatically creating these tokens for
  ServiceAccounts. The feature gate is removed in v1.27, because it was elevated to GA status; you can still create indefinite service account tokens manually, but should take into account the security implications.

#### Node audience restriction for service account tokens

FEATURE STATE:
`Kubernetes v1.33 [beta]`(enabled by default)

When the `ServiceAccountNodeAudienceRestriction` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/)
is enabled, the [NodeRestriction](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction)
admission plugin limits which audiences a kubelet can request when creating service
account tokens via the `TokenRequest` API. By default, the kubelet can only request
tokens for audiences already referenced by pods on that node (through projected service
account token volumes or CSI driver token requests). Administrators can grant
kubelets access to additional audiences using RBAC rules with the
`request-serviceaccounts-token-audience` verb.

This restriction a