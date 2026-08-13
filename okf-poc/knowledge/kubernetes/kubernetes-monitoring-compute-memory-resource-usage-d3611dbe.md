---
id: kubernetes-monitoring-compute-memory-resource-usage-d3611dbe
type: concept
title: Monitoring compute & memory resource usage
description: The kubelet reports the resource usage of a Pod as part of the Pod
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Monitoring compute & memory resource usage

The kubelet reports the resource usage of a Pod as part of the Pod
[`status`](https://kubernetes.io/docs/concepts/overview/working-with-objects/#object-spec-and-status).

If optional [tools for monitoring](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-usage-monitoring/)
are available in your cluster, then Pod resource usage can be retrieved either
from the [Metrics API](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/#metrics-api)
directly or from your monitoring tools.