---
id: kubernetes-updating-annotations-47e6546b
type: concept
title: Updating annotations
description: Sometimes you would want to attach annotations to resources. Annotations
  are arbitrary
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Updating annotations

Sometimes you would want to attach annotations to resources. Annotations are arbitrary
non-identifying metadata for retrieval by API clients such as tools or libraries.
This can be done with `kubectl annotate`. For example:

```
kubectl annotate pods my-nginx-v4-9gw19 description='my frontend running nginx'
kubectl get pods my-nginx-v4-9gw19 -o yaml
```

```
apiVersion: v1
kind: pod
metadata:
  annotations:
    description: my frontend running nginx
...
```

For more information, see [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
and [kubectl annotate](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate/).