---
id: kubernetes-api-structure-1182b951
type: concept
title: API structure
description: 'A `Workload` consists of two fields: a list of `PodGroupTemplates` and
  an optional controller'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## API structure

A `Workload` consists of two fields: a list of `PodGroupTemplates` and an optional controller
reference. The entire `Workload` spec is immutable after creation: you cannot modify
existing templates, add new templates, or remove templates from `podGroupTemplates`.