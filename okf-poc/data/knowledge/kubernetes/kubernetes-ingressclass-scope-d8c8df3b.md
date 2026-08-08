---
id: kubernetes-ingressclass-scope-d8c8df3b
type: concept
title: IngressClass scope
description: Depending on your ingress controller, you may be able to use parameters
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/ingress/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### IngressClass scope

Depending on your ingress controller, you may be able to use parameters
that you set cluster-wide, or just for one namespace.



The default scope for IngressClass parameters is cluster-wide.

If you set the `.spec.parameters` field and don't set
`.spec.parameters.scope`, or if you set `.spec.parameters.scope` to
`Cluster`, then the IngressClass refers to a cluster-scoped resource.
The `kind` (in combination the `apiGroup`) of the parameters
refers to a cluster-scoped API (possibly a custom resource), and
the `name` of the parameters identifies a specific cluster scoped
resource for that API.

For example:

```
---
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-1
spec:
  controller: example.com/ingress-controller
  parameters:
    # The parameters for this IngressClass are specified in a
    # ClusterIngressParameter (API group k8s.example.net) named
    # "external-config-1". This definition tells Kubernetes to
    # look for a cluster-scoped parameter resource.
    scope: Cluster
    apiGroup: k8s.example.net
    kind: ClusterIngressParameter
    name: external-config-1
```

FEATURE STATE:
`Kubernetes v1.23 [stable]`

If you set the `.spec.parameters` field and set
`.spec.parameters.scope` to `Namespace`, then the IngressClass refers
to a namespaced-scoped resource. You must also set the `namespace`
field within `.spec.parameters` to the namespace that contains
the parameters you want to use.

The `kind` (in combination the `apiGroup`) of the parameters
refers to a namespaced API (for example: ConfigMap), and
the `name` of the parameters identifies a specific resource
in the namespace you specified in `namespace`.

Namespace-scoped parameters help the cluster operator delegate control over the
configuration (for example: load balancer settings, API gateway definition)
that is used for a workload. If you used a cluster-scoped parameter then either:

- the cluster operator team needs to approve a different team's changes every
  time there's a new configuration change being applied.
- the cluster operator must define specific access controls, such as
  [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) roles and bindings, that let
  the application team make changes to the cluster-scoped parameters resource.

The IngressClass API itself is always cluster-scoped.

Here is an example of an IngressClass that refers to parameters that are
namespaced:

```
---
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-2
spec:
  controller: example.com/ingress-controller
  parameters:
    # The parameters for this IngressClass are specified in an
    # IngressParameter (API group k8s.example.com) named "external-config",
    # that's in the "external-configuration" namespace.
    scope: Namespace
    apiGroup: k8s.example.com
    kind: IngressParameter
    namespace: external-configuration
    name: external-config
```