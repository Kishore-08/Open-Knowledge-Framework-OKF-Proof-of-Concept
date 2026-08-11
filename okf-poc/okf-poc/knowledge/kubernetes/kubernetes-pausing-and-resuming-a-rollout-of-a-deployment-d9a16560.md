---
id: kubernetes-pausing-and-resuming-a-rollout-of-a-deployment-d9a16560
type: concept
title: Pausing and Resuming a rollout of a Deployment
description: When you update a Deployment, or plan to, you can pause rollouts
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pausing and Resuming a rollout of a Deployment

When you update a Deployment, or plan to, you can pause rollouts
for that Deployment before you trigger one or more updates. When
you're ready to apply those changes, you resume rollouts for the
Deployment. This approach allows you to
apply multiple fixes in between pausing and resuming without triggering unnecessary rollouts.

- For example, with a Deployment that was created:

  Get the Deployment details:

  ```
  kubectl get deploy
  ```

  The output is similar to this:

  ```
  NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
  nginx     3         3         3            3           1m
  ```

  Get the rollout status:

  ```
  kubectl get rs
  ```

  The output is similar to this:

  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   3         3         3         1m
  ```
- Pause by running the following command:

  ```
  kubectl rollout pause deployment/nginx-deployment
  ```

  The output is similar to this:

  ```
  deployment.apps/nginx-deployment paused
  ```
- Then update the image of the Deployment:

  ```
  kubectl set image deployment/nginx-deployment nginx=nginx:1.16.1
  ```

  The output is similar to this:

  ```
  deployment.apps/nginx-deployment image updated
  ```
- Notice that no new rollout started:

  ```
  kubectl rollout history deployment/nginx-deployment
  ```

  The output is similar to this:

  ```
  deployments "nginx"
  REVISION  CHANGE-CAUSE
  1   <none>
  ```
- Get the rollout status to verify that the existing ReplicaSet has not changed:

  ```
  kubectl get rs
  ```

  The output is similar to this:

  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   3         3         3         2m
  ```
- You can make as many updates as you wish, for example, update the resources that will be used:

  ```
  kubectl set resources deployment/nginx-deployment -c=nginx --limits=cpu=200m,memory=512Mi
  ```

  The output is similar to this:

  ```
  deployment.apps/nginx-deployment resource requirements updated
  ```

  The initial state of the Deployment prior to pausing its rollout will continue its function, but new updates to
  the Deployment will not have any effect as long as the Deployment rollout is paused.
- Eventually, resume the Deployment rollout and observe a new ReplicaSet coming up with all the new updates:

  ```
  kubectl rollout resume deployment/nginx-deployment
  ```

  The output is similar to this:

  ```
  deployment.apps/nginx-deployment resumed
  ```
- [Watch](https://kubernetes.io/docs/reference/using-api/api-concepts/#api-verbs "A verb that is used to track changes to an object in Kubernetes as a stream.") the status of the rollout until it's done.

  ```
  kubectl get rs --watch
  ```

  The output is similar to this:

  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   2         2         2         2m
  nginx-3926361531   2         2         0         6s
  nginx-3926361531   2         2         1         18s
  nginx-2142116321   1         2         2         2m
  nginx-2142116321   1         2         2         2m
  nginx-3926361531   3         2         1         18s
  nginx-3926361531   3         2         1         18s
  nginx-2142116321   1         1         1         2m
  nginx-3926361531   3         3         1         18s
  nginx-3926361531   3         3         2         19s
  nginx-2142116321   0         1         1         2m
  nginx-2142116321   0         1         1         2m
  nginx-2142116321   0         0         0         2m
  nginx-3926361531   3         3         3         20s
  ```
- Get the status of the latest rollout:

  ```
  kubectl get rs
  ```

  The output is similar to this:

  ```
  NAME               DESIRED   CURRENT   READY     AGE
  nginx-2142116321   0         0         0         2m
  nginx-3926361531   3         3         3         28s
  ```

#### Note:

You cannot rollback a paused Deployment until y