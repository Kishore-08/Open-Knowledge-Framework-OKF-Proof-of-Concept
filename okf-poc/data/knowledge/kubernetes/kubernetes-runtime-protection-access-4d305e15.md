---
id: kubernetes-runtime-protection-access-4d305e15
type: concept
title: 'Runtime protection: access'
description: The Kubernetes API is what makes your cluster work. Protecting this API
  is key
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Runtime protection: access

The Kubernetes API is what makes your cluster work. Protecting this API is key
to providing effective cluster security.

Other pages in the Kubernetes documentation have more detail about how to set up
specific aspects of access control. The [security checklist](https://kubernetes.io/docs/concepts/security/security-checklist/)
provides suggested basic checks for your cluster.

Beyond that, securing your cluster means implementing effective
[authentication](https://kubernetes.io/docs/concepts/security/controlling-access/#authentication) and
[authorization](https://kubernetes.io/docs/concepts/security/controlling-access/#authorization) for API access. Use [ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/) to
provide and manage security identities for workloads and cluster
components.

Kubernetes uses TLS to protect API traffic; make sure to deploy the cluster using
TLS (including for traffic between nodes and the control plane) and protect the
encryption keys. If you use Kubernetes' own API for
[CertificateSigningRequests](https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#certificate-signing-requests),
pay special attention to restricting misuse there.