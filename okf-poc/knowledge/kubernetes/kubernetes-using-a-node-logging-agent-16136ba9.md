---
id: kubernetes-using-a-node-logging-agent-16136ba9
type: concept
title: Using a node logging agent
description: You can implement cluster-level logging by including a *node-level logging
  agent* on each node.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/logging/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Using a node logging agent

You can implement cluster-level logging by including a *node-level logging agent* on each node.
The logging agent is a dedicated tool that exposes logs or pushes logs to a backend.
Commonly, the logging agent is a container that has access to a directory with log files from all of the
application containers on that node.

Because the logging agent must run on every node, it is recommended to run the agent
as a `DaemonSet`.

Node-level logging creates only one agent per node and doesn't require any changes to the
applications running on the node.

Containers write to stdout and stderr, but with no agreed format. A node-level agent collects
these logs and forwards them for aggregation.