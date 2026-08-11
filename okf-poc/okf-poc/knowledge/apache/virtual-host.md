---
id: apache-virtual-host
type: concept
title: Apache Virtual Host
description: Run multiple websites on a single Apache HTTP Server instance
category: apache
tags: [apache, virtual-host, name-based, ip-based, httpd]
source:
  name: Apache HTTP Server Documentation
  url: https://httpd.apache.org/docs/current/vhosts/
updated_at: 2026-08-05
created_at: 2026-08-05
aliases: [VirtualHost, Virtual Host, vhost]
related: [apache-directives]
---

## Virtual Host

The Apache HTTP Server's virtual hosting capability lets you run more than one
website (such as `www.example.com` and `www.example.org`) on a single machine. The
different sites can share one IP address or use different IPs.

## Types of Virtual Hosting

- **Name-based virtual hosting**: many hostnames on one IP address. This is the
  most common method; the server uses the `Host` header to select the correct
  `VirtualHost` block.
- **IP-based virtual hosting**: a different IP address for each website.
- **Port-based virtual hosting**: different sites on different ports of the same
  machine (for example behind a proxy or firewall).

## Name-based Virtual Host Example

```apache
<VirtualHost *:80>
    ServerName www.example.com
    ServerAlias example.com
    DocumentRoot /var/www/example.com
    ErrorLog logs/example.com-error_log
    CustomLog logs/example.com-access_log common
</VirtualHost>
```

Requests for `www.example.com` are served from `/var/www/example.com`.

## Multiple Hosts on One IP

The server first matches the IP address and port, then the best match based on
`ServerName` / `ServerAlias`. If no host matches, the first virtual host on that
address and port becomes the default and serves all unmatched requests.

## Virtual Host Directives

- `ServerName`: the hostname the virtual host responds to.
- `ServerAlias`: alternate names for the same virtual host.
- `DocumentRoot`: directory from which static files are served.
- `ErrorLog` / `CustomLog`: per-host logging.
- `ProxyPass` / `ProxyPassReverse`: reverse-proxy to a backend application.

## Default Virtual Host

For a given address/port, the first `VirtualHost` block in the configuration is the
default and receives requests whose `Host` matches no virtual host. A
`<VirtualHost _default_:*>` block can be used to make this explicit.

## Logging

Each virtual host can have its own error and access logs via `ErrorLog` and
`CustomLog`, which is essential when hosting unrelated sites on one server.
