---
id: kubernetes-logs-c2bd57dc
type: concept
title: Logs
description: Logs provide a chronological record of events inside applications, Kubernetes
  system components, and security-related activities such as audit logging.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/observability/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Logs

Logs provide a chronological record of events inside applications, Kubernetes system components, and security-related activities such as audit logging.

Container runtimes capture a containerized application’s output from standard output (`stdout`) and standard error (`stderr`) streams. While runtimes implement this differently, the integration with the kubelet is standardized through the *CRI logging format*, and the kubelet makes these logs available through `kubectl logs`.

*Figure 3a. Node-level logging architecture.*

System component logs capture events from the cluster and are often useful for debugging and troubleshooting. These components are classified in two different ways: those that run in a container and those that do not. For example, the `kube-scheduler` and `kube-proxy` usually run in containers, whereas the `kubelet` and the container runtime run directly on the host.

- On machines with `systemd`, the kubelet and container runtime write to journald. Otherwise, they write to `.log` files in the `/var/log` directory.
- System components that run inside containers always write to `.log` files in `/var/log`, bypassing the default container logging mechanism.

System component and container logs stored under `/var/log` require log rotation to prevent uncontrolled growth. Some cluster provisioning scripts install log rotation by default; verify your environment and adjust as needed. See the [system logs reference](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/) for details on locations, formats, and configuration options.

Most clusters run a node-level logging agent (for example, Fluent Bit or Fluentd) that tails these files and forwards entries to a central log store. The [logging architecture guidance](https://kubernetes.io/docs/concepts/cluster-administration/logging/) explains how to design such pipelines, apply retention, and log flows to backends.

Figure 3 outlines a common log aggregation pipeline.

```
flowchart LR
    subgraph Sources
        A[Application stdout / stderr]
        B[Control plane logs]
        C[Audit records]
    end
    A --> N[Node log agent]
    B --> N
    C --> N
    N --> L[Central log store]
    L --> Q[Dashboards, alerting, SIEM]
```

*Figure 3. Components of a typical Kubernetes logs pipeline.*

See [Common observability tools - logging tools](https://kubernetes.io/docs/concepts/cluster-administration/observability/#logging-tools) for logging agents and central log stores.

#### See Also

- [Logging architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/)
- [System logs](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/)
- [Logging tasks and tutorials](https://kubernetes.io/docs/tasks/debug/logging/)
- [Configure audit logging](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)