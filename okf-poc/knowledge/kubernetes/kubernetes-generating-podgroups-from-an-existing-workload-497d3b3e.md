---
id: kubernetes-generating-podgroups-from-an-existing-workload-497d3b3e
type: concept
title: Generating PodGroups from an existing Workload
description: When the Workload already exists, whether compiled by a parent controller
  or created manually,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Generating PodGroups from an existing Workload

When the Workload already exists, whether compiled by a parent controller or created manually,
a child controller that only manages the runtime PodGroup uses `NewBuilderFromExistingWorkload`
instead. That builder creates PodGroup objects from the supplied Workload using its own owner
reference. It does not validate or compile anything, so the existing Workload is never
recompiled.

```
builder := workloadbuilder.NewBuilderFromExistingWorkload(parentWorkload, workloadbuilder.BuildOptions{Owner: owner})
podGroup, err := builder.NewPodGroup("trainer-pg", "trainer-pgt-0")
```