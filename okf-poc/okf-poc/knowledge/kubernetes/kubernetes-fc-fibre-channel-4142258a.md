---
id: kubernetes-fc-fibre-channel-4142258a
type: concept
title: fc (fibre channel)
description: An `fc` volume type allows an existing fibre channel block storage volume
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/volumes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### fc (fibre channel)

An `fc` volume type allows an existing fibre channel block storage volume
to be mounted in a Pod. You can specify single or multiple target world wide names (WWNs)
using the parameter `targetWWNs` in your Volume configuration. If multiple WWNs are specified,
targetWWNs expect that those WWNs are from multi-path connections.

#### Note:

You must configure FC SAN Zoning to allocate and mask those LUNs (volumes) to the target WWNs
beforehand so that Kubernetes hosts can access them.