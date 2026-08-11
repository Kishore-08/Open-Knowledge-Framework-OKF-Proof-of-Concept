---
id: linux-man-pages-see-also-top-https-man7-org-linux-man-pages-man5-acl-5-html--31f41c54
type: concept
title: SEE ALSO         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SEE ALSO         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       chmod(1), creat(2), getfacl(1), ls(1), mkdir(2), mkfifo(2),
       mknod(2), mount(8), open(2), setfacl(1), stat(2), umask(1)

   POSIX 1003.1e DRAFT 17
       https://wt.tuxomania.net/publications/posix.1e/download.html 

   POSIX 1003.1e FUNCTIONS BY CATEGORY
       ACL storage management
            acl_dup(3), acl_free(3), acl_init(3)

       ACL entry manipulation
            acl_copy_entry(3), acl_create_entry(3), acl_delete_entry(3),
            acl_get_entry(3), acl_valid(3)

            acl_add_perm(3), acl_calc_mask(3), acl_clear_perms(3),
            acl_delete_perm(3), acl_get_permset(3), acl_set_permset(3)

            acl_get_qualifier(3), acl_get_tag_type(3),
            acl_set_qualifier(3), acl_set_tag_type(3)

       ACL manipulation on an object
            acl_delete_def_file(3), acl_get_fd(3), acl_get_file(3),
            acl_set_fd(3), acl_set_file(3)

       ACL format translation
            acl_copy_entry(3), acl_copy_ext(3), acl_from_text(3),
            acl_to_text(3), acl_size(3)

   POSIX 1003.1e FUNCTIONS BY AVAILABILITY
       The first group of functions is supported on most systems with
       POSIX-like access control lists, while the second group is
       supported on fewer systems.  For applications that will be ported
       the second group is best avoided.

       acl_delete_def_file(3), acl_dup(3), acl_free(3), acl_from_text(3),
       acl_get_fd(3), acl_get_file(3), acl_init(3), acl_set_fd(3),
       acl_set_file(3), acl_to_text(3), acl_valid(3)

       acl_add_perm(3), acl_calc_mask(3), acl_clear_perms(3),
       acl_copy_entry(3), acl_copy_ext(3), acl_copy_int(3),
       acl_create_entry(3), acl_delete_entry(3), acl_delete_perm(3),
       acl_get_entry(3), acl_get_permset(3), acl_get_qualifier(3),
       acl_get_tag_type(3), acl_set_permset(3), acl_set_qualifier(3),
       acl_set_tag_type(3), acl_size(3)

   LINUX EXTENSIONS
       These non-portable extensions are available on Linux systems.

       acl_check(3), acl_cmp(3), acl_entries(3), acl_equiv_mode(3),
       acl_error(3), acl_extended_fd(3), acl_extended_file(3),
       acl_extended_file_nofollow(3), acl_from_mode(3), acl_get_perm(3),
       acl_to_any_text(3)
```

## AUTHOR         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       Andreas Gruenbacher, <andreas.gruenbacher@gmail.com>
```