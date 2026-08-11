---
id: kubernetes-operating-system-support-9edb5061
type: concept
title: Operating system support
description: '- Linux nodes support swap; you need to configure each node to enable
  it.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Operating system support

- Linux nodes support swap; you need to configure each node to enable it.
  By default, the kubelet will **not** start on a Linux node that has swap enabled.
- Windows nodes require swap space.
  By default, the kubelet does **not** start on a Windows node that has swap disabled.