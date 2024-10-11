#!/usr/bin/env python3
"""
module that houses a function that takes
a list with int and float and return
their sum as float
"""

def sum_mixed_list(mxd_list: list) -> float:
    """
    function that takes a list with mixed data
    types, then return the sum of element of
    the list as a float
    """
    return float(sum(mxd_list))
