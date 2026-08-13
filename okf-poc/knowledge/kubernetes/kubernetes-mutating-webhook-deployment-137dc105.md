---
id: kubernetes-mutating-webhook-deployment-137dc105
type: concept
title: Mutating webhook deployment
description: This section provides recommendations for deploying your mutating admission
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Mutating webhook deployment

This section provides recommendations for deploying your mutating admission
webhooks. In summary, these are as follows:

- Gradually roll out the webhook configuration and monitor for issues by
  namespace.
- Limit access to edit the webhook configuration resources.
- Limit access to the namespace that runs the webhook server, if the server is
  in-cluster.