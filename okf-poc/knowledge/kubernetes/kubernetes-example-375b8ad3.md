---
id: kubernetes-example-375b8ad3
type: concept
title: Example
description: '[`controllers/frontend.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/controllers/frontend.yaml)![](https://kubernetes.io/images/copycode.svg
  "Copy controllers/fr'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Example

[`controllers/frontend.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/controllers/frontend.yaml)![](https://kubernetes.io/images/copycode.svg "Copy controllers/frontend.yaml to clipboard")

```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend
  labels:
    app: guestbook
    tier: frontend
spec:
  # modify replicas according to your case
  replicas: 3
  selector:
    matchLabels:
      tier: frontend
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - name: php-redis
        image: us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
```

Saving this manifest into `frontend.yaml` and submitting it to a Kubernetes cluster will
create the defined ReplicaSet and the Pods that it manages.

```
kubectl apply -f https://kubernetes.io/examples/controllers/frontend.yaml
```

You can then get the current ReplicaSets deployed:

```
kubectl get rs
```

And see the frontend one you created:

```
NAME       DESIRED   CURRENT   READY   AGE
frontend   3         3         3       6s
```

You can also check on the state of the ReplicaSet:

```
kubectl describe rs/frontend
```

And you will see output similar to:

```
Name:         frontend
Namespace:    default
Selector:     tier=frontend
Labels:       app=guestbook
              tier=frontend
Annotations:  <none>
Replicas:     3 current / 3 desired
Pods Status:  3 Running / 0 Waiting / 0 Succeeded / 0 Failed
Pod Template:
  Labels:  tier=frontend
  Containers:
   php-redis:
    Image:        us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
    Port:         <none>
    Host Port:    <none>
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Events:
  Type    Reason            Age   From                   Message
  ----    ------            ----  ----                   -------
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-gbgfx
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-rwz57
  Normal  SuccessfulCreate  13s   replicaset-controller  Created pod: frontend-wkl7w
```

And lastly you can check for the Pods brought up:

```
kubectl get pods
```

You should see Pod information similar to:

```
NAME             READY   STATUS    RESTARTS   AGE
frontend-gbgfx   1/1     Running   0          10m
frontend-rwz57   1/1     Running   0          10m
frontend-wkl7w   1/1     Running   0          10m
```

You can also verify that the owner reference of these pods is set to the frontend ReplicaSet.
To do this, get the yaml of one of the Pods running:

```
kubectl get pods frontend-gbgfx -o yaml
```

The output will look similar to this, with the frontend ReplicaSet's info set in the metadata's ownerReferences field:

```
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: "2024-02-28T22:30:44Z"
  generateName: frontend-
  labels:
    tier: frontend
  name: frontend-gbgfx
  namespace: default
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: frontend
    uid: e129deca-f864-481b-bb16-b27abfd92292
...
```