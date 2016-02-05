

def LCS_recursive(X, Y, i, j):
    len = 0
    if i == 0 or j == 0:
        if X[i] == Y[j]:
            return 1
        else:
            return 0
    if X[i] == Y[j]:
        return (1 + LCS_recursive(X, Y, i-1, j-1))
    else:
        return max(LCS_recursive(X, Y, i-1, j), LCS_recursive(X, Y, i, j-1))


if __name__ == "__main__":
    A = "ABCBDAB"
    B = "BDCABA"

    print(LCS_recursive(A, B, len(A)-1, len(B)-1))