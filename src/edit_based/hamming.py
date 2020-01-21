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


def hamming(obj1: Union[str, list], obj2: Union[str, list], sequences: bool)\
        -> int:
    """
    >>> hamming('cofee', 'beer', sequences=True)
    1
    >>> hamming('cindi', 'cator', sequences=False)
    4
    >>> hamming('love', 'love', sequences=True)
    0
    >>> hamming('pain', 'psql', sequences=False)
    3
    >>> hamming([1,2,3], [1,3,2], sequences=True)
    2
    >>> hamming('walk, talk, coffee', 'walk; talk, beer', sequences=True)
    1
    >>> hamming('CND, ETH, BTC', ['CND', 'ETH', 'BTC'], sequences=True)
    0
    """
    if not sequences:
        if (type(obj1) != str) or (type(obj1) != str):
            raise TypeError('Put sequences=True for lists')
    obj1 = if_string(obj1, sequences)
#     print(obj1)
    obj2 = if_string(obj2, sequences)
#     print(obj2)
    if len(obj1) != len(obj2):
        raise ValueError('Undefined for sequences of unequal length.')
    crazy_df = pd.DataFrame({'obj1': obj1, 'obj2': obj2})
    crazy_df['no_coincidence'] = (crazy_df['obj1'] != crazy_df['obj2']) * 1
    return crazy_df['no_coincidence'].sum()


def make_list(seq):
    seq = seq.replace(';', ',')
    if (seq.find(',') == -1) and (seq.find(';') == -1):
        seq = seq.replace(' ', ',')
    seq = seq.split(',')
    seq = [s.strip() for s in seq]
    return seq


def if_string(seq, sequences):
    if type(seq) == str:
        if sequences:
            seq = make_list(seq)
        else:
            seq = list(seq)
    return seq


doctest.testmod()
