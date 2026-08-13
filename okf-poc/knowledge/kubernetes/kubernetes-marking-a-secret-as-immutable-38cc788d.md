---
id: kubernetes-marking-a-secret-as-immutable-38cc788d
type: concept
title: Marking a Secret as immutable
description: You can create an immutable Secret by setting the `immutable` field to
  `true`. For example,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Marking a Secret as immutable

You can create an immutable Secret by setting the `immutable` field to `true`. For example,

```
apiVersion: v1
kind: Secret
metadata: ...
data: ...
immutable: true
```

You can also update any existing mutable Secret to make it immutable.

#### Note:

Once a Secret or ConfigMap is marked as immutable, it is *not* possible to revert this change
nor to mutate the contents of the `data` field. You can only delete and recreate the Secret.
Existing Pods maintain a mount point to the deleted Secret - it is recommended to recreate
these pods.