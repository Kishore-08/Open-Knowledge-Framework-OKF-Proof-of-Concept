---
id: kubernetes-observability-and-runtime-security-4d305e15
type: concept
title: Observability and runtime security
description: Kubernetes lets you extend your cluster with extra tooling. You can set
  up third
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Observability and runtime security

Kubernetes lets you extend your cluster with extra tooling. You can set up third
party solutions to help you monitor or troubleshoot your applications and the
clusters they are running. You also get some basic observability features built
in to Kubernetes itself. Your code running in containers can generate logs,
publish metrics, or provide other observability data; at deploy time, you need to
make sure your cluster provides an appropriate level of protection there.

If you set up a metrics dashboard or something similar, review the chain of components
that populate data into that dashboard, as well as the dashboard itself. Make sure
that the whole chain is designed with enough resilience and integrity protection
that you can rely on it even during an incident where your cluster might be degraded.

Where appropriate, deploy security measures below the Kubernetes layer,
such as cryptographically measured boot or authenticated distribution
of time (which helps ensure the fidelity of logs and audit records).

For a high-assurance environment, deploy cryptographic protections to ensure that
logs are both tamper-proof and confidential.

## What's next