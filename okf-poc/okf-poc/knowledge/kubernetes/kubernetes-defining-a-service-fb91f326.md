---
id: kubernetes-defining-a-service-fb91f326
type: concept
title: Defining a Service
description: A Service is an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects
  "An entity in the Kubernetes system, representing part of the state of your cluster.")
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Defining a Service

A Service is an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/#kubernetes-objects "An entity in the Kubernetes system, representing part of the state of your cluster.")
(the same way that a Pod or a ConfigMap is an object). You can create,
view or modify Service definitions using the Kubernetes API. Usually
you use a tool such as `kubectl` to make those API calls for you.

For example, suppose you have a set of Pods that each listen on TCP port 9376
and are labelled as `app.kubernetes.io/name=MyApp`. You can define a Service to
publish that TCP listener:

[`service/simple-service.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/service/simple-service.yaml)![](https://kubernetes.io/images/copycode.svg "Copy service/simple-service.yaml to clipboard")

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 9376
```

Applying this manifest creates a new Service named "my-service" with the default
ClusterIP [service type](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types). The Service
targets TCP port 9376 on any Pod with the `app.kubernetes.io/name: MyApp` label.

Kubernetes assigns this Service an IP address (the *cluster IP*),
that is used by the virtual IP address mechanism. For more details on that mechanism,
read [Virtual IPs and Service Proxies](https://kubernetes.io/docs/reference/networking/virtual-ips/).

The controller for that Service continuously scans for Pods that
match its selector, and then makes any necessary updates to the set of
EndpointSlices for the Service.

The name of a Service object must be a valid
[RFC 1123 label name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#rfc-1123-label-names).

#### Note:

A Service can map *any* incoming `port` to a `targetPort`. By default and
for convenience, the `targetPort` is set to the same value as the `port`
field.