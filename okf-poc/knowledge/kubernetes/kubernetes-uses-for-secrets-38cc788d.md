---
id: kubernetes-uses-for-secrets-38cc788d
type: concept
title: Uses for Secrets
description: 'You can use Secrets for purposes such as the following:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Uses for Secrets

You can use Secrets for purposes such as the following:

- [Set environment variables for a container](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data).
- [Provide credentials such as SSH keys or passwords to Pods](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#provide-prod-test-creds).
- [Allow the kubelet to pull container images from private registries](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/).

The Kubernetes control plane also uses Secrets; for example,
[bootstrap token Secrets](https://kubernetes.io/docs/concepts/configuration/secret/#bootstrap-token-secrets) are a mechanism to
help automate node registration.