---
id: kubernetes-scaling-policies-cdcbb833
type: concept
title: Scaling policies
description: One or more scaling policies can be specified in the `behavior` section
  of the spec.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Scaling policies

One or more scaling policies can be specified in the `behavior` section of the spec.
When multiple policies are specified the policy which allows the highest amount of
change is the policy which is selected by default. The following example shows this behavior
while scaling down:

```
behavior:
  scaleDown:
    policies:
    - type: Pods
      value: 4
      periodSeconds: 60
    - type: Percent
      value: 10
      periodSeconds: 60
```

`periodSeconds` indicates the length of time in the past for which the policy must hold true.
The maximum value that you can set for `periodSeconds` is 1800 (half an hour).
The first policy *(Pods)* allows at most 4 replicas to be scaled down in one minute. The second policy
*(Percent)* allows at most 10% of the current replicas to be scaled down in one minute.

Since by default the policy which allows the highest amount of change is selected, the second policy will
only be used when the number of pod replicas is more than 40. With 40 or less replicas, the first policy will be applied.
For instance if there are 80 replicas and the target has to be scaled down to 10 replicas
then during the first step 8 replicas will be reduced. In the next iteration when the number
of replicas is 72, 10% of the pods is 7.2 but the number is rounded up to 8. On each loop of
the autoscaler controller the number of pods to be change is re-calculated based on the number
of current replicas. When the number of replicas falls below 40 the first policy *(Pods)* is applied
and 4 replicas will be reduced at a time.

The policy selection can be changed by specifying the `selectPolicy` field for a scaling
direction. By setting the value to `Min` which would select the policy which allows the
smallest change in the replica count. Setting the value to `Disabled` completely disables
scaling in that direction.