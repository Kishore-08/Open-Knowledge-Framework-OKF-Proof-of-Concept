---
id: kubernetes-the-workloadbuilder-library-497d3b3e
type: concept
title: The workloadbuilder library
description: '`workloadbuilder` is a shared Go library that turns a controller''s
  scheduling intent into'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## The workloadbuilder library

`workloadbuilder` is a shared Go library that turns a controller's scheduling intent into
the scheduler-facing Workload and its runtime PodGroup/CompositePodGroup objects, so each
controller does not reimplement defaulting, validation, and template compilation. It is designed for both
in-tree controllers (such as the Job controller) and out-of-tree controllers (such as
JobSet or Kubeflow TrainJob), which vendor it like any other Go dependency. It ships from
`k8s.io/component-helpers/scheduling/schedulingv1/workloadbuilder`.

The library consumes the `scheduling.k8s.io/v1alpha3` building blocks and compiles them into
`scheduling.k8s.io/v1beta1` Workload and PodGroup objects, while CompositePodGroup
objects remain `scheduling.k8s.io/v1alpha3`.