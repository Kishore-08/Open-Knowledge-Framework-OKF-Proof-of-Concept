---
id: kubernetes-authenticating-service-account-credentials-2e4cf2b5
type: concept
title: Authenticating service account credentials
description: ServiceAccounts use signed
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/service-accounts/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Authenticating service account credentials

ServiceAccounts use signed
[JSON Web Tokens](https://www.rfc-editor.org/rfc/rfc7519 "A means of representing claims to be transferred between two parties.") (JWTs)
to authenticate to the Kubernetes API server, and to any other system where a
trust relationship exists. Depending on how the token was issued
(either time-limited using a `TokenRequest` or using a legacy mechanism with
a Secret), a ServiceAccount token might also have an expiry time, an audience,
and a time after which the token *starts* being valid. When a client that is
acting as a ServiceAccount tries to communicate with the Kubernetes API server,
the client includes an `Authorization: Bearer <token>` header with the HTTP
request. The API server checks the validity of that bearer token as follows:

1. Checks the token signature.
2. Checks whether the token has expired.
3. Checks whether object references in the token claims are currently valid.
4. Checks whether the token is currently valid.
5. Checks the audience claims.

The TokenRequest API produces *bound tokens* for a ServiceAccount. This
binding is linked to the lifetime of the client, such as a Pod, that is acting
as that ServiceAccount. See [Token Volume Projection](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#serviceaccount-token-volume-projection)
for an example of a bound pod service account token's JWT schema and payload.

For tokens issued using the `TokenRequest` API, the API server also checks that
the specific object reference that is using the ServiceAccount still exists,
matching by the [unique ID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names "A Kubernetes systems-generated string to uniquely identify objects.") of that
object. For legacy tokens that are mounted as Secrets in Pods, the API server
checks the token against the Secret.

For more information about the authentication process, refer to
[Authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens).