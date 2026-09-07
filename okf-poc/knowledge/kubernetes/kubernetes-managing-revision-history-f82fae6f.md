---
id: kubernetes-managing-revision-history-f82fae6f
type: concept
title: Managing Revision History
description: 'Control retained revisions with `.spec.revisionHistoryLimit`:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Managing Revision History

Control retained revisions with `.spec.revisionHistoryLimit`:

```
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: webapp
spec:
  revisionHistoryLimit: 5  # Keep last 5 revisions
  # ... other spec fields ...
```

- **Default**: 10 revisions retained if unspecified
- **Cleanup**: Oldest revisions are garbage-collected when exceeding the limit

#### Performing Rollbacks

You can revert to a previous configuration using:

```
# View revision history
kubectl rollout history statefulset/webapp

# Rollback to a specific revision
kubectl rollout undo statefulset/webapp --to-revision=3
```

This will:

- Apply the Pod template from revision 3
- Create a new ControllerRevision with an updated revision number

#### Inspecting ControllerRevisions

To view associated ControllerRevisions:

```
# List all revisions for the StatefulSet
kubectl get controllerrevisions -l app.kubernetes.io/name=webapp

# View detailed configuration of a specific revision
kubectl get controllerrevision/webapp-3 -o yaml
```

#### Best Practices

##### Retention Policy

- Set `revisionHistoryLimit` between **5–10** for most workloads.
- Increase only if **deep rollback history** is required.

##### Monitoring

- Regularly check revisions with:

  ```
  kubectl get controllerrevisions
  ```

- Alert on **rapid revision count growth**.

##### Avoid

- Manual edits to ControllerRevision objects.
- Using revisions as a backup mechanism (use actual backup tools).
- Setting `revisionHistoryLimit: 0` (disables rollback capability).