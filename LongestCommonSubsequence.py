

def LCS_recursive(X, Y, i, j):
    if i < 0 or j < 0:
        return 0
    if X[i] == Y[j]:
        return 1 + LCS_recursive(X, Y, i-1, j-1)
    else:
        return max(LCS_recursive(X, Y, i-1, j), LCS_recursive(X, Y, i, j-1))


def LCS_dp(X, Y, table, I, J):
    for j in range(1, J+1):
        for i in range(1, I+1):
            if X[i-1] == Y[j-1]:
                table[j][i] = 1 + table[j-1][i-1]
            else:
                table[j][i] = max(table[j-1][i], table[j][i-1])
    return table


def trace_route(X, Y, table, I, J):
    path = []
    while I > 0 and J > 0:
        # go sideways
        while table[J][I] == table[J][I-1] and I >= 0:
            I -= 1
        if X[I-1] == Y[J-1]:
            path.append(X[I-1])
        else:
            # go up
            while table[J][I] == table[J-1][I] and J >= 0:
                J -= 1
            if X[I-1] == Y[J-1]:
                path.append(Y[J-1])
        I -= 1
        J -= 1
    path.reverse()
    print(" ".join(str(x) for x in path))


if __name__ == "__main__":
    [I, J] = [int(x) for x in input().strip().split()]
    A = [str(x) for x in input().strip().split()]
    B = [str(x) for x in input().strip().split()]
    table = [[0 for X in range(len(A)+1)] for Y in range(len(B)+1)]

    table = LCS_dp(A, B, table, len(A), len(B))
    trace_route(A, B, table, len(A), len(B))