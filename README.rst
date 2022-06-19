========
products
========

Simple function for building ensembles of iterables that are disjoint partitions of an overall Cartesian product.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/products.svg
   :target: https://badge.fury.io/py/products
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/products/badge/?version=latest
   :target: https://products.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/lapets/products/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/lapets/products/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/lapets/products/badge.svg?branch=main
   :target: https://coveralls.io/github/lapets/products?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------

.. |itertools_product| replace:: ``itertools.product``
.. _itertools_product: https://docs.python.org/3/library/itertools.html#itertools.product

Once the |itertools_product|_ has been used to build an iterable for a `Cartesian product <https://en.wikipedia.org/wiki/Cartesian_product>`__, it is already too late to partition that iterable into multiple iterables where each one represents a subset of the product set. Iterables representing disjoint subsets can, for example, make it easier to employ parallelization when processing the product set.

.. |products| replace:: ``products``
.. _products: https://products.readthedocs.io/en/latest/_source/products.html#products.products.products

The |products|_ function in this package constructs a list of independent `iterators <https://docs.python.org/3/glossary.html#term-iterator>`__ for a specified number of disjoint subsets of a product set (in the manner of the `parts <https://pypi.org/project/parts>`__ library), exploiting as much information as is available about the constituent factor sets of the overall product set in order to do so.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/products>`__::

    python -m pip install products

The library can be imported in the usual ways::

    import products
    from products import products

.. |product| replace:: ``product``
.. _product: https://docs.python.org/3/library/itertools.html#itertools.product

This library provides an alternative to the built-in Cartesian product function |product|_ found in `itertools <https://docs.python.org/3/library/itertools.html>`__, making it possible to iterate over multiple disjoint subsets of a Cartesian product (even in parallel). Consider the Cartesian product below::

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

This library makes it possible to create a number of iterators such that each iterator represents a disjoint subset of the overall Cartesian product. The example below does so for the Cartesian product introduced above, creating four disjoint subsets (rather than one overall set)::

    >>> from products import products
    >>> ss = products([1, 2], {'a', 'b'}, (True, False), number=4)
    >>> for s in ss:
    ...     print(list(s))
    [(1, 'a', True), (1, 'a', False)]
    [(1, 'b', True), (1, 'b', False)]
    [(2, 'a', True), (2, 'a', False)]
    [(2, 'b', True), (2, 'b', False)]

The `iterable <https://docs.python.org/3/glossary.html#term-iterable>`__ corresponding to each subset is *independent* from the others, making it possible to employ techniques such parallelization (*e.g.*, using the built-in `multiprocessing <https://docs.python.org/3/library/multiprocessing.html>`__ library) when operating on the elements of the overall Cartesian product.

Development
-----------
All installation and development dependencies are managed using `setuptools <https://pypi.org/project/setuptools>`__ and are fully specified in ``setup.py``. The ``extras_require`` parameter is used to `specify optional requirements <https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
.. include:: toc.rst

The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__::

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. ../setup.py && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see ``setup.cfg`` for configuration details)::

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python products/products.py -v

Style conventions are enforced using `Pylint <https://www.pylint.org>`__::

    python -m pip install .[lint]
    python -m pylint products

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/lapets/products>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/products>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Remove any old build/distribution files. Then, package the source into a distribution archive using the `wheel <https://pypi.org/project/wheel>`__ package::

    rm -rf dist *.egg-info
    python setup.py sdist bdist_wheel

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__ using the `twine <https://pypi.org/project/twine>`__ package::

    python -m twine upload dist/*
