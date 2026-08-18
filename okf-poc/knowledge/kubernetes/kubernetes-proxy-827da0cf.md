---
id: kubernetes-proxy-827da0cf
type: concept
title: Proxy
description: 'You can configure `kubectl` to use a proxy per cluster using `proxy-url`
  in your kubeconfig file, like this:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

## Proxy

You can configure `kubectl` to use a proxy per cluster using `proxy-url` in your kubeconfig file, like this:

```
apiVersion: v1
kind: Config

clusters:
- cluster:
    proxy-url: http://proxy.example.org:3128
    server: https://k8s.example.org/k8s/clusters/c-xxyyzz
  name: development

users:
- name: developer

contexts:
- context:
  name: development
```