---
id: kubernetes-how-kubernetes-resourcequotas-work-193abbf6
type: concept
title: How Kubernetes ResourceQuotas work
description: 'ResourceQuotas work like this:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## How Kubernetes ResourceQuotas work

ResourceQuotas work like this:

- Different teams work in different namespaces. This separation can be enforced with
  [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) or any other [authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
  mechanism.
- A cluster administrator creates at least one ResourceQuota for each namespace.

  - To make sure the enforcement stays enforced, the cluster administrator should also restrict access to delete or update
    that ResourceQuota; for example, by defining a [ValidatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/).
- Users create resources (pods, services, etc.) in the namespace, and the quota system
  tracks usage to ensure it does not exceed hard resource limits defined in a ResourceQuota.

  You can apply a [scope](https://kubernetes.io/docs/concepts/policy/resource-quotas/#quota-scopes) to a ResourceQuota to limit where it applies,
- If creating or updating a resource violates a quota constraint, the control plane rejects that request with HTTP
  status code `403 Forbidden`. The error includes a message explaining the constraint that would have been violated.
- If quotas are enabled in a namespace for [resource](https://kubernetes.io/docs/reference/glossary/?all=true#term-infrastructure-resource "A defined amount of infrastructure available for consumption (CPU, memory, etc).")
  such as `cpu` and `memory`, users must specify requests or limits for those values when they define a Pod; otherwise,
  the quota system may reject pod creation.

  The resource quota [walkthrough](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
  shows an example of how to avoid this problem.

#### Note:

- You can define a [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/)
  to force defaults on pods that make no compute resource requirements (so that users don't have to remember to do that).

You often do not create Pods directly; for example, you more usually create a [workload management](https://kubernetes.io/docs/concepts/workloads/controllers/)
object such as a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "Manages a replicated application on your cluster."). If you create a Deployment that tries to use more
resources than are available, the creation of the Deployment (or other workload management object) **succeeds**, but
the Deployment may not be able to get all of the Pods it manages to exist. In that case you can check the status of
the Deployment, for example with `kubectl describe`, to see what has happened.

- For `cpu` and `memory` resources, ResourceQuotas enforce that **every**
  (new) pod in that namespace sets a limit for that resource.
  If you enforce a resource quota in a namespace for either `cpu` or `memory`,
  you and other clients, **must** specify either `requests` or `limits` for that resource,
  for every new Pod you submit. If you don't, the control plane may reject admission
  for that Pod.
- For other resources: ResourceQuota works and will ignore pods in the namespace without
  setting a limit or request for that resource. It means that you can create a new pod
  without limit/request for ephemeral storage if the resource quota limits the ephemeral
  storage of this namespace.

You can use a [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/) to automatically set
a default request for these resources.

The name of a ResourceQuota object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

Examples of policies that could be created using namespaces and quotas are:

- In a cluster with a capacity of 32 GiB RAM, and 16 cores, let team A use 20 GiB and 10 cores,
  let B use 10GiB and 4 cores, and hold 2GiB and 2 cores in reserve