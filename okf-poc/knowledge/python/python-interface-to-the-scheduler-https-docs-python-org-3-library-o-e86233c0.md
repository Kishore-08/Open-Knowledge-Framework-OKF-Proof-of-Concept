---
id: python-interface-to-the-scheduler-https-docs-python-org-3-library-o-e86233c0
type: concept
title: Interface to the scheduler[¶](https://docs.python.org/3/library/os.html#interface-to-the-scheduler
  "Link to this heading")
description: These functions control how a process is allocated CPU time by the operating
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Interface to the scheduler[¶](https://docs.python.org/3/library/os.html#interface-to-the-scheduler "Link to this heading")

These functions control how a process is allocated CPU time by the operating
system. They are only available on some Unix platforms. For more detailed
information, consult your Unix manpages.

Added in version 3.3.

The following scheduling policies are exposed if they are supported by the
operating system.

os.SCHED\_OTHER[¶](https://docs.python.org/3/library/os.html#os.SCHED_OTHER "Link to this definition")
:   The default scheduling policy.

os.SCHED\_BATCH[¶](https://docs.python.org/3/library/os.html#os.SCHED_BATCH "Link to this definition")
:   Scheduling policy for CPU-intensive processes that tries to preserve
    interactivity on the rest of the computer.

os.SCHED\_DEADLINE[¶](https://docs.python.org/3/library/os.html#os.SCHED_DEADLINE "Link to this definition")
:   Scheduling policy for tasks with deadline constraints.

    Added in version 3.14.

os.SCHED\_IDLE[¶](https://docs.python.org/3/library/os.html#os.SCHED_IDLE "Link to this definition")
:   Scheduling policy for extremely low priority background tasks.

os.SCHED\_NORMAL[¶](https://docs.python.org/3/library/os.html#os.SCHED_NORMAL "Link to this definition")
:   Alias for [`SCHED_OTHER`](https://docs.python.org/3/library/os.html#os.SCHED_OTHER "os.SCHED_OTHER").

    Added in version 3.14.

os.SCHED\_SPORADIC[¶](https://docs.python.org/3/library/os.html#os.SCHED_SPORADIC "Link to this definition")
:   Scheduling policy for sporadic server programs.

os.SCHED\_FIFO[¶](https://docs.python.org/3/library/os.html#os.SCHED_FIFO "Link to this definition")
:   A First In First Out scheduling policy.

os.SCHED\_RR[¶](https://docs.python.org/3/library/os.html#os.SCHED_RR "Link to this definition")
:   A round-robin scheduling policy.

os.SCHED\_RESET\_ON\_FORK[¶](https://docs.python.org/3/library/os.html#os.SCHED_RESET_ON_FORK "Link to this definition")
:   This flag can be OR’ed with any other scheduling policy. When a process with
    this flag set forks, its child’s scheduling policy and priority are reset to
    the default.

*class* os.sched\_param(*sched\_priority*)[¶](https://docs.python.org/3/library/os.html#os.sched_param "Link to this definition")
:   This class represents tunable scheduling parameters used in
    [`sched_setparam()`](https://docs.python.org/3/library/os.html#os.sched_setparam "os.sched_setparam"), [`sched_setscheduler()`](https://docs.python.org/3/library/os.html#os.sched_setscheduler "os.sched_setscheduler"), and
    [`sched_getparam()`](https://docs.python.org/3/library/os.html#os.sched_getparam "os.sched_getparam"). It is immutable.

    At the moment, there is only one possible parameter:

    sched\_priority[¶](https://docs.python.org/3/library/os.html#os.sched_param.sched_priority "Link to this definition")
    :   The scheduling priority for a scheduling policy.

os.sched\_get\_priority\_min(*policy*)[¶](https://docs.python.org/3/library/os.html#os.sched_get_priority_min "Link to this definition")
:   Get the minimum priority value for *policy*. *policy* is one of the
    scheduling policy constants above.

os.sched\_get\_priority\_max(*policy*)[¶](https://docs.python.org/3/library/os.html#os.sched_get_priority_max "Link to this definition")
:   Get the maximum priority value for *policy*. *policy* is one of the
    scheduling policy constants above.

os.sched\_setscheduler(*pid*, *policy*, *param*, */*)[¶](https://docs.python.org/3/library/os.html#os.sched_setscheduler "Link to this definition")
:   Set the scheduling policy for the process with PID *pid*. A *pid* of 0 means
    the calling process. *policy* is one of the scheduling policy constants
    above. *param* is a [`sched_param`](https://docs.python.org/3/library/os.html#os.sched_param "os.sched_param") instance.

os.sched\_getscheduler(*pid*, */*)[¶](https://docs.python.org/3/library/os.html#os.sched_getscheduler "Link to this definition")
:   Retur