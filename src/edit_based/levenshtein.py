# slow algorithm without recursion, matrices, with mention of pandas

'''
In information theory, linguistics and computer science,
the Levenshtein distance is a string metric for measuring
the difference between two sequences. Informally,
the Levenshtein distance between two words is the minimum number
of single-character edits (insertions, deletions or substitutions)
required to change one word into the other. It is named after
the Soviet mathematician Vladimir Levenshtein, who considered this
 distance in 1965.
(https://en.wikipedia.org/wiki/Levenshtein_distance)
'''

import itertools
import doctest

import pandas as pd


# TODO most of the names should be changed
def levenshtein(obj1, obj2, sequences=False):
    # TODO г$вно --> конфетка
    """
    >>> levenshtein('Linux Astra', 'Linux Mint', sequences=True) == 1
    True
    >>> levenshtein('Linux Astra', 'Linux Mint', sequences=False) == 5
    True
    >>> levenshtein('г$вно', 'конфетка', sequences=False) == 8
    True
    >>> levenshtein('любовь', 'морковь', sequences=False) == 4
    True
    >>> levenshtein('картошка', 'бефстроганов') == 10
    True
    """
    # TODO add examples
    if not sequences:
        if (type(obj1) != str) or (type(obj1) != str):
            raise TypeError('Put sequences=True for lists')
        obj1 = list(obj1)
        obj2 = list(obj2)
    else:
        obj1 = make_list(obj1)
        obj2 = make_list(obj2)
    LSDs = []
    common_groups = just_seqs(obj1, obj2)
    for group in common_groups:
        LSDs.append(levenshtein_somnitelnaya_distance(obj1, obj2, group))
    return min(LSDs)


def find_seqs(seq):
    seqs = []
    while seq:
        seqs.append(seq)
        seq = seq[1:]
    return seqs


def just_seqs(obj1, obj2):
    common_elements = []
    for element in obj1:
        if element in obj2:
            common_elements.append(element)
    common_elements = set(common_elements)
    obj1 = [el for el in obj1 if el in common_elements]
    obj2 = [el for el in obj2 if el in common_elements]

    max_length = max(len(obj1), len(obj2))
    if len(obj1) == max_length:
        long = obj1
        short = obj2
    else:
        long = obj2
        short = obj1
    groups_common = []
    for seq in find_seqs(short):
        common = []
        long_temp = long
        for element in seq:
            if element in long_temp:
                index = long_temp.index(element)
                long_temp = long_temp[index:]
                common.append(element)
        groups_common.append(common)
    return groups_common


def levenshtein_somnitelnaya_distance(obj1, obj2, common_group):
    # for one of the objects we have just 1 combination, for another it depends
    first_sequence_init = quasi_permutations(
        element_positions(obj1, common_group),
        common_group,
    )
    second_sequence_init = quasi_permutations(
        element_positions(obj2, common_group),
        common_group,
    )
    LSDs = []  # levenshtein somnitelnaya distance :-)
    if len(first_sequence_init) == 1:
        first_sequence = first_sequence_init[0]
        remainder1 = len(obj1[first_sequence[-1] + 1:])
        first_sequence = [first_sequence[0]] +\
                         [first_sequence[i + 1] - first_sequence[i]
                          for i in range(len(first_sequence) - 1)]
        for seq_init in second_sequence_init:
            seq = seq_init
            remainder2 = len(obj2[seq_init[-1] + 1:])
            seq = [seq[0]] + [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
            l1 = first_sequence + [remainder1]
            l2 = seq + [remainder2]
            useful_positions = [i for i in range(len(l1) - 1) if
                                max(l1[i], l2[i]) + max(l1[i + 1], l2[i + 1]) <=
                                max(l1[i] + l1[i + 1] + 1, l2[i] + l2[i + 1] + 1)]
            first = [first_sequence_init[0][i] for i in useful_positions]
            if len(first) != 0:  # len(first) == len(second))
                first = [first[0]] + [first[i + 1] - first[i] for i in range(len(first) - 1)]
                second = [seq_init[i] for i in useful_positions]
                second = [second[0]] + [second[i + 1] - second[i] for i in range(len(second) - 1)]
                good_guys = []
                for num in range(len(second)):
                    max_index = max(first[num], second[num])
                    good_guys.append(max_index)
                LSD = sum(good_guys) + 1 + max(remainder1, remainder2) - len(good_guys)
            else:
                LSD = max(len(obj1), len(obj2))
            LSDs.append(LSD)
    else:
        second_sequence = second_sequence_init[0]
        remainder2 = len(obj2[second_sequence[-1] + 1:])
        second_sequence = [second_sequence[0]] + \
                          [second_sequence[i + 1] - second_sequence[i]
                           for i in range(len(second_sequence) - 1)]
        for seq_init in first_sequence_init:
            seq = seq_init
            remainder1 = len(obj1[seq[-1] + 1:])
            seq = [seq[0]] + [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]

            l1 = seq + [remainder1]
            l2 = second_sequence + [remainder2]
            useful_positions = [i for i in range(len(l1) - 1) if
                                max(l1[i], l2[i]) + max(l1[i + 1], l2[i + 1]) <=
                                max(l1[i] + l1[i + 1] + 1, l2[i] + l2[i + 1] + 1)]
            first = [seq_init[i] for i in useful_positions]
            if len(first) != 0:
                first = [first[0]] + \
                        [first[i + 1] - first[i] for i in range(len(first) - 1)]
                second = [second_sequence_init[0][i] for i in useful_positions]
                second = [second[0]] + \
                         [second[i + 1] - second[i] for i in range(len(second) - 1)]
                good_guys = []
                for num in range(len(first)):
                    max_index = max(first[num], second[num])
                    good_guys.append(max_index)
                LSD = sum(good_guys) + 1 + max(remainder1, remainder2) - len(good_guys)
            else:
                LSD = max(len(obj1), len(obj2))
            LSDs.append(LSD)
    return min(LSDs)


def element_positions(obj, common_group):
    dict_positions = {}
    for element in common_group:
        obj_tmp = obj
        dict_positions[element] = []
        while element in obj_tmp:
            index = obj_tmp.index(element)
            dict_positions[element].append(index + 1)
            obj_tmp = obj_tmp[index + 1:]
        dict_positions[element] = [sum(dict_positions[element][:n + 1])
                                   for n in range(len(dict_positions[element]))]
        dict_positions[element] = [pos - 1 for pos in dict_positions[element]]
    return dict_positions


def quasi_permutations(element_positions, common_group):
    # return sequences of element positions not to be replaced
    hm = pd.DataFrame(columns=['position'])
    for element in common_group:
        tmp = pd.DataFrame(
            {'position': [element_positions[element]]},
            index=[element],
        )
        hm = pd.concat([hm, tmp])
    quasi = list(itertools.product(*hm['position']))
    quasi = [list(q) for q in quasi
             if sorted(list(q)) == list(q) and len(q) == len(set(q))]
    return quasi


def make_list(seq):
    seq = seq.replace(';', ',')
    seq = seq.replace(' ', ',')
    seq = seq.split(',')
    seq = [s.strip() for s in seq]
    return seq


def is_sequence(seq):
    comma = seq.find(',')
    semicolon = seq.find(';')
    whitespace = seq.find(' ')
    return (comma != -1) or (semicolon != -1) or (whitespace != -1)


def if_string(seq):
    if type(seq) == str:
        if is_sequence(seq):
            seq = make_list(seq)
        else:
            seq = list(seq)
    return seq


doctest.testmod()
