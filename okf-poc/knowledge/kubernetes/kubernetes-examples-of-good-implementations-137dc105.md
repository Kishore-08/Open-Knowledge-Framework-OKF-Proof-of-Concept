---
id: kubernetes-examples-of-good-implementations-137dc105
type: concept
title: Examples of good implementations
description: '**Note:** This section links to third party projects that provide functionality
  required by Kubernetes. The Kubernetes project authors aren''t responsible for these
  projects, which are listed alphabeti'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Examples of good implementations

**Note:** This section links to third party projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for these projects, which are listed alphabetically. To add a project to this list, read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before submitting a change. [More information.](https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/#third-party-content-disclaimer)

The following projects are examples of "good" custom webhook server
implementations. You can use them as a starting point when designing your own
webhooks. Don't use these examples as-is; use them as a starting point and
design your webhooks to run well in your specific environment.

- [`cert-manager`](https://github.com/cert-manager/cert-manager/tree/master/internal/webhook)
- [Gatekeeper Open Policy Agent (OPA)](https://open-policy-agent.github.io/gatekeeper/website/docs/mutation)