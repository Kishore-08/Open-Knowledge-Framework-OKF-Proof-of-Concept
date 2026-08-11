---
id: kubernetes-using-configmaps-as-environment-variables-02bcaed0
type: concept
title: Using Configmaps as environment variables
description: To use a Configmap in an [environment variable](https://kubernetes.io/docs/concepts/containers/container-environment/
  "Container environment variables are name=value pairs that provide useful informat
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/configmap/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Using Configmaps as environment variables

To use a Configmap in an [environment variable](https://kubernetes.io/docs/concepts/containers/container-environment/ "Container environment variables are name=value pairs that provide useful information into containers running in a Pod.")
in a Pod:

1. For each container in your Pod specification, add an environment variable
   for each Configmap key that you want to use to the
   `env[].valueFrom.configMapKeyRef` field.
2. Modify your image and/or command line so that the program looks for values
   in the specified environment variables.

This is an example of defining a ConfigMap as a pod environment variable:

The following ConfigMap (myconfigmap.yaml) stores two properties: username and access\_level:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: myconfigmap
data:
  username: k8s-admin
  access_level: "1"
```

The following command will create the ConfigMap object:

```
kubectl apply -f myconfigmap.yaml
```

The following Pod consumes the content of the ConfigMap as environment variables:

[`configmap/env-configmap.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/configmap/env-configmap.yaml)![](https://kubernetes.io/images/copycode.svg "Copy configmap/env-configmap.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: env-configmap
spec:
  containers:
    - name: app
      command: ["/bin/sh", "-c", "printenv"]
      image: busybox:latest
      envFrom:
        - configMapRef:
            name: myconfigmap
```

The `envFrom` field instructs Kubernetes to create environment variables from the sources nested within it.
The inner `configMapRef` refers to a ConfigMap by its name and selects all its key-value pairs.
Add the Pod to your cluster, then retrieve its logs to see the output from the printenv command.
This should confirm that the two key-value pairs from the ConfigMap have been set as environment variables:

```
kubectl apply -f env-configmap.yaml
```

```
kubectl logs pod/env-configmap
```

The output is similar to this:

```
...
username: "k8s-admin"
access_level: "1"
...
```

Sometimes a Pod won't require access to all the values in a ConfigMap.
For example, you could have another Pod which only uses the username value from the ConfigMap.
For this use case, you can use the `env.valueFrom` syntax instead, which lets you select individual keys in
a ConfigMap. The name of the environment variable can also be different from the key within the ConfigMap.
For example:

```
apiVersion: v1
kind: Pod
metadata:
  name: env-configmap
spec:
  containers:
  - name: envars-test-container
    image: nginx
    env:
    - name: CONFIGMAP_USERNAME
      valueFrom:
        configMapKeyRef:
          name: myconfigmap
          key: username
```

In the Pod created from this manifest, you will see that the environment variable
`CONFIGMAP_USERNAME` is set to the value of the `username` value from the ConfigMap.
Other keys from the ConfigMap data are not copied into the environment.

It's important to note that the range of characters allowed for environment
variable names in pods is [restricted](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config).
If any keys do not meet the rules, those keys are not made available to your container, though
the Pod is allowed to start.