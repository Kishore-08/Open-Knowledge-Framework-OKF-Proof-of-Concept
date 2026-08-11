---
id: kubernetes-baseline-1a2d7179
type: concept
title: Baseline
description: '**The *Baseline* policy is aimed at ease of adoption for common containerized
  workloads while'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Baseline

**The *Baseline* policy is aimed at ease of adoption for common containerized workloads while
preventing known privilege escalations.** This policy is targeted at application operators and
developers of non-critical applications. The following listed controls should be
enforced/disallowed:

#### Note:

In this table, wildcards (`*`) indicate all elements in a list. For example,
`spec.containers[*].securityContext` refers to the Security Context object for *all defined
containers*. If any of the listed containers fails to meet the requirements, the entire pod will
fail validation.

Baseline policy specification

| Control | Policy |
| --- | --- |
| HostProcess | Windows Pods offer the ability to run [HostProcess containers](https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod) which enables privileged access to the Windows host machine. Privileged access to the host is disallowed in the Baseline policy.  FEATURE STATE: `Kubernetes v1.26 [stable]`  **Restricted Fields**   - `spec.securityContext.windowsOptions.hostProcess` - `spec.containers[*].securityContext.windowsOptions.hostProcess` - `spec.initContainers[*].securityContext.windowsOptions.hostProcess` - `spec.ephemeralContainers[*].securityContext.windowsOptions.hostProcess`   **Allowed Values**   - Undefined/nil - `false` |
| Host Namespaces | Sharing the host namespaces must be disallowed.  **Restricted Fields**   - `spec.hostNetwork` - `spec.hostPID` - `spec.hostIPC`   **Allowed Values**   - Undefined/nil - `false` |
| Privileged Containers | Privileged Pods disable most security mechanisms and must be disallowed.  **Restricted Fields**   - `spec.containers[*].securityContext.privileged` - `spec.initContainers[*].securityContext.privileged` - `spec.ephemeralContainers[*].securityContext.privileged`   **Allowed Values**   - Undefined/nil - `false` |
| Capabilities | Adding additional capabilities beyond those listed below must be disallowed.  **Restricted Fields**   - `spec.containers[*].securityContext.capabilities.add` - `spec.initContainers[*].securityContext.capabilities.add` - `spec.ephemeralContainers[*].securityContext.capabilities.add`   **Allowed Values**   - Undefined/nil - `AUDIT_WRITE` - `CHOWN` - `DAC_OVERRIDE` - `FOWNER` - `FSETID` - `KILL` - `MKNOD` - `NET_BIND_SERVICE` - `SETFCAP` - `SETGID` - `SETPCAP` - `SETUID` - `SYS_CHROOT` |
| HostPath Volumes | HostPath volumes must be forbidden.  **Restricted Fields**   - `spec.volumes[*].hostPath`   **Allowed Values**   - Undefined/nil |
| Host Ports | HostPorts should be disallowed entirely (recommended) or restricted to a known list  **Restricted Fields**   - `spec.containers[*].ports[*].hostPort` - `spec.initContainers[*].ports[*].hostPort` - `spec.ephemeralContainers[*].ports[*].hostPort`   **Allowed Values**   - Undefined/nil - Known list (not supported by the built-in [Pod Security Admission controller](https://kubernetes.io/docs/concepts/security/pod-security-admission/)) - `0` |
| Host Probes / Lifecycle Hooks (v1.34+) | The Host field in probes and lifecycle hooks must be disallowed.  **Restricted Fields**   - `spec.containers[*].livenessProbe.httpGet.host` - `spec.containers[*].readinessProbe.httpGet.host` - `spec.containers[*].startupProbe.httpGet.host` - `spec.containers[*].livenessProbe.tcpSocket.host` - `spec.containers[*].readinessProbe.tcpSocket.host` - `spec.containers[*].startupProbe.tcpSocket.host` - `spec.containers[*].lifecycle.postStart.tcpSocket.host` - `spec.containers[*].lifecycle.preStop.tcpSocket.host` - `spec.containers[*].lifecycle.postStart.httpGet.host` - `spec.containers[*].lifecycle.preStop.httpGet.host` - `spec.initContainers[*].livenessProbe.httpGet.host` - `spec.initContainers[*].readinessProbe.httpGet.host` - `spec.initContainers[*].startupProbe.httpGet.host` - `spec.initContainers[*].livenessProbe.tcpSocket.host` - `spec.initContainers[*].readinessProbe.tcpSocket.host` - `spec.initContainers[*].startupProbe.tcpSocket.host` - `spec.initC