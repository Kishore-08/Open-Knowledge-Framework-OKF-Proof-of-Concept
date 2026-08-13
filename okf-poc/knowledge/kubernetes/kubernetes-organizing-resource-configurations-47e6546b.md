---
id: kubernetes-organizing-resource-configurations-47e6546b
type: concept
title: Organizing resource configurations
description: Many applications require multiple resources to be created, such as a
  Deployment along with a Service.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/management/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Organizing resource configurations

Many applications require multiple resources to be created, such as a Deployment along with a Service.
Management of multiple resources can be simplified by grouping them together in the same file
(separated by `---` in YAML). For example:

[`application/nginx-app.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/application/nginx-app.yaml)![](https://kubernetes.io/images/copycode.svg "Copy application/nginx-app.yaml to clipboard")

```
apiVersion: v1
kind: Service
metadata:
  name: my-nginx-svc
  labels:
    app: nginx
spec:
  type: LoadBalancer
  ports:
  - port: 80
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

Multiple resources can be created the same way as a single resource:

```
kubectl apply -f https://k8s.io/examples/application/nginx-app.yaml
```

```
service/my-nginx-svc created
deployment.apps/my-nginx created
```

The resources will be created in the order they appear in the manifest. Therefore, it's best to
specify the Service first, since that will ensure the scheduler can spread the pods associated
with the Service as they are created by the controller(s), such as Deployment.

`kubectl apply` also accepts multiple `-f` arguments:

```
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-svc.yaml \
  -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

It is a recommended practice to put resources related to the same microservice or application tier
into the same file, and to group all of the files associated with your application in the same
directory. If the tiers of your application bind to each other using DNS, you can deploy all of
the components of your stack together.

A URL can also be specified as a configuration source, which is handy for deploying directly from
manifests in your source control system:

```
kubectl apply -f https://k8s.io/examples/application/nginx/nginx-deployment.yaml
```

```
deployment.apps/my-nginx created
```

If you need to define more manifests, such as adding a ConfigMap, you can do that too.