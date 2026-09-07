---
id: kubernetes-cri-configuration-3540e4aa
type: concept
title: CRI Configuration
description: For more details on setting up CRI runtimes, see [CRI installation](https://kubernetes.io/docs/setup/production-environment/container-runtimes/).
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/runtime-class/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### CRI Configuration

For more details on setting up CRI runtimes, see [CRI installation](https://kubernetes.io/docs/setup/production-environment/container-runtimes/).

#### [containerd](https://containerd.io/docs/ "A container runtime with an emphasis on simplicity, robustness and portability")

Runtime handlers are configured through containerd's configuration at
`/etc/containerd/config.toml`. Valid handlers are configured under the runtimes section:

```
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.${HANDLER_NAME}]
```

See containerd's [config documentation](https://github.com/containerd/containerd/blob/main/docs/cri/config.md)
for more details:

#### [CRI-O](https://cri-o.io/#what-is-cri-o "A lightweight container runtime specifically for Kubernetes")

Runtime handlers are configured through CRI-O's configuration at `/etc/crio/crio.conf`. Valid
handlers are configured under the
[crio.runtime table](https://github.com/cri-o/cri-o/blob/master/docs/crio.conf.5.md#crioruntime-table):

```
[crio.runtime.runtimes.${HANDLER_NAME}]
  runtime_path = "${PATH_TO_BINARY}"
```

See CRI-O's [config documentation](https://github.com/cri-o/cri-o/blob/master/docs/crio.conf.5.md) for more details.