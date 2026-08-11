---
id: kubernetes-rollover-aka-multiple-updates-in-flight-d9a16560
type: concept
title: Rollover (aka multiple updates in-flight)
description: Each time a new Deployment is observed by the Deployment controller,
  a ReplicaSet is created to bring up
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Rollover (aka multiple updates in-flight)

Each time a new Deployment is observed by the Deployment controller, a ReplicaSet is created to bring up
the desired Pods. If the Deployment is updated, the existing ReplicaSet that controls Pods whose labels
match `.spec.selector` but whose template does not match `.spec.template` is scaled down. Eventually, the new
ReplicaSet is scaled to `.spec.replicas` and all old ReplicaSets is scaled to 0.

If you update a Deployment while an existing rollout is in progress, the Deployment creates a new ReplicaSet
as per the update and start scaling that up, and rolls over the ReplicaSet that it was scaling up previously
-- it will add it to its list of old ReplicaSets and start scaling it down.

For example, suppose you create a Deployment to create 5 replicas of `nginx:1.14.2`,
but then update the Deployment to create 5 replicas of `nginx:1.16.1`, when only 3
replicas of `nginx:1.14.2` had been created. In that case, the Deployment immediately starts
killing the 3 `nginx:1.14.2` Pods that it had created, and starts creating
`nginx:1.16.1` Pods. It does not wait for the 5 replicas of `nginx:1.14.2` to be created
before changing course.