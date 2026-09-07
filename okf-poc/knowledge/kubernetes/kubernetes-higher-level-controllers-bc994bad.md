---
id: kubernetes-higher-level-controllers-bc994bad
type: concept
title: Higher-level controllers
description: For a standalone Job, the Job controller owns both the `Workload` and
  the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Higher-level controllers

For a standalone Job, the Job controller owns both the `Workload` and the
`PodGroup`. When a Job instead carries an `ownerReference` to a parent controller
that compiles the `Workload` (for example, `JobSet`), the Job controller defers
`Workload` ownership to that parent. Whether the Job controller still creates the
runtime `PodGroup` depends on what the parent delegates:

- If the parent sets the `scheduling.k8s.io/group-template-name` annotation on the
  Job, the Job controller creates and owns the `PodGroup`, mapped to the parent's
  named `PodGroupTemplate`.
- Otherwise, the parent owns both objects and the Job controller creates neither;
  it discovers the existing objects and uses them when creating Pods.

If a Job's Pod template already has `.spec.template.spec.schedulingGroup` set, the
Job controller creates neither object, letting you (or a higher-level controller)
manage the `Workload`/`PodGroup` lifecycle yourself.