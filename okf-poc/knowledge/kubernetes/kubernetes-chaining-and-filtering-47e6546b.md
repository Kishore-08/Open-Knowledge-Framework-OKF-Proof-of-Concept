---
id: kubernetes-chaining-and-filtering-47e6546b
type: concept
title: Chaining and filtering
description: Because `kubectl` outputs resource names in the same syntax it accepts,
  you can chain operations
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Chaining and filtering

Because `kubectl` outputs resource names in the same syntax it accepts, you can chain operations
using `$()` or `xargs`:

```
kubectl get $(kubectl create -f docs/concepts/cluster-administration/nginx/ -o name | grep service/ )
kubectl create -f docs/concepts/cluster-administration/nginx/ -o name | grep service/ | xargs -i kubectl get '{}'
```

The output might be similar to:

```
NAME           TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)      AGE
my-nginx-svc   LoadBalancer   10.0.0.208   <pending>     80/TCP       0s
```

With the above commands, first you create resources under `docs/concepts/cluster-administration/nginx/` and print
the resources created with `-o name` output format (print each resource as resource/name).
Then you `grep` only the Service, and then print it with [`kubectl get`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get/).