---
id: kubernetes-use-a-high-availability-deployment-model-137dc105
type: concept
title: Use a high-availability deployment model
description: Consider your cluster's availability requirements when designing your
  webhook.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Use a high-availability deployment model

Consider your cluster's availability requirements when designing your webhook.
For example, during node downtime or zonal outages, Kubernetes marks Pods as
`NotReady` to allow load balancers to reroute traffic to available zones and
nodes. These updates to Pods might trigger your mutating webhooks. Depending on
the number of affected Pods, the mutating webhook server has a risk of timing
out or causing delays in Pod processing. As a result, traffic won't get
rerouted as quickly as you need.

Consider situations like the preceding example when writing your webhooks.
Exclude operations that are a result of Kubernetes responding to unavoidable
incidents.