---
id: kubernetes-self-registration-of-nodes-5445bee6
type: concept
title: Self-registration of Nodes
description: When the kubelet flag `--register-node` is true (the default), the kubelet
  will attempt to
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/nodes/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Self-registration of Nodes

When the kubelet flag `--register-node` is true (the default), the kubelet will attempt to
register itself with the API server. This is the preferred pattern, used by most distros.

For self-registration, the kubelet is started with the following options:

- `--kubeconfig` - Path to credentials to authenticate itself to the API server.
- `--cloud-provider` - How to talk to a [cloud provider](https://kubernetes.io/docs/reference/glossary/?all=true#term-cloud-provider "An organization that offers a cloud computing platform.")
  to read metadata about itself.
- `--register-node` - Automatically register with the API server.
- `--register-with-taints` - Register the node with the given list of
  [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Taints prevent the scheduling of pods on nodes or node groups.") (comma separated `<key>=<value>:<effect>`).

  No-op if `register-node` is false.
- `--node-ip` - Optional comma-separated list of the IP addresses for the node.
  You can only specify a single address for each address family.
  For example, in a single-stack IPv4 cluster, you set this value to be the IPv4 address that the
  kubelet should use for the node.
  See [configure IPv4/IPv6 dual stack](https://kubernetes.io/docs/concepts/services-networking/dual-stack/#configure-ipv4-ipv6-dual-stack)
  for details of running a dual-stack cluster.

  If you don't provide this argument, the kubelet uses the node's default IPv4 address, if any;
  if the node has no IPv4 addresses then the kubelet uses the node's default IPv6 address.
- `--node-labels` - [Labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels "Tags objects with identifying attributes that are meaningful and relevant to users.") to add when registering the node
  in the cluster (see label restrictions enforced by the
  [NodeRestriction admission plugin](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction)).
- `--node-status-update-frequency` - Specifies how often kubelet posts its node status to the API server.

When the [Node authorization mode](https://kubernetes.io/docs/reference/access-authn-authz/node/) and
[NodeRestriction admission plugin](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#noderestriction)
are enabled, kubelets are only authorized to create/modify their own Node resource.

#### Note:

As mentioned in the [Node name uniqueness](https://kubernetes.io/docs/concepts/architecture/nodes/#node-name-uniqueness) section,
when Node configuration needs to be updated, it is a good practice to re-register
the node with the API server. For example, if the kubelet is being restarted with
a new set of `--node-labels`, but the same Node name is used, the change will
not take effect, as labels are only set (or modified) upon Node registration with the API server.

Pods already scheduled on the Node may misbehave or cause issues if the Node
configuration will be changed on kubelet restart. For example, an already running
Pod may be tainted against the new labels assigned to the Node, while other
Pods, that are incompatible with that Pod will be scheduled based on this new
label. Node re-registration ensures all Pods will be drained and properly
re-scheduled.