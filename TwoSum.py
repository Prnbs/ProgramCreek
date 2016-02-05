__author__ = 'psinha4'

def two_sum(arr, target):
    dict = {}
    result = []
    for i, elem in enumerate(arr):
        if elem in dict:
            result.append(dict[elem])
            result.append(elem)
            break
        else:
            dict[target - elem] = elem
    return result


def two_sum_sorted(arr, target):
    j = len(arr) - 1
    i = 0
    while i < j:
        if arr[i] + arr[j] == target:
            return i, j
        if target - arr[i] < arr[j]:
            j -= 1
        if target - arr[j] > arr[i]:
            i += 1
    print ("No solution")


if __name__ == '__main__':
    arr = [8,3,6,2,4,9]
    res = two_sum(arr, 10)
    print (res[0], res[1])
    arr.sort()
    print (arr)
    res = two_sum_sorted(arr, 10)
    print (arr[res[0]], arr[res[1]])
