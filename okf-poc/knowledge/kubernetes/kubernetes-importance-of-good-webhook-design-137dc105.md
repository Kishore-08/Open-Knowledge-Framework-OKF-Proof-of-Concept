---
id: kubernetes-importance-of-good-webhook-design-137dc105
type: concept
title: Importance of good webhook design
description: Admission control occurs when any create, update, or delete request
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Importance of good webhook design

Admission control occurs when any create, update, or delete request
is sent to the Kubernetes API. Admission controllers intercept requests that
match specific criteria that you define. These requests are then sent to
mutating admission webhooks or validating admission webhooks. These webhooks are
often written to ensure that specific fields in object specifications exist or
have specific allowed values.

Webhooks are a powerful mechanism to extend the Kubernetes API. Badly-designed
webhooks often result in workload disruptions because of how much control
the webhooks have over objects in the cluster. Like other API extension
mechanisms, webhooks are challenging to test at scale for compatibility with
all of your workloads, other webhooks, add-ons, and plugins.

Additionally, with every release, Kubernetes adds or modifies the API with new
features, feature promotions to beta or stable status, and deprecations. Even
stable Kubernetes APIs are likely to change. For example, the `Pod` API changed
in v1.29 to add the
[Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) feature.
While it's rare for a Kubernetes object to enter a broken state because of a new
Kubernetes API, webhooks that worked as expected with earlier versions of an API
might not be able to reconcile more recent changes to that API. This can result
in unexpected behavior after you upgrade your clusters to newer versions.

This page describes common webhook failure scenarios and how to avoid them by
cautiously and thoughtfully designing and implementing your webhooks.