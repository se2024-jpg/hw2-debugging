"""
This module implements the merge sort algorithm.

It includes two functions:
1. `merge_sort`: A recursive function to sort an array.
2. `recombine`: A helper function that merges two sorted arrays.

The module also demonstrates sorting a random array using `merge_sort`.
"""
import random

def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    if len(arr) == 1:  # Removed unnecessary parentheses
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


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
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


array = random.sample(range(1, 100), 20)
arr_out = merge_sort(array)

print(arr_out)
