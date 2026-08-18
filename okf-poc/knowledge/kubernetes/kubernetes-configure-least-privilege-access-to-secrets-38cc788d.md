---
id: kubernetes-configure-least-privilege-access-to-secrets-38cc788d
type: concept
title: Configure least-privilege access to Secrets
description: To enhance the security measures around Secrets, use separate namespaces
  to isolate access to mounted secrets.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Configure least-privilege access to Secrets

To enhance the security measures around Secrets, use separate namespaces to isolate access to mounted secrets.

#### Warning:

Any containers that run with `privileged: true` on a node can access all
Secrets used on that node.