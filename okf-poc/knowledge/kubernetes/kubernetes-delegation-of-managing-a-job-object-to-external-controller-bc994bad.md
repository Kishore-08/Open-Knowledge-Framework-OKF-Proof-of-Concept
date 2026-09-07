---
id: kubernetes-delegation-of-managing-a-job-object-to-external-controller-bc994bad
type: concept
title: Delegation of managing a Job object to external controller
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Delegation of managing a Job object to external controller

FEATURE STATE:
`Kubernetes v1.35 [stable]`(enabled by default)

This feature allows you to disable the built-in Job controller, for a specific
Job, and delegate reconciliation of the Job to an external controller.

You indicate the controller that reconciles the Job by setting a custom value
for the `spec.managedBy` field - any value
other than `kubernetes.io/job-controller`. The value of the field is immutable.

#### Note:

When using this feature, make sure the controller indicated by the field is
installed, otherwise the Job may not be reconciled at all.

#### Note:

When developing an external Job controller be aware that your controller needs
to operate in a fashion conformant with the definitions of the API spec and
status fields of the Job object.

Please review these in detail in the [Job API](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/job-v1/).
We also recommend that you run the e2e conformance tests for the Job object to
verify your implementation.

Finally, when developing an external Job controller make sure it does not use the
`batch.kubernetes.io/job-tracking` finalizer, reserved for the built-in controller.

## Alternatives