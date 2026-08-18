---
id: kubernetes-identify-whether-you-use-admission-webhooks-137dc105
type: concept
title: Identify whether you use admission webhooks
description: Even if you don't run your own admission webhooks, some third-party applications
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Identify whether you use admission webhooks

Even if you don't run your own admission webhooks, some third-party applications
that you run in your clusters might use mutating or validating admission
webhooks.

To check whether your cluster has any mutating admission webhooks, run the
following command:

```
kubectl get mutatingwebhookconfigurations
```

The output lists any mutating admission controllers in the cluster.

To check whether your cluster has any validating admission webhooks, run the
following command:

```
kubectl get validatingwebhookconfigurations
```

The output lists any validating admission controllers in the cluster.