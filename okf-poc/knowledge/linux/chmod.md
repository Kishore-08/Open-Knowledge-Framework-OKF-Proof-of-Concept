---
id: linux-chmod
type: concept
title: chmod - change file mode bits
description: Change the permission bits of files and directories
category: linux
tags: [linux, permissions, file-mode, chmod, cli]
source:
  name: Linux man-pages
  url: https://www.kernel.org/doc/man-pages/
updated_at: 2026-08-05
created_at: 2026-08-05
aliases: [chmod, file permissions]
related: [linux-systemctl]
---

## chmod

`chmod` changes the file mode bits (permissions) of each given file according to
`mode`, which can be either a symbolic representation of changes to make, or an
octal number representing the bit pattern for the new mode bits.

## Usage

```text
chmod [OPTION]... MODE[,MODE]... FILE...
chmod [OPTION]... OCTAL-MODE FILE...
```

## Symbolic Mode

The symbolic mode is of the form `[ugoa...][[+-=][perms...]...]`.

- Who (`u` user, `g` group, `o` others, `a` all).
- Operator (`+` add, `-` remove, `=` set exactly).
- Permissions (`r` read, `w` write, `x` execute).

Examples:

- `chmod u+x script.sh` - add execute permission for the owner.
- `chmod g-w file.txt` - remove write permission for the group.
- `chmod a+r file.txt` - make the file readable by everyone.

## Octal Mode

Permissions are encoded as a three- or four-digit octal number. Each digit is the
sum of `4` (read), `2` (write), `1` (execute).

- `chmod 755 file` - owner rwx, group r-x, others r-x.
- `chmod 644 file` - owner rw-, group r--, others r--.
- `chmod 600 secret.key` - owner rw- only.

The leading digit (when present) sets special bits: `4` setuid, `2` setgid,
`1` sticky.

## Common Options

- `-R` (`--recursive`): change files and directories recursively.
- `-v` (`--verbose`): output a diagnostic for every file processed.
- `--reference=RFILE`: use RFILE's mode instead of MODE values.

## Notes

- Directories need execute permission for traversal; read permission lists entries.
- Only the file owner or a privileged user may change a file's mode.
- On some systems the ability to change the mode is further restricted by
  `fs.protected_regular` / mount options.
