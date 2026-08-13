---
id: kubernetes-memory-resource-units-d3611dbe
type: concept
title: Memory resource units
description: Limits and requests for `memory` are measured in bytes. You can express
  memory as
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Memory resource units

Limits and requests for `memory` are measured in bytes. You can express memory as
a plain integer or as a fixed-point number using one of these
[quantity](https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/) suffixes:
E, P, T, G, M, k. You can also use the power-of-two equivalents: Ei, Pi, Ti, Gi,
Mi, Ki. The Kubernetes API also allows m as a suffix (for millibytes: 1/1000 of a byte),
but this isn't useful to specify: you must always assign whole numbers of bytes, or sometimes larger chunks such as multiples of 1 gibibyte.

Here are some examples of memory quantities that represent roughly the same value:

```
128974848, 129e6, 129M,  128974848000m, 123Mi
```

Pay attention to the case of the suffixes. "M" means megabytes, while "m" means millibytes. If you request `400m` of memory, this is a request for 0.4 bytes. Someone who types that probably meant to ask for 400 mebibytes (`400Mi`)
or 400 megabytes (`400M`).