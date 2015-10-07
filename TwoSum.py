__author__ = 'psinha4'

def two_sum(arr, target):
    dict = {}
    result = []
    for i, elem in enumerate(arr):
        if dict.has_key(elem):
            result.append(dict[elem])
            result.append(i)
            break
        else:
            dict[target - elem] = i
    return result


def two_sum_unsorted(arr, target):
    j = len(arr) - 1
    i = 0
    while i < j:
        if arr[i] + arr[j] == target:
            return i, j
        if target - arr[i] < arr[j]:
            j -= 1
        if target - arr[j] > arr[i]:
            i += 1
    print "No solution"


if __name__ == '__main__':
    arr = [8,3,6,2,4,9]
    res = two_sum(arr, 10)
    print arr[res[0]], arr[res[1]]
    arr.sort()
    print arr
    res = two_sum_unsorted(arr, 10)
    print arr[res[0]], arr[res[1]]
