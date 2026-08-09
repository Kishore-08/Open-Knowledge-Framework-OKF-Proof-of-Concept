---
id: kubernetes-comparing-ease-of-use-0f516df7
type: concept
title: Comparing ease of use
description: CRDs are easier to create than Aggregated APIs.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Comparing ease of use

CRDs are easier to create than Aggregated APIs.

| CRDs | Aggregated API |
| --- | --- |
| Do not require programming. Users can choose any language for a CRD controller. | Requires programming and building binary and image. |
| No additional service to run; CRDs are handled by API server. | An additional service to create and that could fail. |
| No ongoing support once the CRD is created. Any bug fixes are picked up as part of normal Kubernetes Master upgrades. | May need to periodically pickup bug fixes from upstream and rebuild and update the Aggregated API server. |
| No need to handle multiple versions of your API; for example, when you control the client for this resource, you can upgrade it in sync with the API. | You need to handle multiple versions of your API; for example, when developing an extension to share with the world. |