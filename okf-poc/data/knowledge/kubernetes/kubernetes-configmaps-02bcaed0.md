---
id: kubernetes-configmaps-02bcaed0
type: concept
title: ConfigMaps
description: A ConfigMap is an API object used to store non-confidential data in key-value
  pairs.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/configmap/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# ConfigMaps

A ConfigMap is an API object used to store non-confidential data in key-value pairs.
[Pods](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster.") can consume ConfigMaps as
environment variables, command-line arguments, or as configuration files in a
[volume](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod.").

A ConfigMap allows you to decouple environment-specific configuration from your [container images](https://kubernetes.io/docs/reference/glossary/?all=true#term-image "Stored instance of a container that holds a set of software needed to run an application."), so that your applications are easily portable.

#### Caution:

ConfigMap does not provide secrecy or encryption.
If the data you want to store are confidential, use a
[Secret](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.") rather than a ConfigMap,
or use additional (third party) tools to keep your data private.