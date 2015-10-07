__author__ = 'prnbs'

from ThreeSum import three_sum


def four_sum(arr, target):
    arr.sort()
    all_results = []
    print arr
    for i, elem in enumerate(arr):
        result = []
        new_target = target - elem
        result = three_sum(arr[i+1:], new_target, sort=False)
        if len(result) > 0:
            print result
            result.append(elem)
            all_results.append(result)
    return all_results

if __name__ == '__main__':
    array = [4, 5, 1, 7, 3, 9, 10, -8, 2, -4, -2]
    result = four_sum(array, 5)
    print result

