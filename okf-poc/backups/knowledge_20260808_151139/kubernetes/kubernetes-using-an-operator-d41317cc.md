---
id: kubernetes-using-an-operator-d41317cc
type: concept
title: Using an operator
description: Once you have an operator deployed, you'd use it by adding, modifying
  or
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Using an operator

Once you have an operator deployed, you'd use it by adding, modifying or
deleting the kind of resource that the operator uses. Following the above
example, you would set up a Deployment for the operator itself, and then:

```
kubectl get SampleDB                   # find configured databases

kubectl edit SampleDB/example-database # manually change some settings
```

…and that's it! The operator will take care of applying the changes
as well as keeping the existing service in good shape.