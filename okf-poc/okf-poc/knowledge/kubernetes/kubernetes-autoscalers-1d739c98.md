---
id: kubernetes-autoscalers-1d739c98
type: concept
title: Autoscalers
description: The functionalities described in previous sections are provided by Node
  *autoscalers*. In addition
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Autoscalers

The functionalities described in previous sections are provided by Node *autoscalers*. In addition
to the Kubernetes API, autoscalers also need to interact with cloud provider APIs to provision and
consolidate Nodes. This means that they need to be explicitly integrated with each supported cloud
provider. The performance and feature set of a given autoscaler can differ between cloud provider
integrations.

```
graph TD
    na[Node autoscaler]
    k8s[Kubernetes]
    cp[Cloud Provider]

    k8s --> |get Pods/Nodes|na
    na --> |drain Nodes|k8s
    na --> |create/remove resources backing Nodes|cp
    cp --> |get resources backing Nodes|na

    classDef white_on_blue fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef blue_on_white fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class na blue_on_white;
    class k8s,cp white_on_blue;
```