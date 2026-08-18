---
id: kubernetes-unaggregated-discovery-0b6c673c
type: concept
title: Unaggregated discovery
description: Without discovery aggregation, discovery is published in levels, with
  the root
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Unaggregated discovery

Without discovery aggregation, discovery is published in levels, with the root
endpoints publishing discovery information for downstream documents.

A list of all group versions supported by a cluster is published at
the `/api` and `/apis` endpoints. Example:

```
{
  "kind": "APIGroupList",
  "apiVersion": "v1",
  "groups": [
    {
      "name": "apiregistration.k8s.io",
      "versions": [
        {
          "groupVersion": "apiregistration.k8s.io/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apiregistration.k8s.io/v1",
        "version": "v1"
      }
    },
    {
      "name": "apps",
      "versions": [
        {
          "groupVersion": "apps/v1",
          "version": "v1"
        }
      ],
      "preferredVersion": {
        "groupVersion": "apps/v1",
        "version": "v1"
      }
    },
    ...
}
```

Additional requests are needed to obtain the discovery document for each group version at
`/apis/<group>/<version>` (for example:
`/apis/rbac.authorization.k8s.io/v1alpha1`), which advertises the list of
resources served under a particular group version. These endpoints are used by
kubectl to fetch the list of resources supported by a cluster.