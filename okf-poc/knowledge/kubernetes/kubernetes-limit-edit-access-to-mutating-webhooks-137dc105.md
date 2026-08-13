---
id: kubernetes-limit-edit-access-to-mutating-webhooks-137dc105
type: concept
title: Limit edit access to mutating webhooks
description: Mutating webhooks are powerful Kubernetes controllers. Use RBAC or another
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Limit edit access to mutating webhooks

Mutating webhooks are powerful Kubernetes controllers. Use RBAC or another
authorization mechanism to limit access to your webhook configurations and
servers. For RBAC, ensure that the following access is only available to trusted
entities:

- Verbs: **create**, **update**, **patch**, **delete**, **deletecollection**
- API group: `admissionregistration.k8s.io/v1`
- API kind: MutatingWebhookConfigurations

If your mutating webhook server runs in the cluster, limit access to create or
modify any resources in that namespace.