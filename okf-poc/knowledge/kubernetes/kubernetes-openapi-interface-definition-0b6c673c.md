---
id: kubernetes-openapi-interface-definition-0b6c673c
type: concept
title: OpenAPI interface definition
description: For details about the OpenAPI specifications, see the [OpenAPI documentation](https://www.openapis.org/).
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## OpenAPI interface definition

For details about the OpenAPI specifications, see the [OpenAPI documentation](https://www.openapis.org/).

Kubernetes serves both OpenAPI v2.0 and OpenAPI v3.0. OpenAPI v3 is the
preferred method of accessing the OpenAPI because it offers a more comprehensive
(lossless) representation of Kubernetes resources. Due to limitations of OpenAPI
version 2, certain fields are dropped from the published OpenAPI including but not
limited to `default`, `nullable`, `oneOf`.