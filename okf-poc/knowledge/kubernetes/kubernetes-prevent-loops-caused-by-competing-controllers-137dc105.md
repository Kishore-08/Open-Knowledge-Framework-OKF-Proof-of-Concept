---
id: kubernetes-prevent-loops-caused-by-competing-controllers-137dc105
type: concept
title: Prevent loops caused by competing controllers
description: Consider any other components that run in your cluster that might conflict
  with
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/admission-webhooks-good-practices/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Prevent loops caused by competing controllers

Consider any other components that run in your cluster that might conflict with
the mutations that your webhook makes. For example, if your webhook adds a label
that a different controller removes, your webhook gets called again. This leads
to a loop.

To detect these loops, try the following:

1. Update your cluster audit policy to log audit events. Use the following
   parameters:

   - `level`: `RequestResponse`
   - `verbs`: `["patch"]`
   - `omitStages`: `RequestReceived`

   Set the audit rule to create events for the specific resources that your
   webhook mutates.
2. Check your audit events for webhooks being reinvoked multiple times with the
   same patch being applied to the same object, or for an object having
   a field updated and reverted multiple times.