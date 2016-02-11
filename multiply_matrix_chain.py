def merge_dims(left_arr, right_arr):
    if left_arr[1] == right_arr[0]:
        return [left_arr[0], right_arr[0], right_arr[1]]
    elif right_arr[1] == left_arr[0]:
        return [right_arr[0], left_arr[0], left_arr[1]]
    print(left_arr, right_arr)


def multiply(sub_list):
    prod = 1
    for i, item in enumerate(sub_list):
        prod *= item
    return prod


def compute_dim(sublist):
    return [sublist[0], sublist[2]]


def get_dim_of(mat_dim, array_number):
    return [mat_dim[array_number], mat_dim[array_number+1]]


def min_multiply_chain(mat_dim):
    memo = [[0 for i in range(len(mat_dim)-1)] for j in range(2, len(mat_dim))]
    dims = [[0 for i in range(len(mat_dim)-1)] for j in range(2, len(mat_dim))]

    for i in range(len(mat_dim)):
        for j in range(len(mat_dim)-(i+2)):
            if i == 0:
                # set base case
                memo[i][j] = multiply(mat_dim[j:j+3])
                dims[i][j] = (compute_dim(mat_dim[j:j+3]), j+2)
            else:
                left_mat1 = get_dim_of(mat_dim, j)
                right_mat1, next1 = dims[i-1][j+1]
                merged_dims1 = merge_dims(left_mat1, right_mat1)
                cost1 = multiply(merged_dims1) +  memo[i-1][j+1]

                right_mat2, next2 = dims[i-1][j]
                left_mat2 = get_dim_of(mat_dim,next2)
                merged_dims2 = merge_dims(right_mat2, left_mat2)
                cost2 = multiply(merged_dims2) + memo[i-1][j]
                memo[i][j] = min(cost1, cost2)
                if cost1 < cost2:
                    dims[i][j] = ([merged_dims1[0], merged_dims1[2]], next1)
                else:
                    dims[i][j] = ([merged_dims2[0], merged_dims2[2]], next2)
    return memo[len(memo) - 1][0]

if __name__ == '__main__':
    chain = [10,20,30,40,30]
    print(min_multiply_chain(chain))