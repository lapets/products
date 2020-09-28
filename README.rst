========
products
========

Simple function for building ensembles of iterables that are disjoint partitions of an overall Cartesian product.

|pypi| |travis|

.. |pypi| image:: https://badge.fury.io/py/products.svg
   :target: https://badge.fury.io/py/products
   :alt: PyPI version and link.

.. |travis| image:: https://travis-ci.com/lapets/products.svg?branch=master
   :target: https://travis-ci.com/lapets/products

Purpose
-------
Once the ``iterables.product`` `function <https://docs.python.org/3/library/itertools.html#itertools.product>`_ has been used to build an iterable for a Cartesian product, it is already too late to partition that iterable into multiple iterables where each one represent a subset of the product set. Iterables representing disjoint subsets can, for example, make it easier to employ parallelization when processing the product set. The ``products`` function in this package attempts to construct the specified number of disjoint subsets of a product set (in the manner of the `parts <https://pypi.org/project/parts/>`_ library), exploiting as much information as possible about the constituent factor sets of the overall product set in order to do so.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install products

The library can be imported in the usual ways::

    import products
    from products import products

Testing and Conventions
-----------------------
All unit tests are executed and their coverage is measured when using `nose <https://nose.readthedocs.io/>`_ (see ``setup.cfg`` for configution details)::

    nosetests

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`_::

    python products/products.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org/>`_::

    pylint products

Contributions
-------------
In order to contribute to the source code, open an issue or submit a pull request on the GitHub page for this library.

Versioning
----------
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`_.
