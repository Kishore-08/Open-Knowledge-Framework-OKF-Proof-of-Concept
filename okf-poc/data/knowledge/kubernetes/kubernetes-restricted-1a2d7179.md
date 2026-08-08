---
id: kubernetes-restricted-1a2d7179
type: concept
title: Restricted
description: '**The *Restricted* policy is aimed at enforcing current Pod hardening
  best practices, at the'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Restricted

**The *Restricted* policy is aimed at enforcing current Pod hardening best practices, at the
expense of some compatibility.** It is targeted at operators and developers of security-critical
applications, as well as lower-trust users. The following listed controls should be
enforced/disallowed:

#### Note:

In this table, wildcards (`*`) indicate all elements in a list. For example,
`spec.containers[*].securityContext` refers to the Security Context object for *all defined
containers*. If any of the listed containers fails to meet the requirements, the entire pod will
fail validation.

Restricted policy specification

|  |  |
| --- | --- |
| **Control** | **Policy** |
| *Everything from the Baseline policy* | |
| Volume Types | The Restricted policy only permits the following volume types.  **Restricted Fields**   - `spec.volumes[*]`   **Allowed Values** Every item in the `spec.volumes[*]` list must set one of the following fields to a non-null value:  - `spec.volumes[*].configMap` - `spec.volumes[*].csi` - `spec.volumes[*].downwardAPI` - `spec.volumes[*].emptyDir` - `spec.volumes[*].ephemeral` - `spec.volumes[*].persistentVolumeClaim` - `spec.volumes[*].projected` - `spec.volumes[*].secret` |
| Privilege Escalation (v1.8+) | Privilege escalation (such as via set-user-ID or set-group-ID file mode) should not be allowed. *[This is Linux only policy](https://kubernetes.io/docs/concepts/security/pod-security-standards/#os-specific-policy-controls) in v1.25+ `(spec.os.name != windows)`*  **Restricted Fields**   - `spec.containers[*].securityContext.allowPrivilegeEscalation` - `spec.initContainers[*].securityContext.allowPrivilegeEscalation` - `spec.ephemeralContainers[*].securityContext.allowPrivilegeEscalation`   **Allowed Values**   - `false` |
| Running as Non-root | Containers must be required to run as non-root users.  **Restricted Fields**   - `spec.securityContext.runAsNonRoot` - `spec.containers[*].securityContext.runAsNonRoot` - `spec.initContainers[*].securityContext.runAsNonRoot` - `spec.ephemeralContainers[*].securityContext.runAsNonRoot`   **Allowed Values**   - `true`  The container fields may be undefined/`nil` if the pod-level `spec.securityContext.runAsNonRoot` is set to `true`. |
| Running as Non-root user (v1.23+) | Containers must not set runAsUser to 0  **Restricted Fields**   - `spec.securityContext.runAsUser` - `spec.containers[*].securityContext.runAsUser` - `spec.initContainers[*].securityContext.runAsUser` - `spec.ephemeralContainers[*].securityContext.runAsUser`   **Allowed Values**   - any non-zero value - `undefined/null` |
| Seccomp (v1.19+) | Seccomp profile must be explicitly set to one of the allowed values. Both the `Unconfined` profile and the *absence* of a profile are prohibited. *[This is Linux only policy](https://kubernetes.io/docs/concepts/security/pod-security-standards/#os-specific-policy-controls) in v1.25+ `(spec.os.name != windows)`*  **Restricted Fields**   - `spec.securityContext.seccompProfile.type` - `spec.containers[*].securityContext.seccompProfile.type` - `spec.initContainers[*].securityContext.seccompProfile.type` - `spec.ephemeralContainers[*].securityContext.seccompProfile.type`   **Allowed Values**   - `RuntimeDefault` - `Localhost`  The container fields may be undefined/`nil` if the pod-level `spec.securityContext.seccompProfile.type` field is set appropriately. Conversely, the pod-level field may be undefined/`nil` if \_all\_ container- level fields are set. |
| Capabilities (v1.22+) | Containers must drop `ALL` capabilities, and are only permitted to add back the `NET_BIND_SERVICE` capability. *[This is Linux only policy](https://kubernetes.io/docs/concepts/security/pod-security-standards/#os-specific-policy-controls) in v1.25+ `(.spec.os.name != "windows")`*  **Restricted Fields**   - `spec.containers[*].securityContext.capabilities.drop` - `spec.initContainers[*].securityContext.capabilities.drop` - `spec.ephemeralContainers[*].securityContext.capabilitie