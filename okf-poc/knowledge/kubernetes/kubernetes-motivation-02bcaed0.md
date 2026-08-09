---
id: kubernetes-motivation-02bcaed0
type: concept
title: Motivation
description: Use a ConfigMap for setting configuration data separately from application
  code.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/configmap/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Motivation

Use a ConfigMap for setting configuration data separately from application code.

For example, imagine that you are developing an application that you can run on your
own computer (for development) and in the cloud (to handle real traffic).
You write the code to look in an environment variable named `DATABASE_HOST`.
Locally, you set that variable to `localhost`. In the cloud, you set it to
refer to a Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.")
that exposes the database component to your cluster.
This lets you fetch a container image running in the cloud and
debug the exact same code locally if needed.

#### Note:

A ConfigMap is not designed to hold large chunks of data. The data stored in a
ConfigMap cannot exceed 1 MiB. If you need to store settings that are
larger than this limit, you may want to consider mounting a volume or use a
separate database or file service.