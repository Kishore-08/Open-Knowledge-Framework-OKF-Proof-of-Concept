---
id: kubernetes-job-patterns-bc994bad
type: concept
title: Job patterns
description: The Job object can be used to process a set of independent but related
  *work items*.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Job patterns

The Job object can be used to process a set of independent but related *work items*.
These might be emails to be sent, frames to be rendered, files to be transcoded,
ranges of keys in a NoSQL database to scan, and so on.

In a complex system, there may be multiple different sets of work items. Here we are just
considering one set of work items that the user wants to manage together — a *batch job*.

There are several different patterns for parallel computation, each with strengths and weaknesses.
The tradeoffs are:

- One Job object for each work item, versus a single Job object for all work items.
  One Job per work item creates some overhead for the user and for the system to manage
  large numbers of Job objects.
  A single Job for all work items is better for large numbers of items.
- Number of Pods created equals number of work items, versus each Pod can process multiple work items.
  When the number of Pods equals the number of work items, the Pods typically
  requires less modification to existing code and containers. Having each Pod
  process multiple work items is better for large numbers of items.
- Several approaches use a work queue. This requires running a queue service,
  and modifications to the existing program or container to make it use the work queue.
  Other approaches are easier to adapt to an existing containerised application.
- When the Job is associated with a
  [headless Service](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services),
  you can enable the Pods within a Job to communicate with each other to
  collaborate in a computation.

The tradeoffs are summarized here, with columns 2 to 4 corresponding to the above tradeoffs.
The pattern names are also links to examples and more detailed description.

| Pattern | Single Job object | Fewer pods than work items? | Use app unmodified? |
| --- | --- | --- | --- |
| [Queue with Pod Per Work Item](https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/) | ✓ |  | sometimes |
| [Queue with Variable Pod Count](https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/) | ✓ | ✓ |  |
| [Indexed Job with Static Work Assignment](https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/) | ✓ |  | ✓ |
| [Job with Pod-to-Pod Communication](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/) | ✓ | sometimes | sometimes |
| [Job Template Expansion](https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/) |  |  | ✓ |

When you specify completions with `.spec.completions`, each Pod created by the Job controller
has an identical [`spec`](https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status).
This means that all pods for a task will have the same command line and the same
image, the same volumes, and (almost) the same environment variables. These patterns
are different ways to arrange for pods to work on different things.

This table shows the required settings for `.spec.parallelism` and `.spec.completions` for each of the patterns.
Here, `W` is the number of work items.

| Pattern | `.spec.completions` | `.spec.parallelism` |
| --- | --- | --- |
| [Queue with Pod Per Work Item](https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/) | W | any |
| [Queue with Variable Pod Count](https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/) | null | any |
| [Indexed Job with Static Work Assignment](https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/) | W | any |
| [Job with Pod-to-Pod Communication](https://kubernetes.io/docs/tasks/job/job-with-pod-to-pod-communication/) | W | W |
| [Job Template Expansion](https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/) | 1 | should be 1 |

## Advanced usage