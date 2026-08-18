---
id: kubernetes-performance-and-latency-137dc105
type: concept
title: Performance and latency
description: This section describes recommendations for improving performance and
  reducing
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Performance and latency

This section describes recommendations for improving performance and reducing
latency. In summary, these are as follows:

- Consolidate webhooks and limit the number of API calls per webhook.
- Use audit logs to check for webhooks that repeatedly do the same action.
- Use load balancing for webhook availability.
- Set a small timeout value for each webhook.
- Consider cluster availability needs during webhook design.