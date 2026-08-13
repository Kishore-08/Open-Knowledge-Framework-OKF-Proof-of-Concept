---
id: kubernetes-access-to-proxy-subresource-of-nodes-f9926ce8
type: concept
title: Access to `proxy` subresource of Nodes
description: Users with access to the `nodes/proxy` sub-resource have rights to the
  Kubelet API,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/rbac-good-practices/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Access to `proxy` subresource of Nodes

Users with access to the `nodes/proxy` sub-resource have rights to the Kubelet API,
which allows for command execution on every pod on the node(s) to which they have rights.
This access bypasses audit logging and admission control, so care should be taken before
granting any rights to this resource.
These APIs can be exercised via websocket HTTP `GET` requests, which only requires authorization of the **get** verb.
This means that **get** permission on `nodes/proxy` is not a read-only permission.
For example, permission to **get** `nodes/proxy` provides access to privileged kubelet
APIs that can retrieve container logs or execute and attach to pod processes,
even when a caller does not have the equivalent permissions through the
Kubernetes API.

See [Kubelet authentication/authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/#get-nodes-proxy-warning)
for more information.