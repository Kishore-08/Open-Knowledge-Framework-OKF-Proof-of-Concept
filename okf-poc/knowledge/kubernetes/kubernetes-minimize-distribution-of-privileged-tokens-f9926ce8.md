---
id: kubernetes-minimize-distribution-of-privileged-tokens-f9926ce8
type: concept
title: Minimize distribution of privileged tokens
description: Ideally, pods shouldn't be assigned service accounts that have been granted
  powerful permissions
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Minimize distribution of privileged tokens

Ideally, pods shouldn't be assigned service accounts that have been granted powerful permissions
(for example, any of the rights listed under [privilege escalation risks](https://kubernetes.io/docs/concepts/security/rbac-good-practices/#privilege-escalation-risks)).
In cases where a workload requires powerful permissions, consider the following practices:

- Limit the number of nodes running powerful pods. Ensure that any DaemonSets you run
  are necessary and are run with least privilege to limit the blast radius of container escapes.
- Avoid running powerful pods alongside untrusted or publicly-exposed ones. Consider using
  [Taints and Toleration](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/),
  [NodeAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#node-affinity), or
  [PodAntiAffinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)
  to ensure pods don't run alongside untrusted or less-trusted Pods. Pay special attention to
  situations where less-trustworthy Pods are not meeting the **Restricted** Pod Security Standard.