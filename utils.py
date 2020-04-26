#!/usr/bin/env python3
#--------------------------------------------------------------------
#
# MIT License
# Copyright (c) 2020 Louisa
# Version: 1.0.0
# Date: 11-04-2020
# Author: loet
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


def sum_new_tiles(line):
    """ Get the sum of tiles that merged together.
    """
    total = 0
    first_tile, second_tile = 0, 1
    while second_tile < len(line):
        if line[first_tile] == line[second_tile]:
            total += line[first_tile] * 2
            first_tile = second_tile + 1
            second_tile += 2
        elif line[second_tile] == 0:
            second_tile += 1
        else:
            first_tile += 1
            second_tile = first_tile + 1

    return total
