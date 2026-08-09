---
id: kubernetes-limitrange-and-admission-checks-for-pods-76e54018
type: concept
title: LimitRange and admission checks for Pods
description: A LimitRange does **not** check the consistency of the default values
  it applies.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/policy/limit-range/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## LimitRange and admission checks for Pods

A LimitRange does **not** check the consistency of the default values it applies.
This means that a default value for the *limit* that is set by LimitRange may be
less than the *request* value specified for the container in the spec that a client
submits to the API server. If that happens, the final Pod will not be schedulable.

For example, you define a LimitRange with below manifest:

#### Note:

The following examples operate within the default namespace of your cluster, as the namespace
parameter is undefined and the LimitRange scope is limited to the namespace level.
This implies that any references or operations within these examples will interact
with elements within the default namespace of your cluster. You can override the
operating namespace by configuring namespace in the `metadata.namespace` field.

[`concepts/policy/limit-range/problematic-limit-range.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/concepts/policy/limit-range/problematic-limit-range.yaml)![](https://kubernetes.io/images/copycode.svg "Copy concepts/policy/limit-range/problematic-limit-range.yaml to clipboard")

```
apiVersion: v1
kind: LimitRange
metadata:
  name: cpu-resource-constraint
spec:
  limits:
  - default: # this section defines default limits
      cpu: 500m
    defaultRequest: # this section defines default requests
      cpu: 500m
    max: # max and min define the limit range
      cpu: "1"
    min:
      cpu: 100m
    type: Container
```

along with a Pod that declares a CPU resource request of `700m`, but not a limit:

[`concepts/policy/limit-range/example-conflict-with-limitrange-cpu.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/concepts/policy/limit-range/example-conflict-with-limitrange-cpu.yaml)![](https://kubernetes.io/images/copycode.svg "Copy concepts/policy/limit-range/example-conflict-with-limitrange-cpu.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: example-conflict-with-limitrange-cpu
spec:
  containers:
  - name: demo
    image: registry.k8s.io/pause:3.8
    resources:
      requests:
        cpu: 700m
```

then that Pod will not be scheduled, failing with an error similar to:

```
Pod "example-conflict-with-limitrange-cpu" is invalid: spec.containers[0].resources.requests: Invalid value: "700m": must be less than or equal to cpu limit
```

If you set both `request` and `limit`, then that new Pod will be scheduled successfully
even with the same LimitRange in place:

[`concepts/policy/limit-range/example-no-conflict-with-limitrange-cpu.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/concepts/policy/limit-range/example-no-conflict-with-limitrange-cpu.yaml)![](https://kubernetes.io/images/copycode.svg "Copy concepts/policy/limit-range/example-no-conflict-with-limitrange-cpu.yaml to clipboard")

```
apiVersion: v1
kind: Pod
metadata:
  name: example-no-conflict-with-limitrange-cpu
spec:
  containers:
  - name: demo
    image: registry.k8s.io/pause:3.8
    resources:
      requests:
        cpu: 700m
      limits:
        cpu: 700m
```