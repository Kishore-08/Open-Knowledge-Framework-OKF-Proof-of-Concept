---
id: kubernetes-ensure-that-the-mutating-webhooks-in-your-cluster-are-idempo-137dc105
type: concept
title: Ensure that the mutating webhooks in your cluster are idempotent
description: Every mutating admission webhook should be *idempotent*. The webhook
  should be
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Ensure that the mutating webhooks in your cluster are idempotent

Every mutating admission webhook should be *idempotent*. The webhook should be
able to run on an object that it already modified without making additional
changes beyond the original change.

Additionally, all of the mutating webhooks in your cluster should, as a
collection, be idempotent. After the mutation phase of admission control ends,
every individual mutating webhook should be able to run on an object without
making additional changes to the object.

Depending on your environment, ensuring idempotence at scale might be
challenging. The following recommendations might help:

- Use validating admission controllers to verify the final state of
  critical workloads.
- Test your deployments in a staging cluster to see if any objects get modified
  multiple times by the same webhook.
- Ensure that the scope of each mutating webhook is specific and limited.

The following examples show idempotent mutation logic:

1. For a **create** Pod request, set the field
   `.spec.securityContext.runAsNonRoot` of the Pod to true.
2. For a **create** Pod request, if the field
   `.spec.containers[].resources.limits` of a container is not set, set default
   resource limits.
3. For a **create** Pod request, inject a sidecar container with name
   `foo-sidecar` if no container with the name `foo-sidecar` already exists.

In these cases, the webhook can be safely reinvoked, or admit an object that
already has the fields set.

The following examples show non-idempotent mutation logic:

1. For a **create** Pod request, inject a sidecar container with name
   `foo-sidecar` suffixed with the current timestamp (such as
   `foo-sidecar-19700101-000000`).

   Reinvoking the webhook can result in the same sidecar being injected multiple
   times to a Pod, each time with a different container name. Similarly, the
   webhook can inject duplicated containers if the sidecar already exists in
   a user-provided pod.
2. For a **create**/**update** Pod request, reject if the Pod has label `env`
   set, otherwise add an `env: prod` label to the Pod.

   Reinvoking the webhook will result in the webhook failing on its own output.
3. For a **create** Pod request, append a sidecar container named `foo-sidecar`
   without checking whether a `foo-sidecar` container exists.

   Reinvoking the webhook will result in duplicated containers in the Pod, which
   makes the request invalid and rejected by the API server.