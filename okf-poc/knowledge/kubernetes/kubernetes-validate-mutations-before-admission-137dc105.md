---
id: kubernetes-validate-mutations-before-admission-137dc105
type: concept
title: Validate mutations before admission
description: Mutating webhooks run to completion before any validating webhooks run.
  There is
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Validate mutations before admission

Mutating webhooks run to completion before any validating webhooks run. There is
no stable order in which mutations are applied to objects. As a result, your
mutations could get overwritten by a mutating webhook that runs at a later time.

Add a validating admission controller like a ValidatingAdmissionWebhook or a
ValidatingAdmissionPolicy to your cluster to ensure that your mutations
are still present. For example, consider a mutating webhook that inserts the
`restartPolicy: Always` field to specific init containers to make them run as
sidecar containers. You could run a validating webhook to ensure that those
init containers retained the `restartPolicy: Always` configuration after all
mutations were completed.

For details, see the following resources:

- [Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
- [ValidatingAdmissionWebhooks](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)