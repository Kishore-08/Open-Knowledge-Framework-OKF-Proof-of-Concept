---
id: kubernetes-quota-for-extended-resources-193abbf6
type: concept
title: Quota for extended resources
description: In addition to the resources mentioned above, in release 1.10, quota
  support for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Quota for extended resources

In addition to the resources mentioned above, in release 1.10, quota support for
[extended resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources) is added.

As overcommit is not allowed for extended resources, it makes no sense to specify both `requests`
and `limits` for the same extended resource in a quota. So for extended resources, only quota items
with prefix `requests.` are allowed.

Take the GPU resource as an example, if the resource name is `nvidia.com/gpu`, and you want to
limit the total number of GPUs requested in a namespace to 4, you can define a quota as follows:

- `requests.nvidia.com/gpu: 4`

See [Viewing and Setting Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/#viewing-and-setting-quotas) for more details.