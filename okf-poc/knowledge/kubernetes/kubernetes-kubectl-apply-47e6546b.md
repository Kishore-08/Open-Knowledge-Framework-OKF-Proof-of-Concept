---
id: kubernetes-kubectl-apply-47e6546b
type: concept
title: kubectl apply
description: It is suggested to maintain a set of configuration files in source control
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### kubectl apply

It is suggested to maintain a set of configuration files in source control
(see [configuration as code](https://martinfowler.com/bliki/InfrastructureAsCode.html)),
so that they can be maintained and versioned along with the code for the resources they configure.
Then, you can use [`kubectl apply`](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply/)
to push your configuration changes to the cluster.

This command will compare the version of the configuration that you're pushing with the previous
version and apply the changes you've made, without overwriting any automated changes to properties
you haven't specified.

```
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

```
deployment.apps/my-nginx configured
```

To learn more about the underlying mechanism, read [server-side apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/).