---
id: kubernetes-stop-signals-3e34f258
type: concept
title: Stop Signals
description: The stop signal used to kill the container can be defined in the container
  image with the `STOPSIGNAL` instruction.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Stop Signals

The stop signal used to kill the container can be defined in the container image with the `STOPSIGNAL` instruction.
If no stop signal is defined in the image, the default signal of the container runtime
(SIGTERM for both containerd and CRI-O) would be used to kill the container.