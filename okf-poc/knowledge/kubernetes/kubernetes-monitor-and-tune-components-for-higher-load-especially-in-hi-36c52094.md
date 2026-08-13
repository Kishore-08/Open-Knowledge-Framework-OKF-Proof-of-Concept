---
id: kubernetes-monitor-and-tune-components-for-higher-load-especially-in-hi-36c52094
type: concept
title: Monitor and tune components for higher load, especially in high scale environments
description: Control plane component [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/
  "Control plane component that watches for newly created pods with no assigned
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Monitor and tune components for higher load, especially in high scale environments

Control plane component [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") and the internal ResourceClaim controller
orchestrated by the component [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/ "Control Plane component that runs controller processes.") do the
heavy lifting during scheduling of Pods with claims based on metadata stored in
the DRA APIs. Compared to non-DRA scheduled Pods, the number of API server
calls, memory, and CPU utilization needed by these components is increased for
Pods using DRA claims. In addition, node local components like the DRA driver
and kubelet utilize DRA APIs to allocated the hardware request at Pod sandbox
creation time. Especially in high scale environments where clusters have many
nodes, and/or deploy many workloads that heavily utilize DRA defined resource
claims, the cluster administrator should configure the relevant components to
anticipate the increased load.

The effects of mistuned components can have direct or snowballing affects
causing different symptoms during the Pod lifecycle. If the `kube-scheduler`
component's QPS and burst configurations are too low, the scheduler might
quickly identify a suitable node for a Pod but take longer to bind the Pod to
that node. With DRA, during Pod scheduling, the QPS and Burst parameters in the
client-go configuration within `kube-controller-manager` are critical.

The specific values to tune your cluster to depend on a variety of factors like
number of nodes/pods, rate of pod creation, churn, even in non-DRA environments;
see the [SIG Scalability README on Kubernetes scalability
thresholds](https://github.com/kubernetes/community/blob/main/sig-scalability/configs-and-limits/thresholds.md)
for more information. In scale tests performed against a DRA enabled cluster
with 100 nodes, involving 720 long-lived pods (90% saturation) and 80 churn pods
(10% churn, 10 times), with a job creation QPS of 10, `kube-controller-manager`
QPS could be set to as low as 75 and Burst to 150 to meet equivalent metric
targets for non-DRA deployments. At this lower bound, it was observed that the
client side rate limiter was triggered enough to protect the API server from
explosive burst but was high enough that pod startup SLOs were not impacted.
While this is a good starting point, you can get a better idea of how to tune
the different components that have the biggest effect on DRA performance for
your deployment by monitoring the following metrics. For more information on all
the stable metrics in Kubernetes, see the [Kubernetes Metrics
Reference](https://kubernetes.io/docs/reference/instrumentation/metrics/).