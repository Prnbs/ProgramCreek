__author__ = 'prnbs'

def count_combinations(k, score_ways):
    combinations = [0 for i in range(k+1)]
    combinations[0] = 1

    for i, score, in enumerate(score_ways):
        for j in range(score, k+1):
            combinations[j] += combinations[j - score]

    return combinations

def find_closest(target, combinations):
    for i in range(len(combinations)-1, 1, -1):
        if combinations[i] != 0:
            return i
    return 0

if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        [N, K] = [int(x) for x in input().split()]
        W = [int(x) for x in input().split()]

        ways = count_combinations(K, W)
        # print(ways)
        closest = find_closest(K, ways)

        print(closest)
