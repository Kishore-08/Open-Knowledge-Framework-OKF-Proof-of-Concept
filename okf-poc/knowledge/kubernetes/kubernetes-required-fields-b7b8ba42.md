---
id: kubernetes-required-fields-b7b8ba42
type: concept
title: Required Fields
description: As with all other Kubernetes config, a DaemonSet needs `apiVersion`,
  `kind`, and `metadata` fields. For
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Required Fields

As with all other Kubernetes config, a DaemonSet needs `apiVersion`, `kind`, and `metadata` fields. For
general information about working with config files, see
[running stateless applications](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)
and [object management using kubectl](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/).

The name of a DaemonSet object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

A DaemonSet also needs a
[`.spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status)
section.