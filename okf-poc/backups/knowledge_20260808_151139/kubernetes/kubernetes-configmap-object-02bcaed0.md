---
id: kubernetes-configmap-object-02bcaed0
type: concept
title: ConfigMap object
description: A ConfigMap is an [API object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects
  "An entity in the Kubernetes system, representing part of the state of your cluster
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/configmap/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## ConfigMap object

A ConfigMap is an [API object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.")
that lets you store configuration for other objects to use. Unlike most
Kubernetes objects that have a `spec`, a ConfigMap has `data` and `binaryData`
fields. These fields accept key-value pairs as their values. Both the `data`
field and the `binaryData` are optional. The `data` field is designed to
contain UTF-8 strings while the `binaryData` field is designed to
contain binary data as base64-encoded strings.

The name of a ConfigMap must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

Each key under the `data` or the `binaryData` field must consist of
alphanumeric characters, `-`, `_` or `.`. The keys stored in `data` must not
overlap with the keys in the `binaryData` field.

Starting from v1.19, you can add an `immutable` field to a ConfigMap
definition to create an [immutable ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/#configmap-immutable).