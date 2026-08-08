---
id: kubernetes-api-server-to-nodes-pods-and-services-4659e7b7
type: concept
title: API server to nodes, pods, and services
description: The connections from the API server to a node, pod, or service default
  to plain HTTP connections
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### API server to nodes, pods, and services

The connections from the API server to a node, pod, or service default to plain HTTP connections
and are therefore neither authenticated nor encrypted. They can be run over a secure HTTPS
connection by prefixing `https:` to the node, pod, or service name in the API URL, but they will
not validate the certificate provided by the HTTPS endpoint nor provide client credentials. So
while the connection will be encrypted, it will not provide any guarantees of integrity. These
connections **are not currently safe** to run over untrusted or public networks.