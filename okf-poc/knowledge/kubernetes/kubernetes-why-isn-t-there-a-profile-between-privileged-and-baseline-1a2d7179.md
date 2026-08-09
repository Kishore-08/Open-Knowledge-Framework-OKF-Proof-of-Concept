---
id: kubernetes-why-isn-t-there-a-profile-between-privileged-and-baseline-1a2d7179
type: concept
title: Why isn't there a profile between Privileged and Baseline?
description: The three profiles defined here have a clear linear progression from
  most secure (Restricted) to least
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Why isn't there a profile between Privileged and Baseline?

The three profiles defined here have a clear linear progression from most secure (Restricted) to least
secure (Privileged), and cover a broad set of workloads. Privileges required above the Baseline
policy are typically very application specific, so we do not offer a standard profile in this
niche. This is not to say that the privileged profile should always be used in this case, but that
policies in this space need to be defined on a case-by-case basis.

SIG Auth may reconsider this position in the future, should a clear need for other profiles arise.