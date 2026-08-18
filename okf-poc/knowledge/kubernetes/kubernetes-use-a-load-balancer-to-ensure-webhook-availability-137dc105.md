---
id: kubernetes-use-a-load-balancer-to-ensure-webhook-availability-137dc105
type: concept
title: Use a load balancer to ensure webhook availability
description: Admission webhooks should leverage some form of load-balancing to provide
  high
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Use a load balancer to ensure webhook availability

Admission webhooks should leverage some form of load-balancing to provide high
availability and performance benefits. If a webhook is running within the
cluster, you can run multiple webhook backends behind a Service of type
`ClusterIP`.