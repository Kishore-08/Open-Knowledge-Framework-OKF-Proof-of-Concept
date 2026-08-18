---
id: kubernetes-fail-open-and-validate-the-final-state-137dc105
type: concept
title: Fail open and validate the final state
description: Mutating admission webhooks support the `failurePolicy` configuration
  field.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Fail open and validate the final state

Mutating admission webhooks support the `failurePolicy` configuration field.
This field indicates whether the API server should admit or reject the request
if the webhook fails. Webhook failures might occur because of timeouts or errors
in the server logic.

By default, admission webhooks set the `failurePolicy` field to Fail. The API
server rejects a request if the webhook fails. However, rejecting requests by
default might result in compliant requests being rejected during webhook
downtime.

Let your mutating webhooks "fail open" by setting the `failurePolicy` field to
Ignore. Use a validating controller to check the state of requests to ensure
that they comply with your policies.

This approach has the following benefits:

- Mutating webhook downtime doesn't affect compliant resources from deploying.
- Policy enforcement occurs during validating admission control.
- Mutating webhooks don't interfere with other controllers in the cluster.