---
id: python-normaldist-https-docs-python-org-3-library-statistics-html-s-19fe5e6d
type: concept
title: '[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist
  "statistics.NormalDist") objects[¶](https://docs.python.org/3/library/statistics.html#normaldist-objects
  "Link to this heading")'
description: '[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist
  "statistics.NormalDist") is a tool for creating and manipulating normal'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/statistics.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## [`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") objects[¶](https://docs.python.org/3/library/statistics.html#normaldist-objects "Link to this heading")

[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") is a tool for creating and manipulating normal
distributions of a [random variable](http://www.stat.yale.edu/Courses/1997-98/101/ranvar.htm). It is a
class that treats the mean and standard deviation of data
measurements as a single entity.

Normal distributions arise from the [Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem) and have a wide range
of applications in statistics.

*class* statistics.NormalDist(*mu=0.0*, *sigma=1.0*)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "Link to this definition")
:   Returns a new *NormalDist* object where *mu* represents the [arithmetic
    mean](https://en.wikipedia.org/wiki/Arithmetic_mean) and *sigma*
    represents the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation).

    If *sigma* is negative, raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError").

    mean[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mean "Link to this definition")
    :   A read-only property for the [arithmetic mean](https://en.wikipedia.org/wiki/Arithmetic_mean) of a normal
        distribution.

    median[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.median "Link to this definition")
    :   A read-only property for the [median](https://en.wikipedia.org/wiki/Median) of a normal
        distribution.

    mode[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.mode "Link to this definition")
    :   A read-only property for the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) of a normal
        distribution.

    stdev[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.stdev "Link to this definition")
    :   A read-only property for the [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) of a normal
        distribution.

    variance[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.variance "Link to this definition")
    :   A read-only property for the [variance](https://en.wikipedia.org/wiki/Variance) of a normal
        distribution. Equal to the square of the standard deviation.

    *classmethod* from\_samples(*data*)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.from_samples "Link to this definition")
    :   Makes a normal distribution instance with *mu* and *sigma* parameters
        estimated from the *data* using [`fmean()`](https://docs.python.org/3/library/statistics.html#statistics.fmean "statistics.fmean") and [`stdev()`](https://docs.python.org/3/library/statistics.html#statistics.stdev "statistics.stdev").

        The *data* can be any [iterable](https://docs.python.org/3/glossary.html#term-iterable) and should consist of values
        that can be converted to type [`float`](https://docs.python.org/3/library/functions.html#float "float"). If *data* does not
        contain at least two elements, raises [`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError "statistics.StatisticsError") because it
        takes at least one point to estimate a central value and at least two
        points to estimate dispersion.

    samples(*n*, *\**, *seed=None*)[¶](https://docs.python.org/3/library/statistics.html#statistics.NormalDist.samples "Link to this definition")
    :   Generates *n* random samples for a given mean and standard deviation.
        Returns a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of [`float`](https://docs.python.org/3/library/functions.html#fl