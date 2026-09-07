---
id: kubernetes-update-strategies-f82fae6f
type: concept
title: Update strategies
description: A StatefulSet's `.spec.updateStrategy` field allows you to configure
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Update strategies

A StatefulSet's `.spec.updateStrategy` field allows you to configure
and disable automated rolling updates for containers, labels, resource request/limits, and
annotations for the Pods in a StatefulSet. There are three possible values:

`OnDelete`
:   When a StatefulSet's `.spec.updateStrategy.type` is set to `OnDelete`,
    the StatefulSet controller will not automatically update the Pods in a
    StatefulSet. Users must manually delete Pods to cause the controller to
    create new Pods that reflect modifications made to a StatefulSet's `.spec.template`.

`RollingUpdate`
:   The `RollingUpdate` update strategy implements automated, rolling updates for the Pods in a
    StatefulSet. This is the default update strategy.

`Recreate`
:   FEATURE STATE:
    `Kubernetes v1.37 [alpha]`(disabled by default)

    The `Recreate` update strategy deletes all of the StatefulSet's Pods before creating new
    Pods that reflect modifications made to a StatefulSet's `.spec.template`. Using this
    strategy requires the `StatefulSetRecreateStrategy`
    [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#StatefulSetRecreateStrategy)
    to be enabled. See [Recreate](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#recreate) for details.