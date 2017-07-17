"""
Given 2 list of integers, output all the integers from the the first list in which their squares
are in the second list

Example:

list 1 = [4, -5, 8, 6, -3, 1]

list 2 = [9, 15, 100, 36, 0, 41]

The program should return [-3, 6] since 9 and 36 are found in the second list
"""

import math
from collections import defaultdict


def find_common_squares_list(list1, list2):

    square_to_root = defaultdict(list)
    is_square_from_list_1 = defaultdict(bool)

    for x in list1:
        square_to_root[x*x] += [x]
        is_square_from_list_1[x*x] = True

    common_squares_list = []

    for l in list2:
        if is_square_from_list_1[l]:
            common_squares_list.extend(square_to_root[l])

    return common_squares_list


list_1 = [4, -5, 8, 6, -3, 1, 3, 0]
list_2 = [9, 15, 100, 36, 0, 41]

print(find_common_squares_list(list_1, list_2))
