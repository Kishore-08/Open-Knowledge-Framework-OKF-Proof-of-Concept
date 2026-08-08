---
id: kubernetes-distribute-lifecycle-phase-4d305e15
type: concept
title: '*Distribute* lifecycle phase'
description: '- Ensure the security of the supply chain for container images you execute.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## *Distribute* lifecycle phase

- Ensure the security of the supply chain for container images you execute.
- Ensure the security of the supply chain for the cluster and other components
  that execute your application. For example, this might include an external
  database that your cloud native application uses for persistence.

To achieve this, you can:

1. Scan container images and other artifacts for known vulnerabilities.
2. Ensure that software distribution uses encryption in transit, with
   a chain of trust for the software source.
3. Adopt and follow processes to update dependencies when updates are
   available, especially in response to security announcements.
4. Use validation mechanisms such as digital certificates for supply
   chain assurance.
5. Subscribe to feeds and other mechanisms to alert you to security
   risks.
6. Restrict access to artifacts. Place container images in a
   [private registry](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry)
   that only allows authorized clients to pull images.