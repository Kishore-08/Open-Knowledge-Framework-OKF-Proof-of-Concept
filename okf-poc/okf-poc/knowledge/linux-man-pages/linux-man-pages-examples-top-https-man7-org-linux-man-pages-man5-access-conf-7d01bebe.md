---
id: linux-man-pages-examples-top-https-man7-org-linux-man-pages-man5-access-conf-7d01bebe
type: concept
title: EXAMPLES         [top](https://man7.org/linux/man-pages/man5/access.conf.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/access.conf.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## EXAMPLES         [top](https://man7.org/linux/man-pages/man5/access.conf.5.html#top_of_page)

```
       These are some example lines which might be specified in
       /etc/security/access.conf.

       User root should be allowed to get access via cron, X11 terminal
       :0, tty1, ..., tty5, tty6.

       +:root:crond :0 tty1 tty2 tty3 tty4 tty5 tty6

       User root should be allowed to get access from hosts which own the
       IPv4 addresses. This does not mean that the connection have to be
       a IPv4 one, a IPv6 connection from a host with one of this IPv4
       addresses does work, too.

       +:root:192.168.200.1 192.168.200.4 192.168.200.9

       +:root:127.0.0.1

       User root should get access from network 192.168.201.  where the
       term will be evaluated by string matching. But it might be better
       to use network/netmask instead. The same meaning of 192.168.201.
       is 192.168.201.0/24 or 192.168.201.0/255.255.255.0.

       +:root:192.168.201.

       User root should be able to have access from hosts foo1.bar.org
       and foo2.bar.org (uses string matching also).

       +:root:foo1.bar.org foo2.bar.org

       User root should be able to have access from domain foo.bar.org
       (uses string matching also).

       +:root:.foo.bar.org

       User root should be denied to get access from all other sources.

       -:root:ALL

       A user with uid 1003 and a group with gid 1000 should be allowed
       to get access from all other sources.

       +:(1000) 1003:ALL

       User foo and members of netgroup admins should be allowed to get
       access from all sources. This will only work if netgroup service
       is available.

       +:@admins foo:ALL

       User john and foo should get access from IPv6 host address.

       +:john foo:2001:db8:0:101::1

       User john and foo should get access from IPv6 link local host
       address.

       +:john foo:fe80::de95:818c:1b55:7e42%eth1

       User john should get access from IPv6 net/mask.

       +:john:2001:db8:0:101::/64

       Members of group wheel should be allowed to get access from all
       sources.

       +:(wheel):ALL

       Disallow console logins to all but the shutdown, sync and all
       other accounts, which are a member of the wheel group.

       -:ALL EXCEPT (wheel) shutdown sync:LOCAL

       All other users should be denied to get access from all sources.

       -:ALL:ALL
```