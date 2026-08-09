---
id: kubernetes-updating-a-deployment-d9a16560
type: concept
title: Updating a Deployment
description: A Deployment's rollout is triggered if and only if the Deployment's Pod
  template (that is, `.spec.template`)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Updating a Deployment

#### Note:

A Deployment's rollout is triggered if and only if the Deployment's Pod template (that is, `.spec.template`)
is changed, for example if the labels or container images of the template are updated. Other updates, such as scaling the Deployment, do not trigger a rollout.

Follow the steps given below to update your Deployment:

1. Let's update the nginx Pods to use the `nginx:1.16.1` image instead of the `nginx:1.14.2` image.

   ```
   kubectl set image deployment.v1.apps/nginx-deployment nginx=nginx:1.16.1
   ```

   or use the following command:

   ```
   kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
   ```

   where `deployment/nginx-deployment` indicates the Deployment,
   `nginx` indicates the Container the update will take place and
   `nginx:1.16.1` indicates the new image and its tag.

   The output is similar to:

   ```
   deployment.apps/nginx-deployment image updated
   ```

   Alternatively, you can `edit` the Deployment and change `.spec.template.spec.containers[0].image` from `nginx:1.14.2` to `nginx:1.16.1`:

   ```
   kubectl edit deployment/nginx-deployment
   ```

   The output is similar to:

   ```
   deployment.apps/nginx-deployment edited
   ```
2. To see the rollout status, run:

   ```
   kubectl rollout status deployment/nginx-deployment
   ```

   The output is similar to this:

   ```
   Waiting for rollout to finish: 2 out of 3 new replicas have been updated...
   ```

   or

   ```
   deployment "nginx-deployment" successfully rolled out
   ```

Get more details on your updated Deployment:

- After the rollout succeeds, you can view the Deployment by running `kubectl get deployments`.
  The output is similar to this:

  ```
  NAME               READY   UP-TO-DATE   AVAILABLE   AGE
  nginx-deployment   3/3     3            3           36s
  ```
- Run `kubectl get rs` to see that the Deployment updated the Pods by creating a new ReplicaSet and scaling it
  up to 3 replicas, as well as scaling down the old ReplicaSet to 0 replicas.

  ```
  kubectl get rs
  ```

  The output is similar to this:

  ```
  NAME                          DESIRED   CURRENT   READY   AGE
  nginx-deployment-1564180365   3         3         3       6s
  nginx-deployment-2035384211   0         0         0       36s
  ```
- Running `get pods` should now show only the new Pods:

  ```
  kubectl get pods
  ```

  The output is similar to this:

  ```
  NAME                                READY     STATUS    RESTARTS   AGE
  nginx-deployment-1564180365-khku8   1/1       Running   0          14s
  nginx-deployment-1564180365-nacti   1/1       Running   0          14s
  nginx-deployment-1564180365-z9gth   1/1       Running   0          14s
  ```

  Next time you want to update these Pods, you only need to update the Deployment's Pod template again.

  Deployment ensures that only a certain number of Pods are down while they are being updated. By default,
  it ensures that at least 75% of the desired number of Pods are up (25% max unavailable).

  Deployment also ensures that only a certain number of Pods are created above the desired number of Pods.
  By default, it ensures that at most 125% of the desired number of Pods are up (25% max surge).

  For example, if you look at the above Deployment closely, you will see that it first creates a new Pod,
  then deletes an old Pod, and creates another new one. It does not kill old Pods until a sufficient number of
  new Pods have come up, and does not create new Pods until a sufficient number of old Pods have been killed.
  It makes sure that at least 3 Pods are available and that at max 4 Pods in total are available. In case of
  a Deployment with 4 replicas, the number of Pods would be between 3 and 5.
- Get details of your Deployment:

  ```
  kubectl describe deployments
  ```

  The output is similar to this:

  ```
  Name:                   nginx-deployment
  Namespace:              default
  CreationTimestamp:      Thu, 30 Nov