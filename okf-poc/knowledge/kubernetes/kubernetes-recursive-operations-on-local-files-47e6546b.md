---
id: kubernetes-recursive-operations-on-local-files-47e6546b
type: concept
title: Recursive operations on local files
description: If you happen to organize your resources across several subdirectories
  within a particular
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Recursive operations on local files

If you happen to organize your resources across several subdirectories within a particular
directory, you can recursively perform the operations on the subdirectories also, by specifying
`--recursive` or `-R` alongside the `--filename`/`-f` argument.

For instance, assume there is a directory `project/k8s/development` that holds all of the
[manifests](https://kubernetes.io/docs/reference/glossary/?all=true#term-manifest "A serialized specification of one or more Kubernetes API objects.") needed for the development environment,
organized by resource type:

```
project/k8s/development
├── configmap
│   └── my-configmap.yaml
├── deployment
│   └── my-deployment.yaml
└── pvc
    └── my-pvc.yaml
```

By default, performing a bulk operation on `project/k8s/development` will stop at the first level
of the directory, not processing any subdirectories. If you had tried to create the resources in
this directory using the following command, we would have encountered an error:

```
kubectl apply -f project/k8s/development
```

```
error: you must provide one or more resources by argument or filename (.json|.yaml|.yml|stdin)
```

Instead, specify the `--recursive` or `-R` command line argument along with the `--filename`/`-f` argument:

```
kubectl apply -f project/k8s/development --recursive
```

```
configmap/my-config created
deployment.apps/my-deployment created
persistentvolumeclaim/my-pvc created
```

The `--recursive` argument works with any operation that accepts the `--filename`/`-f` argument such as:
`kubectl create`, `kubectl get`, `kubectl delete`, `kubectl describe`, or even `kubectl rollout`.

The `--recursive` argument also works when multiple `-f` arguments are provided:

```
kubectl apply -f project/k8s/namespaces -f project/k8s/development --recursive
```

```
namespace/development created
namespace/staging created
configmap/my-config created
deployment.apps/my-deployment created
persistentvolumeclaim/my-pvc created
```

If you're interested in learning more about `kubectl`, go ahead and read
[Command line tool (kubectl)](https://kubernetes.io/docs/reference/kubectl/).