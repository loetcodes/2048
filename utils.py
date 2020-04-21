#!/usr/bin/env python3
#--------------------------------------------------------------------
#
# Version: 1.0.0
# Date: 11-04-2020
# Author: loet
# Copyright: 2020 loet
# License: MIT license
#
#--------------------------------------------------------------------

"""
General functions

"""

def merge(line):
    """ Merges a single row or column given as line.
    Returns a new list with merged values.
    """
    result_vals = [0 for num in line]
    for num in line:
        # Push all non-zero values to the front
        if num != 0:
            if 0 in result_vals:
                first_zero = result_vals.index(0)
                result_vals[first_zero] = num

    for num in range(len(line) - 1):
        # Merge numbers that are equal.
        if result_vals[num] == result_vals[num + 1]:
            result_vals[num] = result_vals[num] * 2
            result_vals[num + 1] = 0

    for num in range(len(line)):
        # Delete intermediate zeros
        if result_vals[num] == 0:
            result_vals.append(result_vals.pop(num))
    return result_vals


def sum_new_tiles(original_line, new_line):
    """ Compare the new_line and original_line. Returns the sum
    of the difference between the two.
    """
