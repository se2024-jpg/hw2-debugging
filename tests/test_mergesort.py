import sys
sys.path.append('../src')  # Ensure this line is at the top

import pytest
from hw2_debugging import merge_sort

def test_merge_sort_with_multiple_elements():
    arr = [5, 2, 9, 1, 5, 6]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == sorted(arr), "The array should be sorted in ascending order."

def test_merge_sort_with_two_elements():
    arr = [9, 1]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 9], "The two-element array should be sorted in ascending order."

def test_merge_sort_with_reversed_elements():
    arr = [5, 4, 3, 2, 1]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5], "The reversed array should be sorted in ascending order."

