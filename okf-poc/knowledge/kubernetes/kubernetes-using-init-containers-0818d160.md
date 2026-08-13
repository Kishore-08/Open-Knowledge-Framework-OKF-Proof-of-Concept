---
id: kubernetes-using-init-containers-0818d160
type: concept
title: Using init containers
description: Because init containers have separate images from app containers, they
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Using init containers

Because init containers have separate images from app containers, they
have some advantages for start-up related code:

- Init containers can contain utilities or custom code for setup that are not present in an app
  image. For example, there is no need to make an image `FROM` another image just to use a tool like
  `sed`, `awk`, `python`, or `dig` during setup.
- The application image builder and deployer roles can work independently without
  the need to jointly build a single app image.
- Init containers can run with a different view of the filesystem than app containers in the
  same Pod. Consequently, they can be given access to
  [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.") that app containers cannot access.
- Because init containers run to completion before any app containers start, init containers offer
  a mechanism to block or delay app container startup until a set of preconditions are met. Once
  preconditions are met, all of the app containers in a Pod can start in parallel.
- Init containers can securely run utilities or custom code that would otherwise make an app
  container image less secure. By keeping unnecessary tools separate you can limit the attack
  surface of your app container image.