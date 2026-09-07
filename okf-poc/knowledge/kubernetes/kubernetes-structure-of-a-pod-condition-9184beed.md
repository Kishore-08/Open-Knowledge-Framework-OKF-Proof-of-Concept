---
id: kubernetes-structure-of-a-pod-condition-9184beed
type: concept
title: Structure of a Pod condition
description: A Pod's status includes an array of
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Structure of a Pod condition

A Pod's status includes an array of
[PodConditions](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#podcondition-v1-core)
that indicate whether the Pod has passed certain checkpoints.

Each element of the PodCondition array has the following fields:

Fields of a PodCondition

| Field name | Description |
| --- | --- |
| `type` | Name of this Pod condition. |
| `status` | Indicates whether that condition is applicable, with possible values `"True"`, `"False"`, or `"Unknown"`. |
| `lastProbeTime` | Timestamp of when the Pod condition was last probed. |
| `lastTransitionTime` | Timestamp for when the Pod last transitioned from one status to another. |
| `reason` | Machine-readable, UpperCamelCase text indicating the reason for the condition's last transition. |
| `message` | Human-readable message indicating details about the last status transition. |
| `observedGeneration` | The `.metadata.generation` of the Pod at the time the condition was recorded. See [Pod generation](https://kubernetes.io/docs/concepts/workloads/pods/#pod-generation). |