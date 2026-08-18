---
id: kubernetes-linux-distribution-cgroup-v2-support-d94b0a2d
type: concept
title: Linux Distribution cgroup v2 support
description: For a list of Linux distributions that use cgroup v2, refer to the [cgroup
  v2 documentation](https://github.com/opencontainers/runc/blob/main/docs/cgroup-v2.md)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/architecture/cgroups/
updated_at: '2026-08-17'
created_at: '2026-08-17'
---

### Linux Distribution cgroup v2 support

For a list of Linux distributions that use cgroup v2, refer to the [cgroup v2 documentation](https://github.com/opencontainers/runc/blob/main/docs/cgroup-v2.md)

- Container Optimized OS (since M97)
- Ubuntu (since 21.10, 22.04+ recommended)
- Debian GNU/Linux (since Debian 11 bullseye)
- Fedora (since 31)
- Arch Linux (since April 2021)
- RHEL and RHEL-like distributions (since 9)

To check if your distribution is using cgroup v2, refer to your distribution's
documentation or follow the instructions in [Identify the cgroup version on Linux nodes](https://kubernetes.io/docs/concepts/architecture/cgroups/#check-cgroup-version).

You can also enable cgroup v2 manually on your Linux distribution by modifying
the kernel cmdline boot arguments. If your distribution uses GRUB,
`systemd.unified_cgroup_hierarchy=1` should be added in `GRUB_CMDLINE_LINUX`
under `/etc/default/grub`, followed by `sudo update-grub`. However, the
recommended approach is to use a distribution that already enables cgroup v2 by
default.