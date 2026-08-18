---
id: kubernetes-service-controller-8c98aece
type: concept
title: Service controller
description: The service controller watches for Service object **create**, **update**
  and **delete** events and then
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Service controller

The service controller watches for Service object **create**, **update** and **delete** events and then
configures load balancers for those Services appropriately.

To access Services, it requires **list**, and **watch** access. To update Services, it requires
**patch** and **update** access to the `status` subresource.

`v1/Service`:

- list
- get
- watch
- patch
- update