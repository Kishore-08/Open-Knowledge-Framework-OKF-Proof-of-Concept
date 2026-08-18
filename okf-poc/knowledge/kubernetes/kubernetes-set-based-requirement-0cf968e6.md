---
id: kubernetes-set-based-requirement-0cf968e6
type: concept
title: '*Set-based* requirement'
description: '*Set-based* label requirements allow filtering keys according to a set
  of values.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### *Set-based* requirement

*Set-based* label requirements allow filtering keys according to a set of values.
Three kinds of operators are supported: `in`,`notin` and `exists` (only the key identifier).
For example:

```
environment in (production, qa)
tier notin (frontend, backend)
partition
!partition
```

- The first example selects all resources with key equal to `environment` and value
  equal to `production` or `qa`.
- The second example selects all resources with key equal to `tier` and values other
  than `frontend` and `backend`, and all resources with no labels with the `tier` key.
- The third example selects all resources including a label with key `partition`;
  no values are checked.
- The fourth example selects all resources without a label with key `partition`;
  no values are checked.

Similarly the comma separator acts as an *AND* operator. So filtering resources
with a `partition` key (no matter the value) and with `environment` different
than `qa` can be achieved using `partition,environment notin (qa)`.
The *set-based* label selector is a general form of equality since
`environment=production` is equivalent to `environment in (production)`;
similarly for `!=` and `notin`.

*Set-based* requirements can be mixed with *equality-based* requirements.
For example: `partition in (customerA, customerB),environment!=qa`.

## API