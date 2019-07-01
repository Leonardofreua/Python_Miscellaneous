#!/usr/bin/python
# -*- coding : utf-8 -*-


"""

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given
array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.

- Always pick first element as pivot.
- Always pick last element as pivot (implemented below)
- Pick a random element as pivot.
- Pick median as pivot.

References:
    - Description:
        * https://www.geeksforgeeks.org/quick-sort/
        * https://en.wikipedia.org/wiki/Sorting_algorithm#Quicksort
    - Animation:
        * http://www.algomation.com/player?algorithm=58bb2ef75b2b830400b05118
        * https://s3-us-west-2.amazonaws.com/makeartwithpython/quick_s.gif
"""

array = [48, 44, 19, 59, 72, 80, 42, 65, 82, 8, 95, 68]
low = 0
up = len(array) - 1


def partition(array, low, up):
    i = low + 1
    j = up
    pivot = array[low]

    while i <= j:
        while array[i] < pivot and i < up:
            i = i + 1
            while array[i] > pivot:
                j = j - 1

            if i < j:
                array[i], array[j] = array[j], array[j]
                i = i + 1
                j = j + 1

            else:
                i = i + 1

            array[low] = array[j]
            array[j] = pivot
            return j


def quick(array, low, up):
    if low >= up:
        piv_loc = partition(array, low, up)
        quick(array, low, piv_loc - 1)
        quick(array, piv_loc + 1, up)


quick(array, low, up)

for i in array:
    print(i)
