---
id: kubernetes-success-policy-bc994bad
type: concept
title: Success policy
description: When creating an Indexed Job, you can define when a Job can be declared
  as succeeded using a `.spec.successPolicy`,
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Success policy

When creating an Indexed Job, you can define when a Job can be declared as succeeded using a `.spec.successPolicy`,
based on the pods that succeeded.

By default, a Job succeeds when the number of succeeded Pods equals `.spec.completions`.
These are some situations where you might want additional control for declaring a Job succeeded:

- When running simulations with different parameters,
  you might not need all the simulations to succeed for the overall Job to be successful.
- When following a leader-worker pattern, only the success of the leader determines the success or
  failure of a Job. Examples of this are frameworks like MPI and PyTorch etc.

You can configure a success policy, in the `.spec.successPolicy` field,
to meet the above use cases. This policy can handle Job success based on the
succeeded pods. After the Job meets the success policy, the job controller terminates the lingering Pods.
A success policy is defined by rules. Each rule can take one of the following forms:

- When you specify the `succeededIndexes` only,
  once all indexes specified in the `succeededIndexes` succeed, the job controller marks the Job as succeeded.
  The `succeededIndexes` must be a list of intervals between 0 and `.spec.completions-1`.
- When you specify the `succeededCount` only,
  once the number of succeeded indexes reaches the `succeededCount`, the job controller marks the Job as succeeded.
- When you specify both `succeededIndexes` and `succeededCount`,
  once the number of succeeded indexes from the subset of indexes specified in the `succeededIndexes` reaches the `succeededCount`,
  the job controller marks the Job as succeeded.

Note that when you specify multiple rules in the `.spec.successPolicy.rules`,
the job controller evaluates the rules in order. Once the Job meets a rule, the job controller ignores remaining rules.

Here is a manifest for a Job with `successPolicy`:

[`/controllers/job-success-policy.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples//controllers/job-success-policy.yaml)![](https://kubernetes.io/images/copycode.svg "Copy /controllers/job-success-policy.yaml to clipboard")

```
apiVersion: batch/v1
kind: Job
metadata:
  name: job-success
spec:
  parallelism: 10
  completions: 10
  completionMode: Indexed # Required for the success policy
  successPolicy:
    rules:
      - succeededIndexes: 0,2-3
        succeededCount: 1
  template:
    spec:
      containers:
      - name: main
        image: python
        command:          # Provided that at least one of the Pods with 0, 2, and 3 indexes has succeeded,
                          # the overall Job is a success.
          - python3
          - -c
          - |
            import os, sys
            if os.environ.get("JOB_COMPLETION_INDEX") == "2":
              sys.exit(0)
            else:
              sys.exit(1)
      restartPolicy: Never
```

In the example above, both `succeededIndexes` and `succeededCount` have been specified.
Therefore, the job controller will mark the Job as succeeded and terminate the lingering Pods
when either of the specified indexes, 0, 2, or 3, succeed.
The Job that meets the success policy gets the `SuccessCriteriaMet` condition with a `SuccessPolicy` reason.
After the removal of the lingering Pods is issued, the Job gets the `Complete` condition.

Note that the `succeededIndexes` is represented as intervals separated by a hyphen.
The number are listed in represented by the first and last element of the series, separated by a hyphen.

#### Note:

When you specify both a success policy and some terminating policies such as `.spec.backoffLimit` and `.spec.podFailurePolicy`,
once the Job meets either policy, the job controller respects the terminating policy and ignores the success policy.