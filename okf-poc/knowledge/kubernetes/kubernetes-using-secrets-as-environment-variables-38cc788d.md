---
id: kubernetes-using-secrets-as-environment-variables-38cc788d
type: concept
title: Using Secrets as environment variables
description: To use a Secret in an [environment variable](https://kubernetes.io/docs/concepts/containers/container-environment/
  "Container environment variables are name=value pairs that provide useful information
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/secret/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Using Secrets as environment variables

To use a Secret in an [environment variable](https://kubernetes.io/docs/concepts/containers/container-environment/ "Container environment variables are name=value pairs that provide useful information into containers running in a Pod.")
in a Pod:

1. For each container in your Pod specification, add an environment variable
   for each Secret key that you want to use to the
   `env[].valueFrom.secretKeyRef` field.
2. Modify your image and/or command line so that the program looks for values
   in the specified environment variables.

For instructions, refer to
[Define container environment variables using Secret data](https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#define-container-environment-variables-using-secret-data).

It's important to note that the range of characters allowed for environment variable
names in pods is [restricted](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#using-environment-variables-inside-of-your-config).
If any keys do not meet the rules, those keys are not made available to your container, though
the Pod is allowed to start.