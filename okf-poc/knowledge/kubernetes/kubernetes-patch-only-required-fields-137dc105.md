---
id: kubernetes-patch-only-required-fields-137dc105
type: concept
title: Patch only required fields
description: Admission webhook servers send HTTP responses to indicate what to do
  with a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Patch only required fields

Admission webhook servers send HTTP responses to indicate what to do with a
specific Kubernetes API request. This response is an AdmissionReview object.
A mutating webhook can add specific fields to mutate before allowing admission
by using the `patchType` field and the `patch` field in the response. Ensure
that you only modify the fields that require a change.

For example, consider a mutating webhook that's configured to ensure that
`web-server` Deployments have at least three replicas. When a request to
create a Deployment object matches your webhook configuration, the webhook
should only update the value in the `spec.replicas` field.