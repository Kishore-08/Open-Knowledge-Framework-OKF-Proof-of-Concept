---
id: kubernetes-kube-apiserver-10267ad8
type: concept
title: kube-apiserver
description: The API server is a component of the Kubernetes
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### kube-apiserver

The API server is a component of the Kubernetes
[control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") that exposes the Kubernetes API.
The API server is the front end for the Kubernetes control plane.

The main implementation of a Kubernetes API server is [kube-apiserver](https://kubernetes.io/docs/reference/generated/kube-apiserver/).
kube-apiserver is designed to scale horizontally—that is, it scales by deploying more instances.
You can run several instances of kube-apiserver and balance traffic between those instances.