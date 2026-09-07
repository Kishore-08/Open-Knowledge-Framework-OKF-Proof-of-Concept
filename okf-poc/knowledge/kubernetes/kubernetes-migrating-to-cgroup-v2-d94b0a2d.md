---
id: kubernetes-migrating-to-cgroup-v2-d94b0a2d
type: concept
title: Migrating to cgroup v2
description: To migrate to cgroup v2, ensure that you meet the [requirements](https://kubernetes.io/docs/concepts/architecture/cgroups/#requirements),
  then upgrade
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cgroups/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Migrating to cgroup v2

To migrate to cgroup v2, ensure that you meet the [requirements](https://kubernetes.io/docs/concepts/architecture/cgroups/#requirements), then upgrade
to a kernel version that enables cgroup v2 by default.

The kubelet automatically detects that the OS is running on cgroup v2 and
performs accordingly with no additional configuration required.

There should not be any noticeable difference in the user experience when
switching to cgroup v2, unless users are accessing the cgroup file system
directly, either on the node or from within the containers.

cgroup v2 uses a different API than cgroup v1, so if there are any
applications that directly access the cgroup file system, they need to be
updated to newer versions that support cgroup v2. For example:

- Some third-party monitoring and security agents may depend on the cgroup filesystem.
  Update these agents to versions that support cgroup v2.
- If you run [cAdvisor](https://github.com/google/cadvisor) as a stand-alone
  DaemonSet for monitoring pods and containers, update it to v0.43.0 or later.
- If you deploy Java applications, prefer to use versions which fully support cgroup v2:
  - [OpenJDK / HotSpot](https://bugs.openjdk.org/browse/JDK-8230305): jdk8u372, 11.0.16, 15 and later
  - [IBM Semeru Runtimes](https://www.ibm.com/support/pages/apar/IJ46681): 8.0.382.0, 11.0.20.0, 17.0.8.0, and later
  - [IBM Java](https://www.ibm.com/support/pages/apar/IJ46681): 8.0.8.6 and later
- If you are using the [uber-go/automaxprocs](https://github.com/uber-go/automaxprocs) package, make sure
  the version you use is v1.5.1 or higher.
- If you deploy [Node.js](https://nodejs.org/) applications, prefer to use versions that detect cgroup v2
  memory limits. Node.js reads cgroup v2 memory limits (through [libuv](https://libuv.org/))
  starting with Node.js v20.3.0. The v18 release line does not reliably detect cgroup v2 memory limits.
  Versions without this support may read the host's total memory instead of the
  limit applied to the pod, which can lead to an incorrectly sized heap and out-of-memory (OOM)
  terminations. On affected versions, set the heap size explicitly, for example with the
  `--max-old-space-size` flag.