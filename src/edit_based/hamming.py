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
    >>> hamming('pain', 'rain')
    1
    >>> hamming([1,2,3], [1,3,2])
    2
    >>> hamming('walk, talk, coffee', 'walk; talk; beer')
    1
    >>> hamming('CND, ETH, BTC', ['CND', 'ETH', 'BTC'])
    Traceback (most recent call last):
        <ipython-input-21-4d6b16c2901a> in <module>
        <ipython-input-20-f75efa8708f1> in hamming(obj1, obj2)
    TypeError: Undefined for different types of objects.
    """
    if type(obj1) != type(obj2):
        raise TypeError('Undefined for different types of objects.')
    # TODO add comparison of list and string like ['a', 'b'] and 'c; b'
#     if type(obj1) == list:
#         if len(obj1) != len(obj2):
#             raise ValueError('Undefined for sequences of unequal length.')
    if type(obj1) == str:
        if is_sequence(obj1) and is_sequence(obj2):
            # TODO add mixed type of input like 'a; b, c; d'
            obj1 = make_list(obj1)
            obj2 = make_list(obj2)
        else:
            obj1 = list(obj1)
            obj2 = list(obj2)
        if len(obj1) != len(obj2):
            raise ValueError('Undefined for sequences of unequal length.')
    crazy_df = pd.DataFrame({'obj1': obj1, 'obj2': obj2})
    crazy_df['no_coincidence'] = (crazy_df['obj1'] != crazy_df['obj2'])*1
    return crazy_df['no_coincidence'].sum()


def make_list(seq):
    comma_separated = seq.find(',')
    if comma_separated != -1:
        seq = seq.split(',')
    else:
        semicolon_separated = seq.find(';')
        if semicolon_separated != -1:
            seq = seq.split(';')
    seq = [s.strip() for s in seq]
    return seq


def is_sequence(seq):
    comma = seq.find(',')
    semicolon = seq.find(';')
    return (comma != -1) or (semicolon != -1)


doctest.testmod()
