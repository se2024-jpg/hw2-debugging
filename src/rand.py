"""
This module provides a function to generate a random array of integers.

It includes the `random_array` function, which fills a given list with random integers
between 1 and 20 using the `shuf` command-line utility.
"""

import subprocess


def random_array(arr):
    """
    Fills the given list with random integers between 1 and 20.

    :param arr: List to be filled with random integers.
    :return: The list filled with random integers.
    """
    for i, _ in enumerate(arr):
        # Running the subprocess command
        result = subprocess.run(["shuf", "-i", "1-20", "-n", "1"],
                                capture_output=True, text=True, check=True)
        # Convert the output to integer, ensuring to strip any trailing
        # newlines or spaces
        # Need to specify base as 10
        arr[i] = int(result.stdout.strip(), base=10)
    return arr
