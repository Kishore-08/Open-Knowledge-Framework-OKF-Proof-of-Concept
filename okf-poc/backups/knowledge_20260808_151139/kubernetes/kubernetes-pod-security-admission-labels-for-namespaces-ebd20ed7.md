---
id: kubernetes-pod-security-admission-labels-for-namespaces-ebd20ed7
type: concept
title: Pod Security Admission labels for namespaces
description: Once the feature is enabled or the webhook is installed, you can configure
  namespaces to define the admission
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod Security Admission labels for namespaces

Once the feature is enabled or the webhook is installed, you can configure namespaces to define the admission
control mode you want to use for pod security in each namespace. Kubernetes defines a set of
[labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") that you can set to define which of the
predefined Pod Security Standard levels you want to use for a namespace. The label you select
defines what action the [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.")
takes if a potential violation is detected:

Pod Security Admission modes

| Mode | Description |
| --- | --- |
| **enforce** | Policy violations will cause the pod to be rejected. |
| **audit** | Policy violations will trigger the addition of an audit annotation to the event recorded in the [audit log](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/), but are otherwise allowed. |
| **warn** | Policy violations will trigger a user-facing warning, but are otherwise allowed. |

A namespace can configure any or all modes, or even set a different level for different modes.

For each mode, there are two labels that determine the policy used:

```
# The per-mode level label indicates which policy level to apply for the mode.
#
# MODE must be one of `enforce`, `audit`, or `warn`.
# LEVEL must be one of `privileged`, `baseline`, or `restricted`.
pod-security.kubernetes.io/<MODE>: <LEVEL>

# Optional: per-mode version label that can be used to pin the policy to the
# version that shipped with a given Kubernetes minor version (for example v1.36).
#
# MODE must be one of `enforce`, `audit`, or `warn`.
# VERSION must be a valid Kubernetes minor version, or `latest`.
pod-security.kubernetes.io/<MODE>-version: <VERSION>
```

Check out [Enforce Pod Security Standards with Namespace Labels](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/) to see example usage.