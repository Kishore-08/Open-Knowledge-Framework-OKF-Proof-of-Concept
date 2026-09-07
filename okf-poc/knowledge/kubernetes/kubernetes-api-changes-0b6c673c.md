---
id: kubernetes-api-changes-0b6c673c
type: concept
title: API changes
description: Any system that is successful needs to grow and change as new use cases
  emerge or existing ones change.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### API changes

Any system that is successful needs to grow and change as new use cases emerge or existing ones change.
Therefore, Kubernetes has designed the Kubernetes API to continuously change and grow.
The Kubernetes project aims to *not* break compatibility with existing clients, and to maintain that
compatibility for a length of time so that other projects have an opportunity to adapt.

In general, new API resources and new resource fields can be added often and frequently.
Elimination of resources or fields requires following the
[API deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/).

Kubernetes makes a strong commitment to maintain compatibility for official Kubernetes APIs
once they reach general availability (GA), typically at API version `v1`. Additionally,
Kubernetes maintains compatibility with data persisted via *beta* API versions of official Kubernetes APIs,
and ensures that data can be converted and accessed via GA API versions when the feature goes stable.

If you adopt a beta API version, you will need to transition to a subsequent beta or stable API version
once the API graduates. The best time to do this is while the beta API is in its deprecation period,
since objects are simultaneously accessible via both API versions. Once the beta API completes its
deprecation period and is no longer served, the replacement API version must be used.

#### Note:

Although Kubernetes also aims to maintain compatibility for *alpha* APIs versions, in some
circumstances this is not possible. If you use any alpha API versions, check the release notes
for Kubernetes when upgrading your cluster, in case the API did change in incompatible
ways that require deleting all existing alpha objects prior to upgrade.

Refer to [API versions reference](https://kubernetes.io/docs/reference/using-api/#api-versioning)
for more details on the API version level definitions.