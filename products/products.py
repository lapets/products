"""Pre-partitioned Cartesian product iterables.

Simple function for building ensembles of iterables
that are disjoint partitions of an overall Cartesian product.
"""

import doctest
import itertools
from parts import parts

def products(*args, number=None):
    """
    Build the specified number disjoint subsets (as iterables)
    of the Cartesian product. The disjoint subsets are all
    entries in the overall result, which is a list.

    >>> p = itertools.product([1,2], {'a', 'b'}, (True, False))
    >>> p_ = products([1,2], {'a', 'b'}, (True, False))
    >>> list(p) == list(list(p_)[0])
    True
    >>> list(list(products())[0])
    [()]
    >>> list(list(products([1,2]))[0])
    [(1,), (2,)]
    >>> (x, y, z) = ([1,2], ['a','b'], [True, False])
    >>> [list(s) for s in products(x, y, number=2)]
    [[(1, 'a'), (1, 'b')], [(2, 'a'), (2, 'b')]]
    >>> for s in [list(s) for s in products(x, y, z, number=2)]:
    ...     print(s)
    [(1, 'a', True), (1, 'a', False), (1, 'b', True), (1, 'b', False)]
    [(2, 'a', True), (2, 'a', False), (2, 'b', True), (2, 'b', False)]
    >>> ss = [set(s) for s in products(x, y, z, x, y, z, number=5)]
    >>> s = ss[0] | ss[1] | ss[2] | ss[3] | ss[4]
    >>> s == set(itertools.product(x, y, z, x, y, z))
    True
    >>> set([len(ss[i] & ss[j]) for i in range(5) for j in range(5) if i != j])
    {0}
    >>> len(products(*[[1,2,3]]*1000, number=5))
    5
    >>> ls = [len(products(*[[1,2]]*1000, number=n)) for n in range(1, 100)]
    >>> ls == list(range(1, 100))
    True
    >>> products([1,2], number='abc')
    Traceback (most recent call last):
      ...
    TypeError: number of disjoint subsets must be an integer
    >>> products((i for i in range(3)), number=2)
    Traceback (most recent call last):
      ...
    TypeError: arguments must be of type list, set, frozenset, or tuple
    >>> products([1,2], number=0)
    Traceback (most recent call last):
      ...
    ValueError: number of disjoint subsets must be a positive integer
    >>> products([1,2], number=0)
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
