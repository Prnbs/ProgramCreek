import sys

def find_min_neighbour(memo, i, j):
    up = memo[i-1][j]
    left = memo[i][j-1]
    diag = memo[i-1][j-1]
    return min([up, left, diag])


def find_min_neighbour_forward(memo, i, j, length, width):
    down = sys.maxsize
    right = sys.maxsize
    diag = sys.maxsize

    if i+1 <= length:
        down = memo[i+1][j]
    if j+1 <= width:
        right = memo[i][j+1]
    if i+1 <= length and j+1 <= width:
        diag = memo[i+1][j+1]
    smallest = min([down, right, diag])
    if smallest == down:
        return smallest, i+1, j
    if smallest == right:
        return smallest, i, j+1
    return smallest, i+1, j+1


def compute_changes(memo, string_input, string_target):
    INSERT = 1
    DELETE = 2
    REPLACE = 0
    width = len(string_target)
    height = len(string_input)
    operations = []
    i = j = 0
    prev_cost = 0
    while i != height+1 and j != width+1:
        min_cost, i, j = find_min_neighbour_forward(memo, i, j, height, width)
        if min_cost == sys.maxsize:
            break
        if min_cost - prev_cost == 0:
            operations.append('M/R')
        elif min_cost - prev_cost == INSERT:
            operations.append('I')
        else:
            operations.append('D')
        prev_cost = min_cost
    return operations



def calculate_edit_distance(string_input, string_target):
    width = len(string_target)
    height = len(string_input)
    INSERT = 1
    DELETE = 1
    REPLACE = 1

    memo = [[0 for i in range(width+1)] for i in range(height+1)]

    # set base cases for 0th row
    # all inserts
    for i in range(1, width+1):
        memo[0][i] = memo[0][i-1] + INSERT

    # set base cases for 0th column
    # all deletes
    for i in range(1, height+1):
        memo[i][0] = memo[i-1][0] + DELETE

    for i in range(1, height+1):
        for j in range(1, width+1):
            if i == j:
                # same position in both strings
                if string_input[i-1] == string_target[j-1]:
                    memo[i][j] = find_min_neighbour(memo, i, j)
                else:
                    # replacement is cheapest since indexes match
                    memo[i][j] = find_min_neighbour(memo, i, j) + REPLACE
            elif i > j:
                # input string is longer than target
                if string_input[i-1] == string_target[j-1]:
                    memo[i][j] = find_min_neighbour(memo, i, j)
                else:
                    # delete must happen
                    memo[i][j] = find_min_neighbour(memo, i, j) + DELETE
            else:
                # input string is shorter than target
                if string_input[i-1] == string_target[j-1]:
                    memo[i][j] = find_min_neighbour(memo, i, j)
                else:
                    # insert must happen
                    memo[i][j] = find_min_neighbour(memo, i, j) + INSERT
    return memo

if __name__ == '__main__':
    str_input = "sweet"
    str_target = "feet"
    memo = calculate_edit_distance(str_input, str_target)
    operations = compute_changes(memo, str_input, str_target)
    print (operations)
