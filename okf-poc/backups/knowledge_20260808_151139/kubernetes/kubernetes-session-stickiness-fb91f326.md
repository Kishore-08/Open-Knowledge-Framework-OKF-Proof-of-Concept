---
id: kubernetes-session-stickiness-fb91f326
type: concept
title: Session stickiness
description: If you want to make sure that connections from a particular client are
  passed to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Session stickiness

If you want to make sure that connections from a particular client are passed to
the same Pod each time, you can configure session affinity based on the client's
IP address. Read [session affinity](https://kubernetes.io/docs/reference/networking/virtual-ips/#session-affinity)
to learn more.