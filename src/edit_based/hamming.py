# it is much more interesting to apply it to real sequences
# application to lists and sequences separated by commas or semicolons

'''
In information theory, the Hamming distance between
two objings of equal length is the number of positions
at which the corresponding symbols are different.
In other words, it measures the minimum number
of substitutions required to change one objing into the other,
or the minimum number of errors that could have transformed
one objing into the other. In a more general context,
the Hamming distance is one of several objing metrics for measuring
the edit distance between two sequences. It is named after the American
mathematician Richard Hamming.
(https://en.wikipedia.org/wiki/Hamming_distance)
'''
from typing import Union
import pandas as pd
import doctest


def hamming(obj1: Union[str, list], obj2: Union[str, list]) -> int:
    """
    >>> hamming('cofee', 'beer')
    Traceback (most recent call last):
        <ipython-input-22-8dd38782a5ef> in <module>
        <ipython-input-21-3a6a0e35205f> in hamming(obj1, obj2)
        raise ValueError('Undefined for sequences of unequal length.')
    ValueError: Undefined for sequences of unequal length.
    >>> hamming('cindi', 'cator')
    4
    >>> hamming('love', 'love')
    0
    >>> hamming('pain', 'psql')
    3
    >>> hamming([1,2,3], [1,3,2])
    2
    >>> hamming('walk, talk, coffee', 'walk; talk, beer')
    1
    >>> hamming('CND, ETH, BTC', ['CND', 'ETH', 'BTC'])
    0
    """
    obj1 = if_string(obj1)
    obj2 = if_string(obj2)
    if len(obj1) != len(obj2):
        raise ValueError('Undefined for sequences of unequal length.')
    crazy_df = pd.DataFrame({'obj1': obj1, 'obj2': obj2})
    crazy_df['no_coincidence'] = (crazy_df['obj1'] != crazy_df['obj2']) * 1
    return crazy_df['no_coincidence'].sum()


def make_list(seq):
    seq = seq.replace(';', ',')
    seq = seq.split(',')
    seq = [s.strip() for s in seq]
    return seq


def is_sequence(seq):
    comma = seq.find(',')
    semicolon = seq.find(';')
    return (comma != -1) or (semicolon != -1)


def if_string(seq):
    if type(seq) == str:
        if is_sequence(seq):
            seq = make_list(seq)
        else:
            seq = list(seq)
    return seq


doctest.testmod()
