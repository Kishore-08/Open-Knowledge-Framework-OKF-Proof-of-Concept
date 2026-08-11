---
id: kubernetes-motivation-d41317cc
type: concept
title: Motivation
description: The *operator pattern* aims to capture the key aim of a human operator
  who
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Motivation

The *operator pattern* aims to capture the key aim of a human operator who
is managing a service or set of services. Human operators who look after
specific applications and services have deep knowledge of how the system
ought to behave, how to deploy it, and how to react if there are problems.

People who run workloads on Kubernetes often like to use automation to take
care of repeatable tasks. The operator pattern captures how you can write
code to automate a task beyond what Kubernetes itself provides.