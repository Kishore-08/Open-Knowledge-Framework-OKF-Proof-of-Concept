---
id: kubernetes-csrs-and-certificate-issuing-f9926ce8
type: concept
title: CSRs and certificate issuing
description: The CSR API allows for users with `create` rights to CSRs and `update`
  rights on `certificatesigningrequests/approval`
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### CSRs and certificate issuing

The CSR API allows for users with `create` rights to CSRs and `update` rights on `certificatesigningrequests/approval`
where the signer is `kubernetes.io/kube-apiserver-client` to create new client certificates
which allow users to authenticate to the cluster. Those client certificates can have arbitrary
names including duplicates of Kubernetes system components. This will effectively allow for privilege escalation.

### Token request

Users with `create` rights on `serviceaccounts/token` can create TokenRequests to issue
tokens for existing service accounts.