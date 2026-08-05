---
id: linux-systemctl
type: concept
title: systemctl - control the systemd system and service manager
description: Manage services, units, and the systemd boot process
category: linux
tags: [linux, systemd, systemctl, services, init]
source:
  name: Linux man-pages
  url: https://www.kernel.org/doc/man-pages/
updated_at: 2026-08-05
created_at: 2026-08-05
aliases: [systemctl, systemd]
related: [linux-chmod]
---

## systemctl

`systemctl` may be used to introspect and control the state of the `systemd`
system and service manager. It manages units (services, sockets, timers, mounts,
and other objects).

## Basic Usage

```text
systemctl [OPTIONS...] COMMAND [UNIT...]
```

## Controlling Services

- `systemctl start UNIT` - start (activate) a unit.
- `systemctl stop UNIT` - stop (deactivate) a unit.
- `systemctl restart UNIT` - restart a unit.
- `systemctl reload UNIT` - ask the unit to reload its configuration.
- `systemctl status UNIT` - show runtime status of a unit.
- `systemctl enable UNIT` - make the unit start on boot.
- `systemctl disable UNIT` - remove the unit from boot-time activation.

`enable` and `disable` do not start or stop the unit; they only control whether it
is activated when the system boots.

## Querying State

- `systemctl list-units` - list loaded units.
- `systemctl list-unit-files` - list installed unit files and their enabled state.
- `systemctl is-active UNIT` - check whether a unit is active.
- `systemctl is-enabled UNIT` - check whether a unit is enabled to start at boot.

## System State

- `systemctl reboot` - shut down and reboot the system.
- `systemctl poweroff` - shut down and power off the system.
- `systemctl suspend` - suspend the system.
- `systemctl daemon-reload` - reload the manager configuration after editing
  unit files.

After editing a unit file, run `systemctl daemon-reload` before `systemctl restart`
so the changes are picked up.

## Unit States

A service can be `active` (running), `inactive` (stopped), `failed` (errored
during start), `activating`, or `deactivating`. Use `journalctl -u UNIT` to inspect
a unit's logs.
