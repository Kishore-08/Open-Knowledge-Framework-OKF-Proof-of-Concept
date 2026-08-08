---
id: kubernetes-authenticating-service-account-credentials-in-your-own-code-2e4cf2b5
type: concept
title: Authenticating service account credentials in your own code
description: If you have services of your own that need to validate Kubernetes service
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/service-accounts/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Authenticating service account credentials in your own code

If you have services of your own that need to validate Kubernetes service
account credentials, you can use the following methods:

- [TokenReview API](https://kubernetes.io/docs/reference/kubernetes-api/authentication-resources/token-review-v1/)
  (recommended)
- OIDC discovery

The Kubernetes project recommends that you use the TokenReview API, because
this method invalidates tokens that are bound to API objects such as Secrets,
ServiceAccounts, Pods or Nodes when those objects are deleted. For example, if you
delete the Pod that contains a projected ServiceAccount token, the cluster
invalidates that token immediately and a TokenReview immediately fails.
If you use OIDC validation instead, your clients continue to treat the token
as valid until the token reaches its expiration timestamp.

Your application should always define the audience that it accepts, and should
check that the token's audiences match the audiences that the application
expects. This helps to minimize the scope of the token so that it can only be
used in your application and nowhere else.