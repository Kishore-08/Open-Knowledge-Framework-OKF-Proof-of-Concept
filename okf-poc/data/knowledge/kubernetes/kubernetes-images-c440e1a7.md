---
id: kubernetes-images-c440e1a7
type: concept
title: Images
description: A container image represents binary data that encapsulates an application
  and all its
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Images

A container image represents binary data that encapsulates an application and all its
software dependencies. Container images are executable software bundles that can run
standalone and that make very well-defined assumptions about their runtime environment.

You typically create a container image of your application and push it to a registry
before referring to it in a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.").

This page provides an outline of the container image concept.

#### Note:

If you are looking for the container images for a Kubernetes
release (such as v1.36, the latest minor release),
visit [Download Kubernetes](https://kubernetes.io/releases/download/).