========
products
========

Simple function for building ensembles of iterables that are disjoint partitions of an overall Cartesian product.

|pypi| |readthedocs| |travis| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/products.svg
   :target: https://badge.fury.io/py/products
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/products/badge/?version=latest
   :target: https://products.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |travis| image:: https://app.travis-ci.com/lapets/products.svg?branch=master
   :target: https://app.travis-ci.com/lapets/products
   :alt: Travis CI build status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/products/badge.svg?branch=master
   :target: https://coveralls.io/github/lapets/products?branch=master
   :alt: Coveralls test coverage summary.

Purpose
-------
Once the ``iterables.product`` `function <https://docs.python.org/3/library/itertools.html#itertools.product>`_ has been used to build an iterable for a Cartesian product, it is already too late to partition that iterable into multiple iterables where each one represents a subset of the product set. Iterables representing disjoint subsets can, for example, make it easier to employ parallelization when processing the product set. The ``products`` function in this package constructs a list of independent iterators for a specified number of disjoint subsets of a product set (in the manner of the `parts <https://pypi.org/project/parts/>`_ library), exploiting as much information as possible about the constituent factor sets of the overall product set in order to do so.

Package Installation and Usage
------------------------------
The package is available on `PyPI <https://pypi.org/project/products/>`_::

    python -m pip install products

The library can be imported in the usual ways::

    import products
    from products import products

This library provides an alternative to the built-in Cartesian product function found in `itertools <https://docs.python.org/3/library/itertools.html>`_, making it possible to iterate over multiple disjoint subsets of a Cartesian product (even in parallel). Consider the Cartesian product below::

    >>> from itertools import product
    >>> p = product([1, 2], {'a', 'b'}, (False, True))
    >>> for t in p:
    ...     print(t)
    (1, 'a', False)
    (1, 'a', True)
    (1, 'b', False)
    (1, 'b', True)
    (2, 'a', False)
    (2, 'a', True)
    (2, 'b', False)
    (2, 'b', True)

This library makes it possible to create a number of iterators such that each iterator represents a disjoint subset of the overall Cartesian product. The example below does so for the above Cartesian product, creating four disjoint subsets::

    >>> from products import products
    >>> ss = products([1, 2], {'a', 'b'}, (True, False), number=4)
    >>> for s in ss:
    ...     print(list(s))
    [(1, 'a', True), (1, 'a', False)]
    [(1, 'b', True), (1, 'b', False)]
    [(2, 'a', True), (2, 'a', False)]
    [(2, 'b', True), (2, 'b', False)]

The iterable corresponding to each subset is independent from the others, making it possible to employ techniques such as multiprocessing when operating on the elements of the overall Cartesian product.

Documentation
-------------
.. include:: toc.rst

The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org/>`_::

    cd docs
    python -m pip install -r requirements.txt
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. ../setup.py && make html

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configuration details)::

    python -m pip install nose coverage
    nosetests --cover-erase

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python products/products.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    python -m pip install pylint
    pylint products

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/products>`_ for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
