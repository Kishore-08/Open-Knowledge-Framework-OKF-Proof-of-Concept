---
id: linux-man-pages-acl-text-forms-top-https-man7-org-linux-man-pages-man5-acl-5-31f41c54
type: concept
title: ACL TEXT FORMS         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ACL TEXT FORMS         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       A long and a short text form for representing ACLs is defined. In
       both forms, ACL entries are represented as three colon separated
       fields: an ACL entry tag type, an ACL entry qualifier, and the
       discretionary access permissions. The first field contains one of
       the following entry tag type keywords:

             user    A user ACL entry specifies the access granted to
                     either the file owner (entry tag type ACL_USER_OBJ)
                     or a specified user (entry tag type ACL_USER).

             group   A group ACL entry specifies the access granted to
                     either the file group (entry tag type ACL_GROUP_OBJ)
                     or a specified group (entry tag type ACL_GROUP).

             mask    A mask ACL entry specifies the maximum access which
                     can be granted by any ACL entry except the user
                     entry for the file owner and the other entry (entry
                     tag type ACL_MASK).

             other   An other ACL entry specifies the access granted to
                     any process that does not match any user or group
                     ACL entries (entry tag type ACL_OTHER).

       The second field contains the user or group identifier of the user
       or group associated with the ACL entry for entries of entry tag
       type ACL_USER or ACL_GROUP, and is empty for all other entries. A
       user identifier can be a user name or a user ID number in decimal
       form. A group identifier can be a group name or a group ID number
       in decimal form.

       The third field contains the discretionary access permissions. The
       read, write and search/execute permissions are represented by the
       r, w, and x characters, in this order. Each of these characters is
       replaced by the - character to denote that a permission is absent
       in the ACL entry.  When converting from the text form to the
       internal representation, permissions that are absent need not be
       specified.

       White space is permitted at the beginning and end of each ACL
       entry, and immediately before and after a field separator (the
       colon character).

   LONG TEXT FORM
       The long text form contains one ACL entry per line. In addition, a
       number sign (#) may start a comment that extends until the end of
       the line. If an ACL_USER, ACL_GROUP_OBJ or ACL_GROUP ACL entry
       contains permissions that are not also contained in the ACL_MASK
       entry, the entry is followed by a number sign, the string
       “effective:”, and the effective access permissions defined by that
       entry. This is an example of the long text form:

             user::rw-
             user:lisa:rw-         #effective:r--
             group::r--
             group:toolies:rw-     #effective:r--
             mask::r--
             other::r--

   SHORT TEXT FORM
       The short text form is a sequence of ACL entries separated by
       commas, and is used for input. Comments are not supported. Entry
       tag type keywords may either appear in their full unabbreviated
       form, or in their single letter abbreviated form. The abbreviation
       for user is u, the abbreviation for group is g, the abbreviation
       for mask is m, and the abbreviation for other is o.  The
       permissions may contain at most one each of the following
       characters in any order: r, w, x.  These are examples of the short
       text form:

             u::rw-,u:lisa:rw-,g::r--,g:toolies:rw-,m::r--,o::r--
             g:toolies:rw,u:lisa:rw,u::wr,g::r,o::r,m::r
```