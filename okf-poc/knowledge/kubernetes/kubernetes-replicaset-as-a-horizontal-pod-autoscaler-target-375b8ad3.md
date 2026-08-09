---
id: kubernetes-replicaset-as-a-horizontal-pod-autoscaler-target-375b8ad3
type: concept
title: ReplicaSet as a Horizontal Pod Autoscaler Target
description: A ReplicaSet can also be a target for
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### ReplicaSet as a Horizontal Pod Autoscaler Target

A ReplicaSet can also be a target for
[Horizontal Pod Autoscalers (HPA)](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/). That is,
a ReplicaSet can be auto-scaled by an HPA. Here is an example HPA targeting
the ReplicaSet we created in the previous example.

[`controllers/hpa-rs.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/controllers/hpa-rs.yaml)![](https://kubernetes.io/images/copycode.svg "Copy controllers/hpa-rs.yaml to clipboard")

```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: frontend-scaler
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: ReplicaSet
    name: frontend
  minReplicas: 3
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

Saving this manifest into `hpa-rs.yaml` and submitting it to a Kubernetes cluster should
create the defined HPA that autoscales the target ReplicaSet depending on the CPU usage
of the replicated Pods.

```
kubectl apply -f https://k8s.io/examples/controllers/hpa-rs.yaml
```

Alternatively, you can use the `kubectl autoscale` command to accomplish the same
(and it's easier!)

```
kubectl autoscale rs frontend --max=10 --min=3 --cpu=50%
```

## Alternatives to ReplicaSet