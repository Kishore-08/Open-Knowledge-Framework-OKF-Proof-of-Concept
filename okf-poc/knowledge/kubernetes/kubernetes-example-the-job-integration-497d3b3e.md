---
id: kubernetes-example-the-job-integration-497d3b3e
type: concept
title: 'Example: the Job integration'
description: The Job controller is the built-in example of these blocks in use. A
  user fills in a Job's
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Example: the Job integration

The Job controller is the built-in example of these blocks in use. A user fills in a Job's
`spec.scheduling`, and the controller compiles it into a Workload and PodGroup. See
[Integrate with Workload APIs](https://kubernetes.io/docs/concepts/workloads/controllers/job/#integrate-with-workload-apis)
for a complete Job manifest, the defaults that apply when `spec.scheduling` is omitted, and
which fields you can change after creation.