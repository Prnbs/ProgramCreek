__author__ = 'prnbs'


def findMedian(arr1, arr1_start, arr1_end, arr2, arr2_start, arr2_end):
    print "Left for arr1 ", arr1[arr1_start :arr1_end]
    print "Left for arr2 ", arr2[arr2_start : arr2_end]
    median1 = arr1[int((arr1_end + arr1_start)/2)]
    median2 = arr2[int((arr2_end + arr2_start)/2)]
    print median1
    print median2

    arr1_remaining = arr1_end - arr1_start
    arr2_remaining = arr2_end - arr2_start
    if median1 == median2:
        print median1
    if arr1_remaining <= 2 and arr2_remaining <= 2:
        print (median1 + median2)/2
        return
    if median1 > median2:
        # for arr1 new start and stop are
        if arr1_remaining > 2:
            arr1_end = int((arr1_end + arr1_start)/2) + 1
        # for arr2 new start and stop are
        if arr2_remaining > 2:
            arr2_start = int((arr2_end + arr2_start)/2)
        findMedian(arr1, arr1_start, arr1_end, arr2, arr2_start, arr2_end)
    if median1 < median2:
        if arr1_remaining > 2:
            arr1_start = int((arr1_end + arr1_start)/2)
        if arr2_remaining > 2:
            arr2_end = int((arr2_end + arr2_start)/2) + 1
        findMedian(arr1, arr1_start, arr1_end, arr2, arr2_start, arr2_end)


def verify(arr1, arr2):
    merged_arr = []
    merged_arr.extend(arr1)
    merged_arr.extend(arr2)
    merged_arr.sort()
    if len(merged_arr)%2 != 0:
        print merged_arr[int(len(merged_arr)/2)]
    else:
        index = int(len(merged_arr)/2)
        item1 = merged_arr[index]
        item2 = merged_arr[index+1]
        print "Averaged", (item1 + item2)/2


if __name__ == '__main__':
    arr1 = [i for i in range(1, 40, 2)]
    arr2 = [i for i in range(2, 80, 2)]
    # arr1 = [1, 5, 7, 10, 13]
    # arr2 = [11, 15, 23, 30, 45]
    print arr1
    print arr2
    findMedian(arr1, 0, len(arr1), arr2, 0, len(arr2))
    verify(arr1, arr2)
