---
id: kubernetes-plugin-configuration-085106f9
type: concept
title: Plugin configuration
description: You can enable or disable plugins in the scheduler configuration. If
  you are using
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Plugin configuration

You can enable or disable plugins in the scheduler configuration. If you are using
Kubernetes v1.18 or later, most scheduling
[plugins](https://kubernetes.io/docs/reference/scheduling/config/#scheduling-plugins) are in use and
enabled by default.

In addition to default plugins, you can also implement your own scheduling
plugins and get them configured along with default plugins. You can visit
[scheduler-plugins](https://github.com/kubernetes-sigs/scheduler-plugins) for more details.

If you are using Kubernetes v1.18 or later, you can configure a set of plugins as
a scheduler profile and then define multiple profiles to fit various kinds of workload.
Learn more at [multiple profiles](https://kubernetes.io/docs/reference/scheduling/config/#multiple-profiles).