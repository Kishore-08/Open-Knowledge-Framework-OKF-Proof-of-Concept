---
id: kubernetes-using-configmaps-02bcaed0
type: concept
title: Using ConfigMaps
description: ConfigMaps can be mounted as data volumes. ConfigMaps can also be used
  by other
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/configmap/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Using ConfigMaps

ConfigMaps can be mounted as data volumes. ConfigMaps can also be used by other
parts of the system, without being directly exposed to the Pod. For example,
ConfigMaps can hold data that other parts of the system should use for configuration.

The most common way to use ConfigMaps is to configure settings for
containers running in a Pod in the same namespace. You can also use a
ConfigMap separately.

For example, you
might encounter [addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/ "Resources that extend the functionality of Kubernetes.")
or [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/ "A specialized controller used to manage a custom resource") that
adjust their behavior based on a ConfigMap.