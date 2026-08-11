---
id: linux-man-pages-concept-31f41c54
type: concept
title: '|  |  |'
description: '|  |  |'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

|  |  |
| --- | --- |
| [man7.org](https://man7.org/index.html) > Linux > [man-pages](https://man7.org/linux/man-pages/index.html) | [Linux/UNIX system programming training](http://man7.org/training/) |

---



# acl(5) — Linux manual page

|  |
| --- |
| [NAME](https://man7.org/linux/man-pages/man5/acl.5.html#NAME) | [DESCRIPTION](https://man7.org/linux/man-pages/man5/acl.5.html#DESCRIPTION) | [ACL TYPES](https://man7.org/linux/man-pages/man5/acl.5.html#ACL_TYPES) | [ACL ENTRIES](https://man7.org/linux/man-pages/man5/acl.5.html#ACL_ENTRIES) | [VALID ACLs](https://man7.org/linux/man-pages/man5/acl.5.html#VALID_ACLs) | [CORRESPONDENCE BETWEEN ACL ENTRIES AND FILE PERMISSION BITS](https://man7.org/linux/man-pages/man5/acl.5.html#CORRESPONDENCE_BETWEEN_ACL_ENTRIES_AND_FILE_PERMISSION_BITS) | [OBJECT CREATION AND DEFAULT ACLs](https://man7.org/linux/man-pages/man5/acl.5.html#OBJECT_CREATION_AND_DEFAULT_ACLs) | [ACCESS CHECK ALGORITHM](https://man7.org/linux/man-pages/man5/acl.5.html#ACCESS_CHECK_ALGORITHM) | [ACL TEXT FORMS](https://man7.org/linux/man-pages/man5/acl.5.html#ACL_TEXT_FORMS) | [RATIONALE](https://man7.org/linux/man-pages/man5/acl.5.html#RATIONALE) | [CHANGES TO THE FILE UTILITIES](https://man7.org/linux/man-pages/man5/acl.5.html#CHANGES_TO_THE_FILE_UTILITIES) | [STANDARDS](https://man7.org/linux/man-pages/man5/acl.5.html#STANDARDS) | [NOTES](https://man7.org/linux/man-pages/man5/acl.5.html#NOTES) | [SEE ALSO](https://man7.org/linux/man-pages/man5/acl.5.html#SEE_ALSO) | [AUTHOR](https://man7.org/linux/man-pages/man5/acl.5.html#AUTHOR) | [COLOPHON](https://man7.org/linux/man-pages/man5/acl.5.html#COLOPHON) |
|  |

```
ACL(5)                      File Formats Manual                    ACL(5)
```

## NAME         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       acl — Access Control Lists
```