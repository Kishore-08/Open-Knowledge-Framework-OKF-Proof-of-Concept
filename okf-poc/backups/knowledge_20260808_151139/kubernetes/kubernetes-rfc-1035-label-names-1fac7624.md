---
id: kubernetes-rfc-1035-label-names-1fac7624
type: concept
title: RFC 1035 Label Names
description: Some resource types require their names to follow the DNS
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### RFC 1035 Label Names

Some resource types require their names to follow the DNS
label standard as defined in [RFC 1035](https://tools.ietf.org/html/rfc1035).
This means the name must:

- contain at most 63 characters
- contain only lowercase alphanumeric characters or '-'
- start with an alphabetic character
- end with an alphanumeric character

#### Note:

While RFC 1123 technically allows labels to start with digits, the current
Kubernetes implementation requires both RFC 1035 and RFC 1123 labels to start
with an alphabetic character. The exception is when the `RelaxedServiceNameValidation`
feature gate is enabled for Service objects, which allows Service names to start with digits.