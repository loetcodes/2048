#!/usr/bin/env python3
#--------------------------------------------------------------------
#
# Version: 1.0.0
# Date: 19-04-2020
# Author: loet
# 
# MIT License
# Copyright (c) 2020 Louisa
#
#--------------------------------------------------------------------

"""
Testing Game functions

"""

import utils


class TestSuite:
    """ Class to test general output of functions.
    """
    def __init__(self, name):
        self.name = name
        self.total_tests = 0
        self.total_passed = 0
        self.total_failed = 0


    def compute_result(self, computed, expected):
        """ Compares the computed result to the expected result.
        """
        if computed == expected:
            self.total_passed += 1
        else:
            self.total_failed += 1


    def report_results(self):
        """ Reports the total tests conducted, numbers passed and failed.
        """
        title = "Testing: " + self.name
        all_chars_length = 80
        title_length = len(title)
        padding = (all_chars_length - title_length) // 2
        message = "=" * padding + title + "=" * padding
        message += ""
        message += "Total Tests: " + self.total_tests + "\n"
        message += "Passed: " + self.total_passed + "\n"
        message += "Failed: " + self.total_failed + "\n"
        message += "=" * all_chars_length
        return message


def test_sum_new_tiles(test_cases):
    """ Tests the sum_new_tiles function.
    Takes a list of tuples. First value in the tuple is the value to compute,
    second is the expected result.
    """
    test_cases = [
        ()
    ]


if __name__ == "__main__":
    TEST = [2, 2, 4, 0]
    # merge_result = [4, 4, 0, 0]
    assert utils.sum_new_tiles(TEST) == 4, "Incorrect result. Expected:4"

    TEST = [2, 2, 4, 4]
    assert utils.sum_new_tiles(TEST) == 12, "Incorrect result. Expected:12"

    TEST = [2, 2, 4, 2]
    assert utils.sum_new_tiles(TEST) == 4, "Incorrect result. Expected:12"

    TEST = [2, 4, 2, 4]
    assert utils.sum_new_tiles(TEST) == 0, "Incorrect result. Expected:12"

    TEST = [2, 0, 0, 2]
    assert utils.sum_new_tiles(TEST) == 4, "Incorrect result. Expected:12"

    TEST = [2, 0, 2, 2]
    assert utils.sum_new_tiles(TEST) == 4, "Incorrect result. Expected:12"

    print("All tests passed.")
