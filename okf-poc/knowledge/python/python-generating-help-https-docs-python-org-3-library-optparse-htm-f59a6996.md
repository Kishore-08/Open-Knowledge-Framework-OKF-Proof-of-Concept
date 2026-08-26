---
id: python-generating-help-https-docs-python-org-3-library-optparse-htm-f59a6996
type: concept
title: Generating help[¶](https://docs.python.org/3/library/optparse.html#generating-help
  "Link to this heading")
description: '`optparse`’s ability to generate help and usage text automatically is'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Generating help[¶](https://docs.python.org/3/library/optparse.html#generating-help "Link to this heading")

`optparse`’s ability to generate help and usage text automatically is
useful for creating user-friendly command-line interfaces. All you have to do
is supply a [`help`](https://docs.python.org/3/library/optparse.html#optparse.Option.help "optparse.Option.help") value for each option, and optionally a short
usage message for your whole program. Here’s an OptionParser populated with
user-friendly (documented) options:

```
usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser(usage=usage)
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=True,
                  help="make lots of noise [default]")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose",
                  help="be vewwy quiet (I'm hunting wabbits)")
parser.add_option("-f", "--filename",
                  metavar="FILE", help="write output to FILE")
parser.add_option("-m", "--mode",
                  default="intermediate",
                  help="interaction mode: novice, intermediate, "
                       "or expert [default: %default]")
```

If `optparse` encounters either `-h` or `--help` on the
command-line, or if you just call `parser.print_help()`, it prints the
following to standard output:

```
Usage: <yourscript> [options] arg1 arg2

Options:
  -h, --help            show this help message and exit
  -v, --verbose         make lots of noise [default]
  -q, --quiet           be vewwy quiet (I'm hunting wabbits)
  -f FILE, --filename=FILE
                        write output to FILE
  -m MODE, --mode=MODE  interaction mode: novice, intermediate, or
                        expert [default: intermediate]
```

(If the help output is triggered by a help option, `optparse` exits after
printing the help text.)

There’s a lot going on here to help `optparse` generate the best possible
help message:

- the script defines its own usage message:

  ```
  usage = "usage: %prog [options] arg1 arg2"
  ```

  `optparse` expands `%prog` in the usage string to the name of the
  current program, i.e. `os.path.basename(sys.argv[0])`. The expanded string
  is then printed before the detailed option help.

  If you don’t supply a usage string, `optparse` uses a bland but sensible
  default: `"Usage: %prog [options]"`, which is fine if your script doesn’t
  take any positional arguments.
- every option defines a help string, and doesn’t worry about
  line-wrapping—`optparse` takes care of wrapping lines and making
  the help output look good.
- options that take a value indicate this fact in their automatically generated
  help message, e.g. for the “mode” option:

  ```
  -m MODE, --mode=MODE
  ```

  Here, “MODE” is called the meta-variable: it stands for the argument that the
  user is expected to supply to `-m`/`--mode`. By default,
  `optparse` converts the destination variable name to uppercase and uses
  that for the meta-variable. Sometimes, that’s not what you want—for
  example, the `--filename` option explicitly sets `metavar="FILE"`,
  resulting in this automatically generated option description:

  ```
  -f FILE, --filename=FILE
  ```

  This is important for more than just saving space, though: the manually
  written help text uses the meta-variable `FILE` to clue the user in that
  there’s a connection between the semi-formal syntax `-f FILE` and the informal
  semantic description “write output to FILE”. This is a simple but effective
  way to make your help text a lot clearer and more useful for end users.
- options that have a default value can include `%default` in the help
  string—`optparse` will replace it with [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") of the option’s
  default value. If an option has no default value (or the default value is
  `None`), `%default` expands to `none`.

#### Grouping Options[¶](https://docs.p