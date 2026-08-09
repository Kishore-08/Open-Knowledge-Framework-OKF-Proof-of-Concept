---
id: kubernetes-exemptions-ebd20ed7
type: concept
title: Exemptions
description: You can define *exemptions* from pod security enforcement in order to
  allow the creation of pods that
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Exemptions

You can define *exemptions* from pod security enforcement in order to allow the creation of pods that
would have otherwise been prohibited due to the policy associated with a given namespace.
Exemptions can be statically configured in the
[Admission Controller configuration](https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-admission-controller/#configure-the-admission-controller).

Exemptions must be explicitly enumerated. Requests meeting exemption criteria are *ignored* by the
Admission Controller (all `enforce`, `audit` and `warn` behaviors are skipped). Exemption dimensions include:

- **Usernames:** requests from users with an exempt authenticated (or impersonated) username are
  ignored.
- **RuntimeClassNames:** pods and [workload resources](https://kubernetes.io/docs/concepts/security/pod-security-admission/#workload-resources-and-pod-templates) specifying an exempt runtime class name are
  ignored.
- **Namespaces:** pods and [workload resources](https://kubernetes.io/docs/concepts/security/pod-security-admission/#workload-resources-and-pod-templates) in an exempt namespace are ignored.

#### Caution:

Most pods are created by a controller in response to a [workload
resource](https://kubernetes.io/docs/concepts/security/pod-security-admission/#workload-resources-and-pod-templates), meaning that exempting an end user will only
exempt them from enforcement when creating pods directly, but not when creating a workload resource.
Controller service accounts (such as `system:serviceaccount:kube-system:replicaset-controller`)
should generally not be exempted, as doing so would implicitly exempt any user that can create the
corresponding workload resource.

Updates to the following pod fields are exempt from policy checks, meaning that if a pod update
request only changes these fields, it will not be denied even if the pod is in violation of the
current policy level:

- Any metadata updates **except** changes to the seccomp or AppArmor annotations:
  - `seccomp.security.alpha.kubernetes.io/pod` (deprecated)
  - `container.seccomp.security.alpha.kubernetes.io/*` (deprecated)
  - `container.apparmor.security.beta.kubernetes.io/*` (deprecated)
- Valid updates to `.spec.activeDeadlineSeconds`
- Valid updates to `.spec.tolerations`