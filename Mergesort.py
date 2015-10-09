
def mergesort(arr):
    size = len(arr)
    if size == 2:
        if arr[0] > arr[1]:
            return [arr[1], arr[0]]
        else:
            return arr
    if size <= 1:
        return [arr[0]]
    if size%2 == 0:
        left_end = (size/2) - 1
        right_start = size/2
    else:
        left_end = (size - 1) / 2
        right_start = (size + 1) / 2

    left_arr = mergesort(arr[0:left_end+1])
    right_arr = mergesort(arr[right_start:])

    i = j = 0
    result = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] > right_arr[j]:
            result.append(right_arr[j])
            j += 1
            continue
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
            continue
    if i == len(left_arr):
        result.extend(right_arr[j:])
    if j == len(right_arr):
        result.extend(left_arr[i:])
    return result


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
    import random

    from timeit import default_timer as timer
    import numpy as np

    mergesort_time = []
    quicksort_time = []
    timsort_time = []

    for i in range (50):
        n = 10000
        unsorted_arr = [random.randint(1, n) for i in range(n)]
        t0 = timer()
        sorted_Arr = mergesort(unsorted_arr)
        t1 = timer()
        mergesort_time.append(t1-t0)
        # print "Mergesort",(t1 - t0)

        t4 = timer()
        quick_sorted_arr = quicksort(unsorted_arr)
        t5 = timer()
        quicksort_time.append(t5-t4)
        # print "Quicksort", (t5-t4)

        t2 = timer()
        sorted(unsorted_arr)
        t3 = timer()
        timsort_time.append(t3-t2)
        # print "Timsort", (t3-t2)

    np_mergesort_time = np.array(mergesort_time)
    print "Avg mergesort time:", np_mergesort_time.mean()

    np_quicksort_time = np.array(quicksort_time)
    print "Avg quicksort time:", np_quicksort_time.mean()

    np_timsort_time = np.array(timsort_time)
    print "Avg timsort time:", np_timsort_time.mean()
