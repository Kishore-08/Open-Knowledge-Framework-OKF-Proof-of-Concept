---
id: kubernetes-pod-template-375b8ad3
type: concept
title: Pod Template
description: The `.spec.template` is a [pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates)
  which is also
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Pod Template

The `.spec.template` is a [pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates) which is also
required to have labels in place. In our `frontend.yaml` example we had one label: `tier: frontend`.
Be careful not to overlap with the selectors of other controllers, lest they try to adopt this Pod.

For the template's [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) field,
`.spec.template.spec.restartPolicy`, the only allowed value is `Always`, which is the default.