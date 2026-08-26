---
id: python-interpolation-of-values-https-docs-python-org-3-library-conf-caa28eb2
type: concept
title: Interpolation of values[¶](https://docs.python.org/3/library/configparser.html#interpolation-of-values
  "Link to this heading")
description: On top of the core functionality, [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser
  "configparser.ConfigParser") supports
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Interpolation of values[¶](https://docs.python.org/3/library/configparser.html#interpolation-of-values "Link to this heading")

On top of the core functionality, [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") supports
interpolation. This means values can be preprocessed before returning them
from `get()` calls.

*class* configparser.BasicInterpolation[¶](https://docs.python.org/3/library/configparser.html#configparser.BasicInterpolation "Link to this definition")
:   The default implementation used by [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser"). It enables
    values to contain format strings which refer to other values in the same
    section, or values in the special default section [[1]](https://docs.python.org/3/library/configparser.html#id16). Additional default
    values can be provided on initialization.

    For example:

    ```
    [Paths]
    home_dir: /Users
    my_dir: %(home_dir)s/lumberjack
    my_pictures: %(my_dir)s/Pictures

    [Escape]
    # use a %% to escape the % sign (% is the only character that needs to be escaped):
    gain: 80%%
    ```

    In the example above, [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") with *interpolation* set to
    `BasicInterpolation()` would resolve `%(home_dir)s` to the value of
    `home_dir` (`/Users` in this case). `%(my_dir)s` in effect would
    resolve to `/Users/lumberjack`. All interpolations are done on demand so
    keys used in the chain of references do not have to be specified in any
    specific order in the configuration file.

    With `interpolation` set to `None`, the parser would simply return
    `%(my_dir)s/Pictures` as the value of `my_pictures` and
    `%(home_dir)s/lumberjack` as the value of `my_dir`.

*class* configparser.ExtendedInterpolation[¶](https://docs.python.org/3/library/configparser.html#configparser.ExtendedInterpolation "Link to this definition")
:   An alternative handler for interpolation which implements a more advanced
    syntax, used for instance in `zc.buildout`. Extended interpolation is
    using `${section:option}` to denote a value from a foreign section.
    Interpolation can span multiple levels. For convenience, if the
    `section:` part is omitted, interpolation defaults to the current section
    (and possibly the default values from the special section).

    For example, the configuration specified above with basic interpolation,
    would look like this with extended interpolation:

    ```
    [Paths]
    home_dir: /Users
    my_dir: ${home_dir}/lumberjack
    my_pictures: ${my_dir}/Pictures

    [Escape]
    # use a $$ to escape the $ sign ($ is the only character that needs to be escaped):
    cost: $$80
    ```

    Values from other sections can be fetched as well:

    ```
    [Common]
    home_dir: /Users
    library_dir: /Library
    system_dir: /System
    macports_dir: /opt/local

    [Frameworks]
    Python: 3.2
    path: ${Common:system_dir}/Library/Frameworks/

    [Arthur]
    nickname: Two Sheds
    last_name: Jackson
    my_dir: ${Common:home_dir}/twosheds
    my_pictures: ${my_dir}/Pictures
    python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}
    ```