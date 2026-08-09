---
id: kubernetes-networking-and-security-4d305e15
type: concept
title: Networking and security
description: You should also consider network security measures, such as
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Networking and security

You should also consider network security measures, such as
[NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) or a
[service mesh](https://glossary.cncf.io/service-mesh/).
Some network plugins for Kubernetes provide encryption for your
cluster network using technologies such as a virtual
private network (VPN) overlay.
By design, Kubernetes lets you use your own networking plugin for your
cluster. If you use managed Kubernetes, the provider may have already selected a
network plugin for you.

The network plugin you choose and the way you integrate it can have a
strong impact on the security of information in transit.