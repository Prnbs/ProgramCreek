import random

def swap(input_arr, i, j):
    input_arr[i], input_arr[j] = input_arr[j], input_arr[i]


def get_next_higher_pos(high_pos, size, input_arr, pivot):
     while high_pos <= size:
        if high_pos == size:
            break
        if input_arr[high_pos] <= input_arr[pivot] and high_pos != pivot:
            break
        else:
            high_pos += 1
     return high_pos


def dutch_flag(input_arr, pivot):
    smaller_pos = 0
    higher_pos = pivot + 1
    middle = pivot
    size = len(input_arr)
    print("pivot: ", input_arr[pivot])

    higher_pos = get_next_higher_pos(higher_pos, size, input_arr, pivot)

    while smaller_pos < pivot:
        if input_arr[smaller_pos] > input_arr[pivot] and smaller_pos < pivot:
            # swap is needed
            # check if higher pos is useable
            if higher_pos < size:
                swap(input_arr, smaller_pos, higher_pos)
            else:
                # higher_pos can't be used so put this item to the right of pivot'
                swap(input_arr, smaller_pos, pivot)
                if middle == pivot:
                    swap(input_arr, smaller_pos, pivot-1)
                else:
                    swap(input_arr, middle-1, smaller_pos)
                middle -= 1
                pivot -= 1
            if input_arr[smaller_pos] < input_arr[pivot]:
                smaller_pos += 1
            higher_pos = get_next_higher_pos(higher_pos, size, input_arr, pivot)
        elif higher_pos < size and input_arr[higher_pos] <= input_arr[pivot]:
            # first put this item just to the right of the pivot
            swap(input_arr, higher_pos, pivot+1)
            # if this item is equal to pivot then just move pivot 1 step right
            if input_arr[pivot+1] == input_arr[pivot]:
                pivot += 1
            else:
                swap(input_arr, pivot+1, pivot)
                if middle == pivot:
                    # only 1 instance of pivot seen so far
                    pivot += 1
                    middle = pivot
                else:
                    swap(input_arr, pivot, middle)
                    middle += 1
                    pivot += 1
            higher_pos = get_next_higher_pos(higher_pos, size, input_arr, pivot)
        elif input_arr[smaller_pos] == input_arr[pivot] and smaller_pos < pivot and smaller_pos < middle:
            swap(input_arr, middle-1, smaller_pos)
            middle -= 1
        else:
            smaller_pos += 1
    return input_arr


if __name__ == '__main__':
    # input_Arr = [random.randint(1, 20) for i in range(13)]
    input_Arr = [3, 18, 10, 1, 16, 19, 5, 5, 14, 12, 17, 17, 2]
    print(input_Arr)
    result = dutch_flag(input_Arr, 4)
    print (input_Arr)
