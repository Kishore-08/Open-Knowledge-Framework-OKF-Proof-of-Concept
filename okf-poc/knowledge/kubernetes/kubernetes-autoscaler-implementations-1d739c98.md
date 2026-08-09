---
id: kubernetes-autoscaler-implementations-1d739c98
type: concept
title: Autoscaler implementations
description: '[Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Autoscaler implementations

[Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)
and [Karpenter](https://github.com/kubernetes-sigs/karpenter) are the two Node autoscalers currently
sponsored by [SIG Autoscaling](https://github.com/kubernetes/community/tree/main/sig-autoscaling).

From the perspective of a cluster user, both autoscalers should provide a similar Node autoscaling
experience. Both will provision new Nodes for unschedulable Pods, and both will consolidate the
Nodes that are no longer optimally utilized.

Different autoscalers may also provide features outside the Node autoscaling scope described on this
page, and those additional features may differ between them.

Consult the sections below, and the linked documentation for the individual autoscalers to decide
which autoscaler fits your use case better.

#### Cluster Autoscaler

Cluster Autoscaler adds or removes Nodes to pre-configured *Node groups*. Node groups generally map
to some sort of cloud provider resource group (most commonly a Virtual Machine group). A single
instance of Cluster Autoscaler can simultaneously manage multiple Node groups. When provisioning,
Cluster Autoscaler will add Nodes to the group that best fits the requests of pending Pods. When
consolidating, Cluster Autoscaler always selects specific Nodes to remove, as opposed to just
resizing the underlying cloud provider resource group.

Additional context:

- [Documentation overview](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/README.md)
- [Cloud provider integrations](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/README.md#faqdocumentation)
- [Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
- [Contact](https://github.com/kubernetes/community/tree/main/sig-autoscaling#contact)

#### Karpenter

Karpenter auto-provisions Nodes based on [NodePool](https://karpenter.sh/docs/concepts/nodepools/)
configurations provided by the cluster operator. Karpenter handles all aspects of node lifecycle,
not just autoscaling. This includes automatically refreshing Nodes once they reach a certain
lifetime, and auto-upgrading Nodes when new worker Node images are released. It works directly with
individual cloud provider resources (most commonly individual Virtual Machines), and doesn't rely on
cloud provider resource groups.

Additional context:

- [Documentation](https://karpenter.sh/)
- [Cloud provider integrations](https://github.com/kubernetes-sigs/karpenter?tab=readme-ov-file#karpenter-implementations)
- [Karpenter FAQ](https://karpenter.sh/docs/faq/)
- [Contact](https://github.com/kubernetes-sigs/karpenter#community-discussion-contribution-and-support)

#### Implementation comparison

Main differences between Cluster Autoscaler and Karpenter:

- Cluster Autoscaler provides features related to just Node autoscaling. Karpenter has a wider
  scope, and also provides features intended for managing Node lifecycle altogether (for example,
  utilizing disruption to auto-recreate Nodes once they reach a certain lifetime, or auto-upgrade
  them to new versions).
- Cluster Autoscaler doesn't support auto-provisioning, the Node groups it can provision from have
  to be pre-configured. Karpenter supports auto-provisioning, so the user only has to configure a
  set of constraints for the provisioned Nodes, instead of fully configuring homogeneous groups.
- Cluster Autoscaler provides cloud provider integrations directly, which means that they're a part
  of the Kubernetes project. For Karpenter, the Kubernetes project publishes Karpenter as a library
  that cloud providers can integrate with to build a Node autoscaler.
- Cluster Autoscaler provides integrations with numerous cloud providers, including smaller and less
  popular providers. There are fewer cloud providers that integrate with Karpenter, including
  [AWS](https://github.com/aws/karpenter-provider-aws),