---
id: kubernetes-template-reference-0cf588b5
type: concept
title: Template reference
description: The optional `spec.podGroupTemplateRef` links the PodGroup back to the
  PodGroupTemplate
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Template reference

The optional `spec.podGroupTemplateRef` links the PodGroup back to the PodGroupTemplate
in the Workload it was created from. This is useful for observability and tooling.

```
spec:
  podGroupTemplateRef:
    workload:
      workloadName: training-policy
      podGroupTemplateName: worker
```