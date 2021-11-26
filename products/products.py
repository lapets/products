"""
Simple function for building ensembles of iterators that
represent disjoint partitions of an overall Cartesian product.
"""
from __future__ import annotations
from typing import Optional
import doctest
import itertools
from parts import parts

def products(*args, number: Optional[int] = None):
    """
    Return a list of the specified number of disjoint subsets (as iterators)
    of the Cartesian product (such that the union of the disjoint subsets is
    equal to the Cartesian product).

    >>> ss = products([1, 2], {'a', 'b'}, (False, True), number=3)
    >>> for s in sorted([sorted(list(s)) for s in ss]):
    ...     for t in s:
    ...         print(t)
    (1, 'a', False)
    (1, 'a', True)
    (1, 'b', False)
    (1, 'b', True)
    (2, 'a', False)
    (2, 'a', True)
    (2, 'b', False)
    (2, 'b', True)

    Two additional basic examples are presented below.

    >>> (x, y, z) = ([1, 2], ['a', 'b'], [True, False])
    >>> [list(s) for s in products(x, y, number=2)]
    [[(1, 'a'), (1, 'b')], [(2, 'a'), (2, 'b')]]
    >>> for s in [list(s) for s in products(x, y, z, number=2)]:
    ...     print(s)
    [(1, 'a', True), (1, 'a', False), (1, 'b', True), (1, 'b', False)]
    [(2, 'a', True), (2, 'a', False), (2, 'b', True), (2, 'b', False)]

    By default (if the ``number`` argument is not assigned a value), the number
    of disjoint subsets is one. Note that the union of the disjoint subsets is
    equivalent to the output of the ``itertools.product`` function.

    >>> p = itertools.product([1, 2], {'a', 'b'}, (True, False))
    >>> ss = products([1, 2], {'a', 'b'}, (True, False))
    >>> list(p) == list(list(ss)[0])
    True

    If no sets are specified, the Cartesian product consists of a single empty
    tuple. If there is one set, the Cartesian product consists of a set of
    one-element tuples. In both cases, a list of disjoint subsets is returned
    as in all other cases (even though the number of disjoint subsets may be
    one).

    >>> list(list(products())[0])
    [()]
    >>> list(list(products([1, 2]))[0])
    [(1,), (2,)]

    It is possible to confirm that the returned subsets are disjoint, and that
    the union of the disjoint subsets is the Cartesian product.

    >>> (x, y, z) = ([1, 2], ['a', 'b'], [True, False])
    >>> ss = [set(s) for s in products(x, y, z, x, y, z, number=5)]
    >>> set([len(ss[i] & ss[j]) for i in range(5) for j in range(5) if i != j])
    {0}
    >>> s = ss[0] | ss[1] | ss[2] | ss[3] | ss[4]
    >>> s == set(itertools.product(x, y, z, x, y, z))
    True
    >>> len(products(*[[1, 2, 3]]*1000, number=5))
    5
    >>> ls = [len(products(*[[1, 2]]*1000, number=n)) for n in range(1, 100)]
    >>> ls == list(range(1, 100))
    True

    Any attempt to apply this function to arguments of an unsupported type
    raises an exception.

    >>> products([1, 2], number='abc')
    Traceback (most recent call last):
      ...
    TypeError: number of disjoint subsets must be an integer
    >>> products((i for i in range(3)), number=2)
    Traceback (most recent call last):
      ...
    TypeError: arguments must be of type list, set, frozenset, or tuple
    >>> products([1, 2], number=0)
    Traceback (most recent call last):
      ...
    ValueError: number of disjoint subsets must be a positive integer
    >>> products([1, 2], number=0)
    Traceback (most recent call last):
      ...
    ValueError: number of disjoint subsets must be a positive integer
    """
    if not all(isinstance(arg, (list, set, frozenset, tuple)) for arg in args):
        raise TypeError(
            'arguments must be of type list, set, frozenset, or tuple'
        )

    if number is not None and not isinstance(number, int):
        raise TypeError('number of disjoint subsets must be an integer')

    if number is not None and number < 1:
        raise ValueError('number of disjoint subsets must be a positive integer')

    # If no target number of disjoint subsets has been supplied, simply
    # return a single product. Note that this function is not equivalent to
    # `itertools.product` because this function always returns a list
    # of iterables (the subsets).
    if number is None or number == 1:
        return [itertools.product(*args)]

    # Determine the product of which prefix of arguments to break up
    # based on the target number of disjoint subsets.
    number_ = 1
    index = len(args)
    for (i, a) in enumerate(args):
        number_ = number_ * len(a)
        if number_ >= number:
            index = min(len(args), i + 1)
            break

    # Create an iterable for each prefix.
    prefixes = list(parts(list(itertools.product(*args[0:index])), number))

    # For each prefix, create an iterable for that prefix by concatenating
    # elements of the prefix to elements of suffix product.
    def generator(prefix):
        for p in prefix:
            for s in itertools.product(*args[index:]):
                yield p + s

    return [generator(prefix) for prefix in prefixes]

if __name__ == "__main__":
    doctest.testmod() # pragma: no cover
