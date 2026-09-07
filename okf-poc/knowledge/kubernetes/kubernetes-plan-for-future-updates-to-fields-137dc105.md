---
id: kubernetes-plan-for-future-updates-to-fields-137dc105
type: concept
title: Plan for future updates to fields
description: In general, design your webhooks under the assumption that Kubernetes
  APIs might
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Plan for future updates to fields

In general, design your webhooks under the assumption that Kubernetes APIs might
change in a later version. Don't write a server that takes the stability of an
API for granted. For example, the release of sidecar containers in Kubernetes
added a `restartPolicy` field to the Pod API.