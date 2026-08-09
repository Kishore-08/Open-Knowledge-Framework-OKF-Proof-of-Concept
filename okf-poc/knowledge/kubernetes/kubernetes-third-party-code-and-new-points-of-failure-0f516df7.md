---
id: kubernetes-third-party-code-and-new-points-of-failure-0f516df7
type: concept
title: Third party code and new points of failure
description: While creating a CRD does not automatically add any new points of failure
  (for example, by causing
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Third party code and new points of failure

While creating a CRD does not automatically add any new points of failure (for example, by causing
third party code to run on your API server), packages (for example, Charts) or other installation
bundles often include CRDs as well as a Deployment of third-party code that implements the
business logic for a new custom resource.

Installing an Aggregated API server always involves running a new Deployment.