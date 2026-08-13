---
id: kubernetes-don-t-change-immutable-objects-137dc105
type: concept
title: Don't change immutable objects
description: Some Kubernetes objects in the API server can't change. For example,
  when you
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Don't change immutable objects

Some Kubernetes objects in the API server can't change. For example, when you
deploy a [static Pod](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/ "A pod managed directly by the kubelet daemon on a specific node."), the
kubelet on the node creates a
[mirror Pod](https://kubernetes.io/docs/reference/glossary/?all=true#term-mirror-pod "An object in the API server that tracks a static pod on a kubelet.") in the API
server to track the static Pod. However, changes to the mirror Pod don't
propagate to the static Pod.

Don't attempt to mutate these objects during admission. All mirror Pods have the
`kubernetes.io/config.mirror` annotation. To exclude mirror Pods while reducing
the security risk of ignoring an annotation, allow static Pods to only run in
specific namespaces.