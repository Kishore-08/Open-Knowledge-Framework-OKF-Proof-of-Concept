---
id: python-function-details-https-docs-python-org-3-library-statistics--19fe5e6d
type: concept
title: Function details[¶](https://docs.python.org/3/library/statistics.html#function-details
  "Link to this heading")
description: 'Note: The functions do not require the data given to them to be sorted.'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/statistics.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Function details[¶](https://docs.python.org/3/library/statistics.html#function-details "Link to this heading")

Note: The functions do not require the data given to them to be sorted.
However, for reading convenience, most of the examples show sorted sequences.

statistics.mean(*data*)[¶](https://docs.python.org/3/library/statistics.html#statistics.mean "Link to this definition")
:   Return the sample arithmetic mean of *data* which can be a sequence or iterable.

    The arithmetic mean is the sum of the data divided by the number of data
    points. It is commonly called “the average”, although it is only one of many
    different mathematical averages. It is a measure of the central location of
    the data.

    If *data* is empty, [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError") will be raised.

    Some examples of use:

    ```
    >>> mean([1, 2, 3, 4, 4])
    2.8
    >>> mean([-1.0, 2.5, 3.25, 5.75])
    2.625

    >>> from fractions import Fraction as F
    >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
    Fraction(13, 21)

    >>> from decimal import Decimal as D
    >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
    Decimal('0.5625')
    ```

    Note

    The mean is strongly affected by [outliers](https://en.wikipedia.org/wiki/Outlier) and is not necessarily a
    typical example of the data points. For a more robust, although less
    efficient, measure of [central tendency](https://en.wikipedia.org/wiki/Central_tendency), see [`median()`](https://docs.python.org/3/library/statistics.html#statistics.median "statistics.median").

    The sample mean gives an unbiased estimate of the true population mean,
    so that when taken on average over all the possible samples,
    `mean(sample)` converges on the true mean of the entire population. If
    *data* represents the entire population rather than a sample, then
    `mean(data)` is equivalent to calculating the true population mean μ.

statistics.fmean(*data*, *weights=None*)[¶](https://docs.python.org/3/library/statistics.html#statistics.fmean "Link to this definition")
:   Convert *data* to floats and compute the arithmetic mean.

    This runs faster than the [`mean()`](https://docs.python.org/3/library/statistics.html#statistics.mean "statistics.mean") function and it always returns a
    [`float`](https://docs.python.org/3/library/functions.html#float "float"). The *data* may be a sequence or iterable. If the input
    dataset is empty, raises a [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError").

    ```
    >>> fmean([3.5, 4.0, 5.25])
    4.25
    ```

    Optional weighting is supported. For example, a professor assigns a
    grade for a course by weighting quizzes at 20%, homework at 20%, a
    midterm exam at 30%, and a final exam at 30%:

    ```
    >>> grades = [85, 92, 83, 91]
    >>> weights = [0.20, 0.20, 0.30, 0.30]
    >>> fmean(grades, weights)
    87.6
    ```

    If *weights* is supplied, it must be the same length as the *data* or
    a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") will be raised.

    Added in version 3.8.

    Changed in version 3.11: Added support for *weights*.

statistics.geometric\_mean(*data*)[¶](https://docs.python.org/3/library/statistics.html#statistics.geometric_mean "Link to this definition")
:   Convert *data* to floats and compute the geometric mean.

    The geometric mean indicates the central tendency or typical value of the
    *data* using the product of the values (as opposed to the arithmetic mean
    which uses their sum).

    Raises a [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError") if the input dataset is empty,
    if it contains a zero, or if it contains a negative value.
    The *data* may be a sequence or iterab