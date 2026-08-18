---
id: kubernetes-writing-a-job-spec-bc994bad
type: concept
title: Writing a Job spec
description: As with all other Kubernetes config, a Job needs `apiVersion`, `kind`,
  and `metadata` fields.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Writing a Job spec

As with all other Kubernetes config, a Job needs `apiVersion`, `kind`, and `metadata` fields.

When the control plane creates new Pods for a Job, the `.metadata.name` of the
Job is part of the basis for naming those Pods. The name of a Job must be a valid
[DNS subdomain](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names)
value, but this can produce unexpected results for the Pod hostnames. For best compatibility,
the name should follow the more restrictive rules for a
[DNS label](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).
Even when the name is a DNS subdomain, the name must be no longer than 63
characters.

A Job also needs a [`.spec` section](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).

### Job Labels

Job labels will have `batch.kubernetes.io/` prefix for `job-name` and `controller-uid`.