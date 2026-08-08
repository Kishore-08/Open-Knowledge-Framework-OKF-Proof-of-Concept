---
id: kubernetes-common-features-0f516df7
type: concept
title: Common Features
description: When you create a custom resource, either via a CRD or an AA, you get
  many features for your API,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Common Features

When you create a custom resource, either via a CRD or an AA, you get many features for your API,
compared to implementing it outside the Kubernetes platform:

| Feature | What it does |
| --- | --- |
| CRUD | The new endpoints support CRUD basic operations via HTTP and `kubectl` |
| Watch | The new endpoints support Kubernetes Watch operations via HTTP |
| Discovery | Clients like `kubectl` and dashboard automatically offer list, display, and field edit operations on your resources |
| json-patch | The new endpoints support PATCH with `Content-Type: application/json-patch+json` |
| merge-patch | The new endpoints support PATCH with `Content-Type: application/merge-patch+json` |
| HTTPS | The new endpoints uses HTTPS |
| Built-in Authentication | Access to the extension uses the core API server (aggregation layer) for authentication |
| Built-in Authorization | Access to the extension can reuse the authorization used by the core API server; for example, RBAC. |
| Finalizers | Block deletion of extension resources until external cleanup happens. |
| Admission Webhooks | Set default values and validate extension resources during any create/update/delete operation. |
| UI/CLI Display | Kubectl, dashboard can display extension resources. |
| Unset versus Empty | Clients can distinguish unset fields from zero-valued fields. |
| Client Libraries Generation | Kubernetes provides generic client libraries, as well as tools to generate type-specific client libraries. |
| Labels and annotations | Common metadata across objects that tools know how to edit for core and custom resources. |

## Preparing to install a custom resource

There are several points to be aware of before adding a custom resource to your cluster.