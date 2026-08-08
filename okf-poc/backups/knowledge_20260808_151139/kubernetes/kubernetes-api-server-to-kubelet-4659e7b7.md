---
id: kubernetes-api-server-to-kubelet-4659e7b7
type: concept
title: API server to kubelet
description: 'The connections from the API server to the kubelet are used for:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### API server to kubelet

The connections from the API server to the kubelet are used for:

- Fetching logs for pods.
- Attaching (usually through `kubectl`) to running pods.
- Providing the kubelet's port-forwarding functionality.

These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not
verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle
attacks and **unsafe** to run over untrusted and/or public networks.

To verify this connection, use the `--kubelet-certificate-authority` flag to provide the API
server with a root certificate bundle to use to verify the kubelet's serving certificate.

If that is not possible, use [SSH tunneling](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/#ssh-tunnels) between the API server and kubelet if
required to avoid connecting over an
untrusted or public network.

Finally, [Kubelet authentication and/or authorization](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/)
should be enabled to secure the kubelet API.