__author__ = 'psinha4'

import random

#not stable
def quicksort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    pivot_index = random.randint(0, size-1)
    left_arr = []
    right_arr = []
    pivot_arr = []
    for i, elem in enumerate(arr):
        if elem < arr[pivot_index]:
            left_arr.append(elem)
        elif elem > arr[pivot_index]:
            right_arr.append(elem)
        else:
            pivot_arr.append(elem)
    # print left_arr, pivot_arr, right_arr
    left_arr_sorted = quicksort(left_arr)
    right_arr_sorted = quicksort(right_arr)
    left_arr_sorted.extend(pivot_arr)
    left_arr_sorted.extend(right_arr_sorted)
    # print "=-->", left_arr_sorted
    return left_arr_sorted


if __name__ == '__main__':
    n = 20
    unsorted_arr = [random.randint(1, n) for i in range(n)]
    print unsorted_arr
    print quicksort(unsorted_arr)
