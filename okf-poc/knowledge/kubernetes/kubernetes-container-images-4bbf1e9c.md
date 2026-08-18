---
id: kubernetes-container-images-4bbf1e9c
type: concept
title: Container images
description: A [container image](https://kubernetes.io/docs/concepts/containers/images/)
  is a ready-to-run
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Container images

A [container image](https://kubernetes.io/docs/concepts/containers/images/) is a ready-to-run
software package containing everything needed to run an application:
the code and any runtime it requires, application and system libraries,
and default values for any essential settings.

Containers are intended to be stateless and
[immutable](https://glossary.cncf.io/immutable-infrastructure/):
you should not change
the code of a container that is already running. If you have a containerized
application and want to make changes, the correct process is to build a new
image that includes the change, then recreate the container to start from the
updated image.