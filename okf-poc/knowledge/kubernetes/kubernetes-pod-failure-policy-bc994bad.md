---
id: kubernetes-pod-failure-policy-bc994bad
type: concept
title: Pod failure policy
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Pod failure policy

FEATURE STATE:
`Kubernetes v1.31 [stable]`(enabled by default)

A Pod failure policy, defined with the `.spec.podFailurePolicy` field, enables
your cluster to handle Pod failures based on the container exit codes and the
Pod conditions.

In some situations, you may want to have a better control when handling Pod
failures than the control provided by the [Pod backoff failure policy](https://kubernetes.io/docs/concepts/workloads/controllers/job/#pod-backoff-failure-policy),
which is based on the Job's `.spec.backoffLimit`. These are some examples of use cases:

- To optimize costs of running workloads by avoiding unnecessary Pod restarts,
  you can terminate a Job as soon as one of its Pods fails with an exit code
  indicating a software bug.
- To guarantee that your Job finishes even if there are disruptions, you can
  ignore Pod failures caused by disruptions (such as [preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption "Preemption logic in Kubernetes helps a pending Pod to find a suitable Node by evicting low priority Pods existing on that Node."),
  [API-initiated eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/ "API-initiated eviction is the process by which you use the Eviction API to create an Eviction object that triggers graceful pod termination.")
  or [taint](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "A core object consisting of three required properties: key, value, and effect. Taints prevent the scheduling of pods on nodes or node groups.")-based eviction) so
  that they don't count towards the `.spec.backoffLimit` limit of retries.

You can configure a Pod failure policy, in the `.spec.podFailurePolicy` field,
to meet the above use cases. This policy can handle Pod failures based on the
container exit codes and the Pod conditions.

Here is a manifest for a Job that defines a `podFailurePolicy`:

[`/controllers/job-pod-failure-policy-example.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples//controllers/job-pod-failure-policy-example.yaml)![](https://kubernetes.io/images/copycode.svg "Copy /controllers/job-pod-failure-policy-example.yaml to clipboard")

```
apiVersion: batch/v1
kind: Job
metadata:
  name: job-pod-failure-policy-example
spec:
  completions: 12
  parallelism: 3
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: main
        image: docker.io/library/bash:5
        command: ["bash"]        # example command simulating a bug which triggers the FailJob action
        args:
        - -c
        - echo "Hello world!" && sleep 5 && exit 42
  backoffLimit: 6
  podFailurePolicy:
    rules:
    - action: FailJob
      onExitCodes:
        containerName: main      # optional
        operator: In             # one of: In, NotIn
        values: [42]
    - action: Ignore             # one of: Ignore, FailJob, Count
      onPodConditions:
      - type: DisruptionTarget   # indicates Pod disruption
```

In the example above, the first rule of the Pod failure policy specifies that
the Job should be marked failed if the `main` container fails with the 42 exit
code. The following are the rules for the `main` container specifically:

- an exit code of 0 means that the container succeeded
- an exit code of 42 means that the **entire Job** failed
- any other exit code represents that the container failed, and hence the entire
  Pod. The Pod will be re-created if the total number of restarts is
  below `backoffLimit`. If the `backoffLimit` is reached the **entire Job** failed.

#### Note:

Because the Pod template specifies a `restartPolicy: Never`,
the kubelet does not restart the `main` container in that particular Pod.

The second rule of the Pod failure policy, specifying the `Ignore` action for
failed Pods with condition `DisruptionTarget` excludes Pod disruptions from
being counted towards the `.spec.backoffLimit`