---
id: kubernetes-troubleshooting-guide
type: concept
title: Kubernetes Troubleshooting Guide
description: This document provides troubleshooting steps for common Kubernetes issues
  such as pods stuck in Pending state, ImagePullBackOff errors, CrashLoopBackOff errors,
  and unreachable services. Each entry details the symptom, probable cause, diagnosis
  command, and practical solution.
category: kubernetes
tags:
- Kubernetes
- Troubleshooting
- Pod Management
- Container Networking
source:
  name: Ingested document
  url: ''
created_at: '2026-08-08'
updated_at: '2026-08-08'
aliases: []
related: []
document_type: Kubernetes
trust_level: Medium
source_file: kubernetes-troubleshooting.json
---

[
  {
    "title": "Pod stuck in Pending state",
    "category": "kubernetes",
    "symptom": "A Pod remains in the Pending phase and never starts.",
    "probable_cause": "The scheduler cannot find a node with enough CPU or memory, or no node matches the nodeSelector and affinity rules.",
    "diagnosis": "Run kubectl describe pod <pod-name> and inspect the Events section for FailedScheduling messages.",
    "solution": "Check node capacity with kubectl top nodes, remove resource requests that exceed node capacity, or fix nodeSelector and taints. Pending can also mean persistent volume claims are unsatisfied."
  },
  {
    "title": "ImagePullBackOff error",
    "category": "kubernetes",
    "symptom": "A container never starts and shows ImagePullBackOff.",
    "probable_cause": "The image name is wrong, the registry requires credentials, or the image does not exist.",
    "diagnosis": "Run kubectl describe pod and look for the pull error message in Events.",
    "solution": "Fix the image tag, add an imagePullSecret for private registries, or verify registry network access from the node."
  },
  {
    "title": "CrashLoopBackOff error",
    "category": "kubernetes",
    "symptom": "A container starts and immediately crashes, restarting repeatedly.",
    "probable_cause": "The application exits with a non-zero code because of a missing config, environment variable, or misconfigured startup command.",
    "diagnosis": "Run kubectl logs <pod-name> --previous to inspect the logs of the crashed container.",
    "solution": "Fix the application error, provide the required environment variables and config maps, and check liveness and readiness probe settings that may be too strict."
  },
  {
    "title": "Service not reachable",
    "category": "kubernetes",
    "symptom": "An application inside the cluster cannot reach a Service, or the Service endpoint is empty.",
    "probable_cause": "The Service selector does not match the Pod labels, or the target port is wrong.",
    "diagnosis": "Run kubectl get endpoints <service-name> to check whether endpoints exist.",
    "solution": "Align the Service selector with the Pod labels, verify the targetPort matches the container port, and confirm the Pods are Running and Ready."
  }
]
