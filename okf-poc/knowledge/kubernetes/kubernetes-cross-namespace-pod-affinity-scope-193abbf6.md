---
id: kubernetes-cross-namespace-pod-affinity-scope-193abbf6
type: concept
title: Cross-namespace pod affinity scope
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Cross-namespace pod affinity scope

FEATURE STATE:
`Kubernetes v1.24 [stable]`

You can use `CrossNamespacePodAffinity` [quota scope](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scopes) to limit which namespaces are allowed to
have pods with affinity terms that cross namespaces. Specifically, it controls which pods are allowed
to set `namespaces` or `namespaceSelector` fields in pod [(anti)affinity terms](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).

Preventing users from using cross-namespace affinity terms might be desired since a pod
with anti-affinity constraints can block pods from all other namespaces
from getting scheduled in a failure domain.

Using this scope, you (as a cluster administrator) can prevent certain namespaces - such as `foo-ns` in the example below -
from having pods that use cross-namespace pod affinity. You configure this creating a ResourceQuota object in
that namespace with `CrossNamespacePodAffinity` scope and hard limit of 0:

```
apiVersion: v1
kind: ResourceQuota
metadata:
  name: disable-cross-namespace-affinity
  namespace: foo-ns
spec:
  hard:
    pods: "0"
  scopeSelector:
    matchExpressions:
    - scopeName: CrossNamespacePodAffinity
      operator: Exists
```

If you want to disallow using `namespaces` and `namespaceSelector` by default, and
only allow it for specific namespaces, you could configure `CrossNamespacePodAffinity`
as a limited resource by setting the kube-apiserver flag `--admission-control-config-file`
to the path of the following configuration file:

```
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: "ResourceQuota"
  configuration:
    apiVersion: apiserver.config.k8s.io/v1
    kind: ResourceQuotaConfiguration
    limitedResources:
    - resource: pods
      matchScopes:
      - scopeName: CrossNamespacePodAffinity
        operator: Exists
```

With the above configuration, pods can use `namespaces` and `namespaceSelector` in pod affinity only
if the namespace where they are created have a resource quota object with
`CrossNamespacePodAffinity` scope and a hard limit greater than or equal to the number of pods using those fields.