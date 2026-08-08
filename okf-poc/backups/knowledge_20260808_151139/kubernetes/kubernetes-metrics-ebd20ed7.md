---
id: kubernetes-metrics-ebd20ed7
type: concept
title: Metrics
description: 'Here are the Prometheus metrics exposed by kube-apiserver:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Metrics

Here are the Prometheus metrics exposed by kube-apiserver:

- `pod_security_errors_total`: This metric indicates the number of errors preventing normal evaluation.
  Non-fatal errors may result in the latest restricted profile being used for enforcement.
- `pod_security_evaluations_total`: This metric indicates the number of policy evaluations that have occurred,
  not counting ignored or exempt requests during exporting.
- `pod_security_exemptions_total`: This metric indicates the number of exempt requests, not counting ignored
  or out of scope requests.