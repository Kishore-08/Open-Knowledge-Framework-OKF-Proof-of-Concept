---
id: kubernetes-rfc-1123-label-names-1fac7624
type: concept
title: RFC 1123 Label Names
description: Some resource types require their names to follow the DNS
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### RFC 1123 Label Names

Some resource types require their names to follow the DNS
label standard as defined in [RFC 1123](https://tools.ietf.org/html/rfc1123).
This means the name must:

- contain at most 63 characters
- contain only lowercase alphanumeric characters or '-'
- start with an alphabetic character
- end with an alphanumeric character

#### Note:

When the `RelaxedServiceNameValidation` feature gate is enabled,
Service object names are allowed to start with a digit.