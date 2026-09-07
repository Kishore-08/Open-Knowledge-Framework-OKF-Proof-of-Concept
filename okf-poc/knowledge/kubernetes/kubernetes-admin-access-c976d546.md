---
id: kubernetes-admin-access-c976d546
type: concept
title: Admin access
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Admin access

FEATURE STATE:
`Kubernetes v1.36 [stable]`(enabled by default)

You can mark a request in a ResourceClaim or ResourceClaimTemplate as having
privileged features for maintenance and troubleshooting tasks. A request with
admin access grants access to in-use devices and may enable additional
permissions when making the device available in a container:

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: large-black-cat-claim-template
spec:
  spec:
    devices:
      requests:
      - name: req-0
        exactly:
          deviceClassName: resource.example.com
          allocationMode: All
          adminAccess: true
```

Admin access is a privileged mode and should not be granted to regular users in
multi-tenant clusters. Only users authorized to
create ResourceClaim or ResourceClaimTemplate objects in namespaces labeled with
`resource.kubernetes.io/admin-access: "true"` (case-sensitive) can use the
`adminAccess` field. This ensures that non-admin users cannot misuse the
feature.

Admin access is controlled by the
[`DRAAdminAccess` feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#DRAAdminAccess)
in the `kube-apiserver`, `kube-scheduler`, and `kubelet`.