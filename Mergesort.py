

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

if __name__ == '__main__':
    import random
    unsorted_arr = [random.randint(1, 20) for i in range(20)]
    print unsorted_arr
    sorted_Arr = mergesort(unsorted_arr)
    print sorted_Arr

