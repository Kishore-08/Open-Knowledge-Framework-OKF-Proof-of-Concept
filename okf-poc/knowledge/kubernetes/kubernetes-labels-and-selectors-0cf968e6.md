---
id: kubernetes-labels-and-selectors-0cf968e6
type: concept
title: Labels and Selectors
description: '*Labels* are key/value pairs that are attached to'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

# Labels and Selectors

*Labels* are key/value pairs that are attached to
[objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.") such as Pods.
Labels are intended to be used to specify identifying attributes of objects
that are meaningful and relevant to users, but do not directly imply semantics
to the core system. Labels can be used to organize and to select subsets of
objects. Labels can be attached to objects at creation time and subsequently
added and modified at any time. Each object can have a set of key/value labels
defined. Each Key must be unique for a given object.

```
"metadata": {
  "labels": {
    "key1" : "value1",
    "key2" : "value2"
  }
}
```

Labels allow for efficient queries and watches and are ideal for use in UIs
and CLIs. Non-identifying information should be recorded using
[annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).