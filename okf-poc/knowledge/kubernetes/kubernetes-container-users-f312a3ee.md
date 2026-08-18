---
id: kubernetes-container-users-f312a3ee
type: concept
title: Container users
description: '[RunAsUsername](https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/)'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/windows-security/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Container users

[RunAsUsername](https://kubernetes.io/docs/tasks/configure-pod-container/configure-runasusername/)
can be specified for Windows Pods or containers to execute the container
processes as specific user. This is roughly equivalent to
[RunAsUser](https://kubernetes.io/docs/concepts/security/pod-security-policy/#users-and-groups).

Windows containers offer two default user accounts, ContainerUser and ContainerAdministrator.
The differences between these two user accounts are covered in
[When to use ContainerAdmin and ContainerUser user accounts](https://docs.microsoft.com/virtualization/windowscontainers/manage-containers/container-security#when-to-use-containeradmin-and-containeruser-user-accounts)
within Microsoft's *Secure Windows containers* documentation.

Local users can be added to container images during the container build process.

#### Note:

- [Nano Server](https://hub.docker.com/_/microsoft-windows-nanoserver) based images run as
  `ContainerUser` by default
- [Server Core](https://hub.docker.com/_/microsoft-windows-servercore) based images run as
  `ContainerAdministrator` by default

Windows containers can also run as Active Directory identities by utilizing
[Group Managed Service Accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/)