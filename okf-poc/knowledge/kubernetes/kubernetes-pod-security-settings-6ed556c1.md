---
id: kubernetes-pod-security-settings-6ed556c1
type: concept
title: Pod security settings
description: To set security constraints on Pods and containers, you use the
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Pod security settings

To set security constraints on Pods and containers, you use the
`securityContext` field in the Pod specification. This field gives you
granular control over what a Pod or individual containers can do. See [Advanced Pod Configuration](https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/) for more details.

For basic security configuration, you should meet the Baseline Pod security standard and run containers as non-root. You can set simple security contexts:

```
apiVersion: v1
kind: Pod
metadata:
  name: security-context-demo
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
  containers:
  - name: sec-ctx-demo
    image: busybox
    command: ["sh", "-c", "sleep 1h"]
```

For advanced security context configuration including capabilities, seccomp profiles, and detailed security options, see the [security concepts](https://kubernetes.io/docs/concepts/security/) section.

- To learn about kernel-level security constraints that you can use,
  see [Linux kernel security constraints for Pods and containers](https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/).
- To learn more about the Pod security context, see
  [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).