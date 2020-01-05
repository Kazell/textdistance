# it is not smth I am supposed to do in the middle of the night

'''
In information theory, the Hamming distance between
two strings of equal length is the number of positions
at which the corresponding symbols are different.
In other words, it measures the minimum number
of substitutions required to change one string into the other,
or the minimum number of errors that could have transformed
one string into the other. In a more general context,
the Hamming distance is one of several string metrics for measuring
the edit distance between two sequences. It is named after the American mathematician Richard Hamming.
(https://en.wikipedia.org/wiki/Hamming_distance)
'''
import pandas as pd
import doctest


def hamming(str1, str2):
    """
    >>> hamming('I was in your eyes', 'thinking I belong them')
    Traceback (most recent call last):
        <ipython-input-22-8dd38782a5ef> in <module>
        <ipython-input-21-3a6a0e35205f> in hamming(str1, str2)
        raise ValueError('Undefined for sequences of unequal length.')
    ValueError: Undefined for sequences of unequal length.
    >>> hamming('cindi', 'cator')
    4
    >>> hamming('love', 'love')
    0
    >>> hamming('pain', 'rain')
    1
    """
    if len(str1) != len(str2):
        raise ValueError('Undefined for sequences of unequal length.')
    str1 = list(str1)
    str2 = list(str2)
    crazy_df = pd.DataFrame({'str1': str1, 'str2': str2})
    crazy_df['no_coincidence'] = (crazy_df['str1'] != crazy_df['str2'])*1
    return crazy_df['no_coincidence'].sum()


doctest.testmod()
