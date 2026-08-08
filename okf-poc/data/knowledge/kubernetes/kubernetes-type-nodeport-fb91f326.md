---
id: kubernetes-type-nodeport-fb91f326
type: concept
title: '`type: NodePort`'
description: If you set the `type` field to `NodePort`, the Kubernetes control plane
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/service/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### `type: NodePort`

If you set the `type` field to `NodePort`, the Kubernetes control plane
allocates a port from a range specified by `--service-node-port-range` flag (default: 30000-32767).
Each node proxies that port (the same port number on every Node) into your Service.
Your Service reports the allocated port in its `.spec.ports[*].nodePort` field.

Using a NodePort gives you the freedom to set up your own load balancing solution,
to configure environments that are not fully supported by Kubernetes, or even
to expose one or more nodes' IP addresses directly.

For a node port Service, Kubernetes additionally allocates a port (TCP, UDP or
SCTP to match the protocol of the Service). Every node in the cluster configures
itself to listen on that assigned port and to forward traffic to one of the ready
endpoints associated with that Service. You'll be able to contact the `type: NodePort`
Service, from outside the cluster, by connecting to any node using the appropriate
protocol (for example: TCP), and the appropriate port (as assigned to that Service).

#### Choosing your own port

If you want a specific port number, you can specify a value in the `nodePort`
field. The control plane will either allocate you that port or report that
the API transaction failed.
This means that you need to take care of possible port collisions yourself.
You also have to use a valid port number, one that's inside the range configured
for NodePort use.

Here is an example manifest for a Service of `type: NodePort` that specifies
a NodePort value (30007, in this example):

```
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - port: 80
      # By default and for convenience, the `targetPort` is set to
      # the same value as the `port` field.
      targetPort: 80
      # Optional field
      # By default and for convenience, the Kubernetes control plane
      # will allocate a port from a range (default: 30000-32767)
      nodePort: 30007
```

#### Reserve Nodeport ranges to avoid collisions

The policy for assigning ports to NodePort services applies to both the auto-assignment and
the manual assignment scenarios. When a user wants to create a NodePort service that
uses a specific port, the target port may conflict with another port that has already been assigned.

To avoid this problem, the port range for NodePort services is divided into two bands.
Dynamic port assignment uses the upper band by default, and it may use the lower band once the
upper band has been exhausted. Users can then allocate from the lower band with a lower risk of port collision.

When using the default NodePort range 30000-32767, the bands are partitioned as follows:

- Static band: 30000-30085
- Dynamic band: 30086-32767

See [Avoid Collisions Assigning Ports to NodePort Services](https://kubernetes.io/blog/2023/05/11/nodeport-dynamic-and-static-allocation/)
for more details on how the static and dynamic bands are calculated.

#### Custom IP address configuration for `type: NodePort` Services

You can set up nodes in your cluster to use a particular IP address for serving node port
services. You might want to do this if each node is connected to multiple networks (for example:
one network for application traffic, and another network for traffic between nodes and the
control plane).

If you want to specify particular IP address(es) to proxy the port, you can set the
`--nodeport-addresses` flag for kube-proxy or the equivalent `nodePortAddresses`
field of the [kube-proxy configuration file](https://kubernetes.io/docs/reference/config-api/kube-proxy-config.v1alpha1/)
to particular IP block(s).

This flag takes a comma-delimited list of IP blocks (e.g. `10.0.0.0/8`, `192.0.2.0/25`)
to specify IP address ranges that kube-proxy should consider as local to this node.

For example, if you start kube-proxy with the `--nodeport-addresses=127.0.0.0/8` flag,
kube-proxy only selects the loopba