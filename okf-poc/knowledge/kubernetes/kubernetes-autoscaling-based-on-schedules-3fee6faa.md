---
id: kubernetes-autoscaling-based-on-schedules-3fee6faa
type: concept
title: Autoscaling based on schedules
description: Another strategy for scaling your workloads is to **schedule** the scaling
  operations, for example in order to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Autoscaling based on schedules

Another strategy for scaling your workloads is to **schedule** the scaling operations, for example in order to
reduce resource consumption during off-peak hours.

Similar to event driven autoscaling, such behavior can be achieved using KEDA in conjunction with
its [`Cron` scaler](https://keda.sh/docs/latest/scalers/cron/).
The `Cron` scaler allows you to define schedules (and time zones) for scaling your workloads in or out.