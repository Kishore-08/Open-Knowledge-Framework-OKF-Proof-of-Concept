---
id: kubernetes-application-protocol-fb91f326
type: concept
title: Application protocol
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Application protocol

FEATURE STATE:
`Kubernetes v1.20 [stable]`

The `appProtocol` field provides a way to specify an application protocol for
each Service port. This is used as a hint for implementations to offer
richer behavior for protocols that they understand.
The value of this field is mirrored by the corresponding
Endpoints and EndpointSlice objects.

This field follows standard Kubernetes label syntax. Valid values are one of:

- [IANA standard service names](https://www.iana.org/assignments/service-names).
- Implementation-defined prefixed names such as `mycompany.com/my-custom-protocol`.
- Kubernetes-defined prefixed names:

| Protocol | Description |
| --- | --- |
| `kubernetes.io/h2c` | HTTP/2 over cleartext as described in [RFC 9113](https://www.rfc-editor.org/rfc/rfc9113) |
| `kubernetes.io/ws` | WebSocket over cleartext as described in [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) |
| `kubernetes.io/wss` | WebSocket over TLS as described in [RFC 6455](https://www.rfc-editor.org/rfc/rfc6455) |