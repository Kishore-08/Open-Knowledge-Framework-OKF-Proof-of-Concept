---
id: python-conversions-to-and-from-polar-coordinates-https-docs-python--307d0f07
type: concept
title: Conversions to and from polar coordinates[¶](https://docs.python.org/3/library/cmath.html#conversions-to-and-from-polar-coordinates
  "Link to this heading")
description: A Python complex number `z` is stored internally using *rectangular*
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/cmath.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Conversions to and from polar coordinates[¶](https://docs.python.org/3/library/cmath.html#conversions-to-and-from-polar-coordinates "Link to this heading")

A Python complex number `z` is stored internally using *rectangular*
or *Cartesian* coordinates. It is completely determined by its *real
part* `z.real` and its *imaginary part* `z.imag`.

*Polar coordinates* give an alternative way to represent a complex
number. In polar coordinates, a complex number *z* is defined by the
modulus *r* and the phase angle *phi*. The modulus *r* is the distance
from *z* to the origin, while the phase *phi* is the counterclockwise
angle, measured in radians, from the positive x-axis to the line
segment that joins the origin to *z*.

The following functions can be used to convert from the native
rectangular coordinates to polar coordinates and back.

cmath.phase(*z*)[¶](https://docs.python.org/3/library/cmath.html#cmath.phase "Link to this definition")
:   Return the phase of *z* (also known as the *argument* of *z*), as a float.
    `phase(z)` is equivalent to `math.atan2(z.imag, z.real)`. The result
    lies in the range [-*π*, *π*], and the branch cut for this operation lies
    along the negative real axis. The sign of the result is the same as the
    sign of `z.imag`, even when `z.imag` is zero:

    ```
    >>> phase(-1+0j)
    3.141592653589793
    >>> phase(-1-0j)
    -3.141592653589793
    ```

Note

The modulus (absolute value) of a complex number *z* can be
computed using the built-in [`abs()`](https://docs.python.org/3/library/functions.html#abs "abs") function. There is no
separate `cmath` module function for this operation.

cmath.polar(*z*)[¶](https://docs.python.org/3/library/cmath.html#cmath.polar "Link to this definition")
:   Return the representation of *z* in polar coordinates. Returns a
    pair `(r, phi)` where *r* is the modulus of *z* and *phi* is the
    phase of *z*. `polar(z)` is equivalent to `(abs(z),
    phase(z))`.

cmath.rect(*r*, *phi*)[¶](https://docs.python.org/3/library/cmath.html#cmath.rect "Link to this definition")
:   Return the complex number *z* with polar coordinates *r* and *phi*.
    Equivalent to `complex(r * math.cos(phi), r * math.sin(phi))`.