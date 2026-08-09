---
id: kubernetes-controllers-78d52ac9
type: concept
title: Controllers
description: In robotics and automation, a *control loop* is
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/controller/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

# Controllers

In robotics and automation, a *control loop* is
a non-terminating loop that regulates the state of a system.

Here is one example of a control loop: a thermostat in a room.

When you set the temperature, that's telling the thermostat
about your *desired state*. The actual room temperature is the
*current state*. The thermostat acts to bring the current state
closer to the desired state, by turning equipment on or off.

In Kubernetes, controllers are control loops that watch the state of your
[cluster](https://kubernetes.io/docs/reference/glossary/?all=true#term-cluster "A set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node."), then make or request
changes where needed.
Each controller tries to move the current cluster state closer to the desired
state.