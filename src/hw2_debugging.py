"""
This module implements the merge sort algorithm.

It includes two functions:
1. `merge_sort`: A recursive function to sort an array.
2. `recombine`: A helper function that merges two sorted arrays.

The module also demonstrates sorting a random array using `merge_sort`.
"""

import random

def merge_sort(input_arr):
    """
    Sorts an array using the merge sort algorithm.
    :param input_arr: List of elements to be sorted.
    :return: Sorted list.
    """
    if len(input_arr) == 1:
        return input_arr

    half = len(input_arr) // 2

    return recombine(merge_sort(input_arr[:half]), merge_sort(input_arr[half:]))


def recombine(left_arr, right_arr):
    """
    Recombines two sorted arrays into a single sorted array.
    :param left_arr: Left sublist.
    :param right_arr: Right sublist.
    :return: Merged and sorted list.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    
    # Ensure correct index assignment and fixing slice vs. int issue
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]  # Fixed indexing
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]  # Fixed indexing
            right_index += 1

    # Ensure correct index assignment for remaining elements
    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]  # Fixed indexing
        right_index += 1

    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]  # Fixed indexing
        left_index += 1

    return merge_arr


arr = random.sample(range(1, 100), 20)
arr_out = merge_sort(arr)

# Fix print statement flush error, ensuring flush is explicitly mentioned if needed
print(arr_out, flush=True)
