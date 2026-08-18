---
id: kubernetes-install-and-enable-a-mutating-webhook-137dc105
type: concept
title: Install and enable a mutating webhook
description: When you're ready to deploy your mutating webhook to a cluster, use the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Install and enable a mutating webhook

When you're ready to deploy your mutating webhook to a cluster, use the
following order of operations:

1. Install the webhook server and start it.
2. Set the `failurePolicy` field in the MutatingWebhookConfiguration manifest
   to Ignore. This lets you avoid disruptions caused by misconfigured webhooks.
3. Set the `namespaceSelector` field in the MutatingWebhookConfiguration
   manifest to a test namespace.
4. Deploy the MutatingWebhookConfiguration to your cluster.

Monitor the webhook in the test namespace to check for any issues, then roll the
webhook out to other namespaces. If the webhook intercepts an API request that
it wasn't meant to intercept, pause the rollout and adjust the scope of the
webhook configuration.