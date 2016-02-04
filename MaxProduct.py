import sys


def compute_max_product_greedy(input_arr):
    negative_parity = 0
    smallest_negative_num_seen = -1 * sys.maxsize
    max_product = 1
    total_zeros = 0
    length_of_input = len(input_arr)
    for i, item in enumerate(input_arr):
        if item == 0:
            total_zeros += 1
            continue
        if item < 0:
            negative_parity += 1
            if abs(smallest_negative_num_seen) > abs(item):
                smallest_negative_num_seen = item
        max_product *= item
    # corner case: 1 -ve number and all others zero
    if negative_parity == 1 and total_zeros == length_of_input - 1:
        return 0
    # corner case: all zeroes
    if total_zeros == length_of_input:
        return 0
    # if odd number of -ves, then remove the product due to the smallest (in value) -ve number
    if negative_parity % 2 == 1:
        max_product /= smallest_negative_num_seen

    return int(max_product)


def compute_max_product_dp_2(input_arr):
    max_product_arr = 0
    min_product_arr = 0

    for i, item in enumerate(input_arr):
        if i == 0:
            if input_arr[i] < 0:
                min_product_arr = item
            else:
                max_product_arr = item
        else:
            prev_max = max_product_arr
            prev_min = min_product_arr
            if item > 0:
                max_product_arr = prev_max * item
                min_product_arr = prev_min * item
            elif item < 0:
                max_product_arr = max(prev_min * item, prev_max)
                min_product_arr = min(min(prev_min, item), prev_max * item)
    return max_product_arr


if __name__ == "__main__":
    input_arr = [int(a) for a in input().split()]
    print("greedy ", compute_max_product_greedy(input_arr))
    print("dp ", compute_max_product_dp_2(input_arr))
