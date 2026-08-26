---
id: python-constants-https-docs-python-org-3-library-cmath-html-constan-307d0f07
type: concept
title: Constants[¶](https://docs.python.org/3/library/cmath.html#constants "Link to
  this heading")
description: cmath.pi[¶](https://docs.python.org/3/library/cmath.html#cmath.pi "Link
  to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/cmath.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Constants[¶](https://docs.python.org/3/library/cmath.html#constants "Link to this heading")

cmath.pi[¶](https://docs.python.org/3/library/cmath.html#cmath.pi "Link to this definition")
:   The mathematical constant *π*, as a float.

cmath.e[¶](https://docs.python.org/3/library/cmath.html#cmath.e "Link to this definition")
:   The mathematical constant *e*, as a float.

cmath.tau[¶](https://docs.python.org/3/library/cmath.html#cmath.tau "Link to this definition")
:   The mathematical constant *τ*, as a float.

    Added in version 3.6.

cmath.inf[¶](https://docs.python.org/3/library/cmath.html#cmath.inf "Link to this definition")
:   Floating-point positive infinity. Equivalent to `float('inf')`.

    Added in version 3.6.

cmath.infj[¶](https://docs.python.org/3/library/cmath.html#cmath.infj "Link to this definition")
:   Complex number with zero real part and positive infinity imaginary
    part. Equivalent to `complex(0.0, float('inf'))`.

    Added in version 3.6.

cmath.nan[¶](https://docs.python.org/3/library/cmath.html#cmath.nan "Link to this definition")
:   A floating-point “not a number” (NaN) value. Equivalent to
    `float('nan')`. See also [`math.nan`](https://docs.python.org/3/library/math.html#math.nan "math.nan").

    Added in version 3.6.

cmath.nanj[¶](https://docs.python.org/3/library/cmath.html#cmath.nanj "Link to this definition")
:   Complex number with zero real part and NaN imaginary part. Equivalent to
    `complex(0.0, float('nan'))`.

    Added in version 3.6.

Note that the selection of functions is similar, but not identical, to that in
module [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.)."). The reason for having two modules is that some users aren’t
interested in complex numbers, and perhaps don’t even know what they are. They
would rather have `math.sqrt(-1)` raise an exception than return a complex
number. Also note that the functions defined in `cmath` always return a
complex number, even if the answer can be expressed as a real number (in which
case the complex number has an imaginary part of zero).

A note on branch cuts: They are curves along which the given function fails to
be continuous. They are a necessary feature of many complex functions. It is
assumed that if you need to compute with complex functions, you will understand
about branch cuts. Consult almost any (not too elementary) book on complex
variables for enlightenment. For information of the proper choice of branch
cuts for numerical purposes, a good reference should be the following:

See also

Kahan, W: Branch cuts for complex elementary functions; or, Much ado about
nothing’s sign bit. In Iserles, A., and Powell, M. (eds.), The state of the art
in numerical analysis. Clarendon Press (1987) pp165–211.