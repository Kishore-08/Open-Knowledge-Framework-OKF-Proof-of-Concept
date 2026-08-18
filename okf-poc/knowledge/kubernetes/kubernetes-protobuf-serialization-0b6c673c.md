---
id: kubernetes-protobuf-serialization-0b6c673c
type: concept
title: Protobuf serialization
description: Kubernetes implements an alternative Protobuf based serialization format
  that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/kubernetes-api/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Protobuf serialization

Kubernetes implements an alternative Protobuf based serialization format that
is primarily intended for intra-cluster communication. For more information
about this format, see the [Kubernetes Protobuf serialization](https://git.k8s.io/design-proposals-archive/api-machinery/protobuf.md)
design proposal and the
Interface Definition Language (IDL) files for each schema located in the Go
packages that define the API objects.