---
id: kubernetes-quota-on-object-count-193abbf6
type: concept
title: Quota on object count
description: You can set quota for *the total number of one particular [resource](https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology
  "A Kubernetes entity, representing an endpoin
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Quota on object count

You can set quota for *the total number of one particular [resource](https://kubernetes.io/docs/reference/using-api/api-concepts/#standard-api-terminology "A Kubernetes entity, representing an endpoint on the Kubernetes API server.") kind* in the Kubernetes API,
using the following syntax:

- `count/<resource>.<group>` for resources from non-core API groups
- `count/<resource>` for resources from the core API group

For example, the PodTemplate API is in the core API group and so if you want to limit the number of
PodTemplate objects in a namespace, you use `count/podtemplates`.

These types of quotas are useful to protect against exhaustion of control plane storage. For example, you may
want to limit the number of Secrets in a server given their large size. Too many Secrets in a cluster can
actually prevent servers and controllers from starting. You can set a quota for Jobs to protect against
a poorly configured CronJob. CronJobs that create too many Jobs in a namespace can lead to a denial of service.

If you define a quota this way, it applies to Kubernetes' APIs that are part of the API server, and
to any custom resources backed by a CustomResourceDefinition.
For example, to create a quota on a `widgets` custom resource in the `example.com` API group,
use `count/widgets.example.com`.
If you use [API aggregation](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/) to
add additional, custom APIs that are not defined as CustomResourceDefinitions, the core Kubernetes
control plane does not enforce quota for the aggregated API. The extension API server is expected to
provide quota enforcement if that's appropriate for the custom API.

##### Generic syntax

This is a list of common examples of object kinds that you may want to put under object count quota,
listed by the configuration string that you would use.

- `count/pods`
- `count/persistentvolumeclaims`
- `count/services`
- `count/secrets`
- `count/configmaps`
- `count/deployments.apps`
- `count/replicasets.apps`
- `count/statefulsets.apps`
- `count/jobs.batch`
- `count/cronjobs.batch`

##### Specialized syntax

There is another syntax only to set the same type of quota, that only works for certain API kinds.
The following types are supported:

| Resource Name | Description |
| --- | --- |
| `configmaps` | The total number of ConfigMaps that can exist in the namespace. |
| `persistentvolumeclaims` | The total number of [PersistentVolumeClaims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) that can exist in the namespace. |
| `pods` | The total number of Pods in a non-terminal state that can exist in the namespace. A pod is in a terminal state if `.status.phase in (Failed, Succeeded)` is true. |
| `replicationcontrollers` | The total number of ReplicationControllers that can exist in the namespace. |
| `resourcequotas` | The total number of ResourceQuotas that can exist in the namespace. |
| `services` | The total number of Services that can exist in the namespace. |
| `services.loadbalancers` | The total number of Services of type `LoadBalancer` that can exist in the namespace. |
| `services.nodeports` | The total number of `NodePorts` allocated to Services of type `NodePort` or `LoadBalancer` that can exist in the namespace. |
| `secrets` | The total number of Secrets that can exist in the namespace. |

For example, `pods` quota counts and enforces a maximum on the number of `pods`
created in a single namespace that are not terminal. You might want to set a `pods`
quota on a namespace to avoid the case where a user creates many small pods and
exhausts the cluster's supply of Pod IPs.

You can find more examples on [Viewing and Setting Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/#viewing-and-setting-quotas).