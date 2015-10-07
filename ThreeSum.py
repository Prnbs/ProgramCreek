__author__ = 'prnbs'

def three_sum(arr, target, sort=False):
    if sort:
        arr.sort()
    # store indices of elems already contributing to sum
    dict = {}
    # store all set of results
    all_result = []
    for i, elem in enumerate(arr):
        starter = elem
        new_target = target - starter
        j = i + 1
        k = len(arr) - 1
        result = []

        while j < k:
            # ensure this index hasn't already contributed
            while dict.has_key(j):
                j += 1
            while dict.has_key(k):
                k -= 1
            if j > k:
                break
            if (arr[k] + arr[j] + starter) == target:
                result.append(arr[i])
                result.append(arr[j])
                result.append(arr[k])
                dict[j] = j
                dict[k] = k
                if not sort:
                    return result
                all_result.append(result)
                break
            # print i, j , k
            if (arr[j] + arr[k]) < new_target:
                j += 1
            if (arr[j] + arr[k]) > new_target:
                k -= 1
    return all_result

if __name__ == '__main__':
    arr = [4, 5, 1, 7, 3, 9, 10, -8, 2, -4, -2]
    result = three_sum(arr, 0, True)
    print result