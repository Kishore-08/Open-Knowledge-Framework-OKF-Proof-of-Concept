---
id: kubernetes-label-selector-updates-d9a16560
type: concept
title: Label selector updates
description: It is generally discouraged to make label selector updates and it is
  suggested to plan your selectors up front.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Label selector updates

It is generally discouraged to make label selector updates and it is suggested to plan your selectors up front.
A Deployment's label selector is **immutable** after creation;
it cannot be updated via `kubectl patch`, `kubectl edit`, `kubectl apply`, or tools like `helm upgrade`.

If you must change the selector, you have to delete the Deployment and recreate it.
By default, deleting the Deployment also deletes its running Pods, causing downtime; use
`--cascade=orphan` if you need those Pods to keep running while you recreate the Deployment
(see the implications below).
Exercise great caution and ensure you grasp the following implications:

- **Additions:** When you create a new Deployment with a narrower selector, the new Deployment **must** also have a suitable Pod template.
  If you have an existing manifest and you edit the manifest to narrow the selector, you need to edit the metadata of the Pod template inside that Deployment, adding the
  new labels
  to match, as otherwise the API server returns a validation error. This is a *non-overlapping* change:
  the new Deployment will not "see" the old Pods (which lack the new label), causing the old
  ReplicaSet to be **orphaned** and a brand-new ReplicaSet to be created.
- **Value Updates:** Changing the existing value in a selector key (e.g., from `v1` to `v2`)
  results in the same behavior as additions (orphaning and recreation).
- **Removals:** Removing an existing key from the Deployment selector does not require any changes
  in the Pod template labels. This is an *overlapping* change: the new, broader selector would
  match the old Pods. Existing ReplicaSets are not orphaned, and a new ReplicaSet is not created,
  but note that the removed label still exists in any existing Pods and ReplicaSets.
  You can clean that up by triggering a rollout for the Deployment.