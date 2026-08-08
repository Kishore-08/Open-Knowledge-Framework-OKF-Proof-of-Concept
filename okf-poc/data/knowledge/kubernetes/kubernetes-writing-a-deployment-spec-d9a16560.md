---
id: kubernetes-writing-a-deployment-spec-d9a16560
type: concept
title: Writing a Deployment Spec
description: As with all other Kubernetes configs, a Deployment needs `.apiVersion`,
  `.kind`, and `.metadata` fields.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Writing a Deployment Spec

As with all other Kubernetes configs, a Deployment needs `.apiVersion`, `.kind`, and `.metadata` fields.
For general information about working with config files, see
[deploying applications](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/),
configuring containers, and [using kubectl to manage resources](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/) documents.

When the control plane creates new Pods for a Deployment, the `.metadata.name` of the
Deployment is part of the basis for naming those Pods. The name of a Deployment must be a valid
[DNS subdomain](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names)
value, but this can produce unexpected results for the Pod hostnames. For best compatibility,
the name should follow the more restrictive rules for a
[DNS label](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).

A Deployment also needs a [`.spec` section](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).