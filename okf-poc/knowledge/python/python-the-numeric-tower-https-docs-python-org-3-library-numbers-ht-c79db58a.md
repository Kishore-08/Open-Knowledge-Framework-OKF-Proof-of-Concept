---
id: python-the-numeric-tower-https-docs-python-org-3-library-numbers-ht-c79db58a
type: concept
title: The numeric tower[¶](https://docs.python.org/3/library/numbers.html#the-numeric-tower
  "Link to this heading")
description: '*class* numbers.Complex[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/numbers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## The numeric tower[¶](https://docs.python.org/3/library/numbers.html#the-numeric-tower "Link to this heading")

*class* numbers.Complex[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex "Link to this definition")
:   Subclasses of this type describe complex numbers and include the operations
    that work on the built-in [`complex`](https://docs.python.org/3/library/functions.html#complex "complex") type. These are: conversions to
    `complex` and [`bool`](https://docs.python.org/3/library/functions.html#bool "bool"), [`real`](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "numbers.Complex.real"), [`imag`](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "numbers.Complex.imag"), `+`,
    `-`, `*`, `/`, `**`, [`abs()`](https://docs.python.org/3/library/functions.html#abs "abs"), [`conjugate()`](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "numbers.Complex.conjugate"), `==`, and
    `!=`. All except `-` and `!=` are abstract.

    real[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "Link to this definition")
    :   Abstract. Retrieves the real component of this number.

    imag[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "Link to this definition")
    :   Abstract. Retrieves the imaginary component of this number.

    *abstractmethod* conjugate()[¶](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "Link to this definition")
    :   Abstract. Returns the complex conjugate. For example, `(1+3j).conjugate()
        == (1-3j)`.

*class* numbers.Real[¶](https://docs.python.org/3/library/numbers.html#numbers.Real "Link to this definition")
:   To [`Complex`](https://docs.python.org/3/library/numbers.html#numbers.Complex "numbers.Complex"), `Real` adds the operations that work on real
    numbers.

    In short, those are: a conversion to [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`math.trunc()`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc"),
    [`round()`](https://docs.python.org/3/library/functions.html#round "round"), [`math.floor()`](https://docs.python.org/3/library/math.html#math.floor "math.floor"), [`math.ceil()`](https://docs.python.org/3/library/math.html#math.ceil "math.ceil"), [`divmod()`](https://docs.python.org/3/library/functions.html#divmod "divmod"), `//`,
    `%`, `<`, `<=`, `>`, and `>=`.

    Real also provides defaults for [`complex()`](https://docs.python.org/3/library/functions.html#complex "complex"), [`real`](https://docs.python.org/3/library/numbers.html#numbers.Complex.real "numbers.Complex.real"),
    [`imag`](https://docs.python.org/3/library/numbers.html#numbers.Complex.imag "numbers.Complex.imag"), and [`conjugate()`](https://docs.python.org/3/library/numbers.html#numbers.Complex.conjugate "numbers.Complex.conjugate").

*class* numbers.Rational[¶](https://docs.python.org/3/library/numbers.html#numbers.Rational "Link to this definition")
:   Subtypes [`Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real") and adds [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator") and
    [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator") properties. It also provides a default for
    [`float()`](https://docs.python.org/3/library/functions.html#float "float").

    The [`numerator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.numerator "numbers.Rational.numerator") and [`denominator`](https://docs.python.org/3/library/numbers.html#numbers.Rational.denominator "numbers.Rational.denominator") values
    should be instances of [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral") and should be in lowest terms with
    `denominator` positive.

    numerator[¶](https://docs.python.o