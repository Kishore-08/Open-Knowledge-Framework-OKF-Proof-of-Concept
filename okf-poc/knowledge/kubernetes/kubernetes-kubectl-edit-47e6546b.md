---
id: kubernetes-kubectl-edit-47e6546b
type: concept
title: kubectl edit
description: 'Alternatively, you may also update resources with [`kubectl edit`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit/):'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### kubectl edit

Alternatively, you may also update resources with [`kubectl edit`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit/):

```
kubectl edit deployment/my-nginx
```

This is equivalent to first `get` the resource, edit it in text editor, and then `apply` the
resource with the updated version:

```
kubectl get deployment my-nginx -o yaml > /tmp/nginx.yaml
vi /tmp/nginx.yaml
# do some edit, and then save the file

kubectl apply -f /tmp/nginx.yaml
deployment.apps/my-nginx configured

rm /tmp/nginx.yaml
```

This allows you to do more significant changes more easily. Note that you can specify the editor
with your `EDITOR` or `KUBE_EDITOR` environment variables.

For more information, please see [kubectl edit](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit/).