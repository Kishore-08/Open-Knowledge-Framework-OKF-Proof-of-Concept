---
id: kubernetes-design-principles-ca23283c
type: concept
title: Design principles
description: 'The following principles shaped the design and architecture of Gateway
  API:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Design principles

The following principles shaped the design and architecture of Gateway API:

- **Role-oriented:** Gateway API kinds are modeled after organizational roles that are
  responsible for managing Kubernetes service networking:
  - **Infrastructure Provider:** Manages infrastructure that allows multiple isolated clusters
    to serve multiple tenants, e.g. a cloud provider.
  - **Cluster Operator:** Manages clusters and is typically concerned with policies, network
    access, application permissions, etc.
  - **Application Developer:** Manages an application running in a cluster and is typically
    concerned with application-level configuration and [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
    composition.
- **Portable:** Gateway API specifications are defined as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
  and are supported by many [implementations](https://gateway-api.sigs.k8s.io/implementations/).
- **Expressive:** Gateway API kinds support functionality for common traffic routing use cases
  such as header-based matching, traffic weighting, and others that were only possible in
  [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) by using custom annotations.
- **Extensible:** Gateway allows for custom resources to be linked at various layers of the API.
  This makes granular customization possible at the appropriate places within the API structure.