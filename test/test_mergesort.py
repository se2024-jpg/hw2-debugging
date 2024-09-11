import sys
sys.path.append('../src')  # Ensure this line is at the top

import pytest
from hw2_debugging import mergeSort

def test_merge_sort_with_integers():
    arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == sorted(arr), "The array should be sorted in ascending order."

def test_merge_sort_with_negative_numbers():
    arr = [-1, -3, -2, -5, -4]
    sorted_arr = mergeSort(arr)
    assert sorted_arr == sorted(arr), "The array should be sorted in ascending order with negative numbers."

def test_merge_sort_with_empty_list():
    arr = []
    sorted_arr = mergeSort(arr)
    assert sorted_arr == [], "The array should be empty and thus return an empty list."

