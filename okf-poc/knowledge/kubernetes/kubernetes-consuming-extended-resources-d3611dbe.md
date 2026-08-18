---
id: kubernetes-consuming-extended-resources-d3611dbe
type: concept
title: Consuming extended resources
description: Users can consume extended resources in Pod specs like CPU and memory.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Consuming extended resources

Users can consume extended resources in Pod specs like CPU and memory.
The scheduler takes care of the resource accounting so that no more than the
available amount is simultaneously allocated to Pods.

The API server restricts quantities of extended resources to whole numbers.
Examples of *valid* quantities are `3`, `3000m` and `3Ki`. Examples of
*invalid* quantities are `0.5` and `1500m` (because `1500m` would result in `1.5`).

#### Note:

Extended resources replace Opaque Integer Resources.
Users can use any domain name prefix other than `kubernetes.io` which is reserved.

To consume an extended resource in a Pod, include the resource name as a key
in the `spec.containers[].resources.limits` map in the container spec.

#### Note:

Extended resources cannot be overcommitted, so request and limit
must be equal if both are present in a container spec.

A Pod is scheduled only if all of the resource requests are satisfied, including
CPU, memory and any extended resources. The Pod remains in the `PENDING` state
as long as the resource request cannot be satisfied.

**Example:**

The Pod below requests 2 CPUs and 1 "example.com/foo" (an extended resource).

```
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: myimage
    resources:
      requests:
        cpu: 2
        example.com/foo: 1
      limits:
        example.com/foo: 1
```